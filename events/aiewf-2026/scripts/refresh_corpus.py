#!/usr/bin/env python3
"""Weekly incremental refresh of the AIEWF 2026 corpus.

Automates the manual refresh performed on 2026-08-19 (commit 788d157), which took
the corpus from 231 to 246 talks. It re-fetches the conference's YouTube playlists,
ingests any newly published official-playlist talks through the existing pipeline,
rebuilds the wiki, and pushes -- but only when every gate passes.

    python3 scripts/refresh_corpus.py --dry-run     # discovery + triage only
    python3 scripts/refresh_corpus.py --no-push     # full run, commit but no push
    python3 scripts/refresh_corpus.py               # full run

Every step is a hard gate. The exit code is the contract: 0 means the corpus is in
a good state (which very often means "nothing new was published this week"), and
nonzero means something needs a human. There is no partial success -- a run that
distills new talks but fails quote verification exits nonzero and pushes nothing.

Design notes worth defending, because each looks like an omission:

  * ONLY OFFICIAL-2026-PLAYLIST MEMBERSHIP AUTO-INGESTS. Videos that appear only in
    a topical track playlist are computed and reported but never ingested. 2025 or
    non-fair contamination is this project's stated embarrassment risk, and the
    topical playlists are cross-year, so that class of candidate stays a human call.

  * A NO-OP WEEK TOUCHES data/ NOT AT ALL. When triage finds nothing, the run exits
    before normalize.py, so the git tree is provably unchanged. Anything else would
    make "did this week change the corpus?" unanswerable from `git status`.

  * A TALK WITH NO ENGLISH CAPTIONS YET IS SKIPPED, NOT FAILED. It stays out of
    index.json, so next week's discovery finds it again for free.

  * PROSE IS NEVER REWRITTEN. Step 10 replaces counts under strict anchored regexes
    that must each match exactly once. If the maturity distribution ever gains a
    settled concept, the run fails rather than editing the "zero settled" headline:
    that is a claim, not a count.

Model access is subscription-only, via the pipeline's own `claude -p` runners
(run_passA.py, run_conceptsB.py, run_passC.py). No Anthropic API key is used,
required, or passed to any child.
"""
import argparse
import collections
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
REPO = os.path.dirname(os.path.dirname(ROOT))

RAW = os.path.join(ROOT, "raw")
CAPS = os.path.join(RAW, "caps")
DATA = os.path.join(ROOT, "data")
INDEX = os.path.join(DATA, "index.json")
CONCEPTS = os.path.join(DATA, "concepts")
PASSA = os.path.join(DATA, "passA")
PASSC = os.path.join(DATA, "passC")
ALL_PLAYLISTS = os.path.join(RAW, "all_playlists.json")
PLAYLIST_MEMBERS = os.path.join(RAW, "playlist_members.json")
VIDEO_IDS = os.path.join(RAW, "video_ids.txt")

YTDLP_ENV = "/tmp/ytdlp-env"
YTDLP = os.path.join(YTDLP_ENV, "bin", "yt-dlp")
CHANNEL_PLAYLISTS = "https://www.youtube.com/@aiDotEngineer/playlists"

# The official 2026 main set. Two structural playlists plus a pattern, because the
# fair adds named track playlists mid-stream: "Generative Media: AI Engineer World's
# Fair 2026" did not exist at build time and carried 8 of the 15 talks the
# 2026-08-19 refresh found.
STRUCTURAL_2026 = {
    "AIE World's Fair 2026 Complete Playlist",
    "AI Engineer World's Fair Online Track 2026",
}
MAIN_2026_RE = re.compile(r"AI Engineer World's Fair 2026", re.I)

# Playlists that mark a video as belonging to a DIFFERENT event. Verbatim from
# find_more.py; keep the two in step.
OTHER_EVENT_RE = re.compile(
    r"europe|code 20|world's fair 2024|world's fair 2025|"
    r"summit|2023|2024|: ai engineer world's fair 2025", re.I)

LIVESTREAM_RE = re.compile(r"livestream|day [12].*(track|stage)|full day", re.I)
LIVESTREAM_MAX_SEC = 4 * 3600

# Quote loss above this share of a new talk's quotes is a transcript-corruption
# signature (see BUILD.md, the caption word-gluing incident), not model variance.
QUOTE_DROP_CEILING = 0.05

PASS_ATTEMPTS = 3          # total attempts, not retries
CONCEPT_BATCH_SIZE = 100
CONCEPT_CONCURRENCY = 2
PASS_CONCURRENCY = "2"

REPORT = {
    "status": "failed",
    "dry_run": False,
    "failed_step": None,
    "message": "",
    "new_talks": 0,
    "new_talk_details": [],
    "deduped_video_ids": [],
    "no_caption_video_ids": [],
    "talks_before": None,
    "talks_after": None,
    "concepts_total": None,
    "concepts_regenerated": 0,
    "quotes_total": None,
    "still_private": 0,
    "track_only_unresolved": 0,
    "track_only_candidates": [],
    "track_only_total": 0,
    "maturity": {},
    "evals": None,
    "committed": False,
    "pushed": False,
    "docs_needing_human_update": [],
}


# ---------------------------------------------------------------------------
# plumbing
# ---------------------------------------------------------------------------

def log(msg=""):
    print(msg, flush=True)


def section(title):
    log()
    log("=" * 78)
    log(title)
    log("=" * 78)


def finish(status, step=None, message=""):
    """Print the human summary tail plus the machine-readable last line, then exit."""
    REPORT["status"] = status
    REPORT["failed_step"] = step
    REPORT["message"] = message
    if status != "ok":
        log()
        log(f"FAILED at {step}: {message}")
    log()
    log("REFRESH_RESULT=" + json.dumps(REPORT, ensure_ascii=False, sort_keys=True))
    sys.exit(0 if status == "ok" else 1)


def fail(step, message):
    finish("failed", step, message)


def child_env():
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)  # subscription auth only, always
    return env


def run_cmd(args, cwd=ROOT, capture=False, timeout=None, check=True, step=None):
    """Run a child. capture=True also echoes, so gates can parse what the log shows."""
    log(f"$ {' '.join(args)}")
    try:
        if capture:
            proc = subprocess.run(args, cwd=cwd, env=child_env(), timeout=timeout,
                                  capture_output=True, text=True)
            out = (proc.stdout or "") + (proc.stderr or "")
            log(out.rstrip())
        else:
            proc = subprocess.run(args, cwd=cwd, env=child_env(), timeout=timeout)
            out = ""
    except subprocess.TimeoutExpired:
        if check:
            fail(step or args[0], f"timed out after {timeout}s: {' '.join(args)}")
        return 124, ""
    if check and proc.returncode != 0:
        fail(step or args[0],
             f"exited {proc.returncode}: {' '.join(args)}" + (f"\n{out[-3000:]}" if out else ""))
    return proc.returncode, out


def ytdlp_print(url, template, timeout=300):
    """One yt-dlp --flat-playlist/--print call. Returns (rc, stdout lines)."""
    try:
        proc = subprocess.run([YTDLP, "--flat-playlist", "--print", template, url],
                              capture_output=True, text=True, timeout=timeout,
                              env=child_env())
    except subprocess.TimeoutExpired:
        return 124, []
    return proc.returncode, [line for line in proc.stdout.splitlines() if line.strip()]


def ensure_ytdlp():
    """The venv lives in /tmp and does not survive a reboot. Rebuild it, or die loudly."""
    if os.path.exists(YTDLP):
        try:
            probe = subprocess.run([YTDLP, "--version"], capture_output=True,
                                   text=True, timeout=60)
            if probe.returncode == 0:
                log(f"yt-dlp {probe.stdout.strip()} at {YTDLP}")
                return
        except Exception:
            pass
        log(f"{YTDLP} exists but does not run; rebuilding the venv.")
    log(f"Creating yt-dlp venv at {YTDLP_ENV} ...")
    try:
        subprocess.run([sys.executable, "-m", "venv", YTDLP_ENV],
                       check=True, capture_output=True, text=True, timeout=300)
        subprocess.run([os.path.join(YTDLP_ENV, "bin", "pip"), "install", "-q", "yt-dlp"],
                       check=True, capture_output=True, text=True, timeout=900)
        probe = subprocess.run([YTDLP, "--version"], capture_output=True,
                               text=True, timeout=60)
        if probe.returncode != 0:
            raise RuntimeError(probe.stderr.strip())
    except Exception as exc:
        fail("ytdlp", f"could not create a working yt-dlp venv at {YTDLP_ENV}: {exc}")
    log(f"yt-dlp {probe.stdout.strip()} installed.")


def emit_usage(rows):
    """Print the CRON_USAGE marker run_plain_cron.sh sums into the run's token total.

    The pipeline's `claude -p` runners record per-call usage in their own runlogs
    rather than printing the marker, so a run's spend would otherwise show as "—"
    on the dashboard.
    """
    totals = {"input": 0, "output": 0, "cache_read": 0, "cache_creation": 0}
    for row in rows:
        if not row.get("ok"):
            continue
        cache_read = int(row.get("cache_read") or 0)
        cache_creation = int(row.get("cache_creation") or 0)
        totals["cache_read"] += cache_read
        totals["cache_creation"] += cache_creation
        totals["input"] += max(int(row.get("tokens_in") or 0) - cache_read - cache_creation, 0)
        totals["output"] += int(row.get("tokens_out") or 0)
    if any(totals.values()):
        log("CRON_USAGE " + json.dumps(totals, separators=(",", ":")))


def read_runlog_tail(path, since_line):
    """Rows appended to a runner's _runlog.jsonl since `since_line`."""
    if not os.path.exists(path):
        return []
    rows = []
    with open(path) as handle:
        for i, line in enumerate(handle):
            if i < since_line or not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def count_lines(path):
    if not os.path.exists(path):
        return 0
    with open(path) as handle:
        return sum(1 for _ in handle)


def load_index():
    with open(INDEX) as handle:
        return json.load(handle)


def passa_slugs():
    return {fn[:-5] for fn in os.listdir(PASSA)
            if fn.endswith(".json") and not fn.startswith(("_", "."))}


def load_passa(slug):
    with open(os.path.join(PASSA, f"{slug}.json")) as handle:
        return json.load(handle)


# ---------------------------------------------------------------------------
# 1. discovery
# ---------------------------------------------------------------------------

def discover():
    section("1. DISCOVERY -- re-fetch the channel's playlists")
    ensure_ytdlp()

    rc, lines = ytdlp_print(CHANNEL_PLAYLISTS, "%(id)s|%(title)s")
    if rc != 0 or not lines:
        fail("discovery", f"could not list playlists for {CHANNEL_PLAYLISTS} (rc={rc}); "
                          "the previous all_playlists.json was left untouched")
    entries = [line.split("|", 1) for line in lines if "|" in line]
    log(f"{len(entries)} playlists on the channel")

    playlists = {}
    for i, (pid, name) in enumerate(entries, 1):
        pid, name = pid.strip(), name.strip()
        prc, vids = ytdlp_print(f"https://www.youtube.com/playlist?list={pid}", "%(id)s")
        if prc != 0:
            log(f"[{i}/{len(entries)}] {name}: FETCH FAILED (rc={prc})")
        playlists[name] = vids
        log(f"[{i}/{len(entries)}] {name}: {len(vids)}")

    # Integrity gate before overwriting the cache. A partially-fetched or shape-changed
    # response written over all_playlists.json would silently poison every later step,
    # and the damage would look like "the fair deleted a bunch of talks".
    missing_structural = STRUCTURAL_2026 - set(playlists)
    if missing_structural:
        fail("discovery", "the official 2026 structural playlist(s) "
                          f"{sorted(missing_structural)} were not in the fetch; refusing to "
                          "overwrite raw/all_playlists.json")
    known = {rec["video_id"] for rec in load_index()}
    seen = {v for vids in playlists.values() for v in vids}
    covered = len(known & seen) / len(known) if known else 1.0
    log(f"coverage of the existing corpus by the fresh fetch: {covered*100:.1f}%")
    if covered < 0.95:
        fail("discovery", f"the fresh playlist fetch only accounts for {covered*100:.1f}% of the "
                          f"{len(known)} talks already in the corpus, which reads as a partial or "
                          "malformed fetch; refusing to overwrite raw/all_playlists.json")

    if os.path.exists(ALL_PLAYLISTS):
        backup = f"{ALL_PLAYLISTS}.bak-{time.strftime('%Y%m%d')}"
        shutil.copy2(ALL_PLAYLISTS, backup)
        log(f"previous cache backed up -> {os.path.relpath(backup, ROOT)}")
    with open(ALL_PLAYLISTS, "w") as handle:
        json.dump(playlists, handle, indent=2, ensure_ascii=False)
    log(f"wrote {os.path.relpath(ALL_PLAYLISTS, ROOT)} ({len(playlists)} playlists)")

    vid2pl = {}
    for name, vids in playlists.items():
        for v in vids:
            vid2pl.setdefault(v, []).append(name)

    main_names = {n for n in playlists
                  if n in STRUCTURAL_2026 or MAIN_2026_RE.search(n)}
    log(f"official 2026 playlists ({len(main_names)}): {sorted(main_names)}")

    other_event_vids = set()
    for name, vids in playlists.items():
        if OTHER_EVENT_RE.search(name):
            other_event_vids.update(vids)

    main_candidates = sorted(
        {v for n in main_names for v in playlists[n]} - known)

    # find_more.py's rule, kept as a REPORT-ONLY signal: 2026-plausible videos that
    # live only in topical (cross-year) playlists.
    track_only = set()
    for name, vids in playlists.items():
        if OTHER_EVENT_RE.search(name) or name in main_names:
            continue
        for v in vids:
            if v not in known and v not in other_event_vids:
                track_only.add(v)
    track_only -= set(main_candidates)

    log(f"already in the corpus:            {len(known)}")
    log(f"official-2026-playlist candidates:{len(main_candidates):>4}")
    log(f"track-only candidates (report):   {len(track_only):>4}")
    return playlists, vid2pl, main_names, main_candidates, sorted(track_only)


# ---------------------------------------------------------------------------
# 2. triage
# ---------------------------------------------------------------------------

def fetch_meta(video_ids, batch_size=40):
    """{video_id: (upload_date, duration, title)} for everything that resolved.

    Batched because the track-only candidate set is in the hundreds and one
    yt-dlp process per video spends most of its life in interpreter startup.
    Videos that are private, removed, or otherwise unavailable simply produce no
    stdout line, so absence from the returned dict IS the "unavailable" signal --
    which is why the process exit code is deliberately ignored here.
    """
    found = {}
    ids = list(video_ids)
    for start in range(0, len(ids), batch_size):
        chunk = ids[start:start + batch_size]
        args = [YTDLP, "--flat-playlist", "--ignore-errors", "--print",
                "%(id)s|%(upload_date)s|%(duration)s|%(title)s"]
        args += [f"https://www.youtube.com/watch?v={v}" for v in chunk]
        try:
            proc = subprocess.run(args, capture_output=True, text=True,
                                  timeout=60 + 15 * len(chunk), env=child_env())
        except subprocess.TimeoutExpired:
            log(f"  metadata batch {start // batch_size + 1} timed out; "
                "its videos are treated as unavailable this run")
            continue
        for line in proc.stdout.splitlines():
            parts = line.strip().split("|", 3)
            if len(parts) == 4 and parts[0] in set(chunk):
                found[parts[0]] = (parts[1], parts[2], parts[3])
        log(f"  metadata batch {start // batch_size + 1}: "
            f"{len(chunk)} requested, {sum(1 for v in chunk if v in found)} resolved")
    return found


def is_2026_or_later(upload_date):
    year = upload_date[:4]
    return year.isdigit() and int(year) >= 2026


def is_livestream_block(title, duration):
    return bool(LIVESTREAM_RE.search(title)) or (
        duration.isdigit() and int(duration) > LIVESTREAM_MAX_SEC)


def triage(vid2pl, main_candidates, track_only):
    section("2. TRIAGE -- provenance and shape gates on every candidate")
    accepted, private, rejected, livestream, unresolved = [], [], [], [], []

    log(f"fetching metadata for {len(main_candidates)} official-playlist candidate(s)")
    meta = fetch_meta(main_candidates)
    for vid in main_candidates:
        row = meta.get(vid)
        if row is None:
            private.append(vid)
            log(f"  {vid} PRIVATE/UNAVAILABLE")
            continue
        upload_date, duration, title = row
        if not is_2026_or_later(upload_date):
            rejected.append(vid)
            log(f"  {vid} REJECT pre-2026 upload {upload_date}: {title}")
            continue
        if is_livestream_block(title, duration):
            livestream.append(vid)
            log(f"  {vid} LIVESTREAM (excluded by design): {title}")
            continue
        accepted.append({"video_id": vid, "upload_date": upload_date,
                         "duration": duration, "title": title,
                         "playlists": vid2pl.get(vid, [])})
        log(f"  {vid} ACCEPT {upload_date} {duration}s: {title}")

    # Track-only candidates are report-only, and there are hundreds of them
    # because the channel's topical playlists are cross-year. Their metadata is
    # cached permanently so this costs one fetch per video ever, not per week,
    # and so the report can distinguish "new since the last run and genuinely
    # needs a human" from the standing backlog.
    cache_path = os.path.join(RAW, "track_only_cache.json")
    cache = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path) as handle:
                cache = json.load(handle)
        except ValueError:
            cache = {}
    uncached = [v for v in track_only if v not in cache]
    log()
    log(f"track-only candidates: {len(track_only)} total, {len(uncached)} not yet triaged")
    if uncached:
        fresh = fetch_meta(uncached)
        for vid in uncached:
            row = fresh.get(vid)
            if row is None:
                # Not cached: an unavailable video may go public later and should
                # be re-checked, unlike one already classified. Counted separately
                # from `private`, which means "private on an OFFICIAL 2026 playlist"
                # -- the number the project actually reports and watches.
                unresolved.append(vid)
                continue
            upload_date, duration, title = row
            cache[vid] = {
                "upload_date": upload_date, "duration": duration, "title": title,
                "eligible": is_2026_or_later(upload_date)
                and not is_livestream_block(title, duration),
                "first_seen": time.strftime("%Y-%m-%d"),
            }
        with open(cache_path, "w") as handle:
            json.dump(cache, handle, indent=2, ensure_ascii=False)

    eligible = [v for v in track_only if cache.get(v, {}).get("eligible")]
    new_for_review = [v for v in eligible if v in uncached]
    track_only_rows = [{"video_id": v, "upload_date": cache[v]["upload_date"],
                        "title": cache[v]["title"], "playlists": vid2pl.get(v, [])}
                       for v in new_for_review]

    REPORT["still_private"] = len(private)
    REPORT["track_only_unresolved"] = len(unresolved)
    REPORT["track_only_candidates"] = track_only_rows
    REPORT["track_only_total"] = len(eligible)

    log()
    log(f"accepted for ingestion: {len(accepted)}")
    log(f"still private on an official 2026 playlist: {len(private)}")
    log(f"track-only videos that did not resolve:     {len(unresolved)}")
    log(f"rejected (pre-2026):    {len(rejected)}")
    log(f"livestream blocks:      {len(livestream)}")
    log(f"track-only eligible:    {len(eligible)} ({len(track_only_rows)} new this run)")
    for row in track_only_rows:
        log(f"  REVIEW {row['video_id']} {row['upload_date']} {row['title']}")
        log(f"         playlists: {row['playlists']}")
    return accepted


# ---------------------------------------------------------------------------
# 3. harvest
# ---------------------------------------------------------------------------

def harvest(accepted):
    section("3. HARVEST -- captions + metadata for the accepted candidates")
    os.makedirs(CAPS, exist_ok=True)
    harvested, no_captions = [], []

    for i, row in enumerate(accepted, 1):
        vid = row["video_id"]
        cap = os.path.join(CAPS, f"{vid}.en.json3")
        if os.path.exists(cap):
            log(f"[{i}/{len(accepted)}] {vid} (cached)")
            harvested.append(row)
            continue
        # Flags copied from harvest.sh. Keep the two in step.
        args = [YTDLP, "--skip-download",
                "--write-auto-subs", "--sub-langs", "en", "--sub-format", "json3",
                "--write-info-json", "--sleep-requests", "1",
                "-o", os.path.join(CAPS, "%(id)s.%(ext)s"),
                f"https://www.youtube.com/watch?v={vid}"]
        try:
            proc = subprocess.run(args, capture_output=True, text=True,
                                  timeout=180, env=child_env())
        except subprocess.TimeoutExpired:
            proc = None
        if os.path.exists(cap):
            log(f"[{i}/{len(accepted)}] {vid} OK")
            harvested.append(row)
        else:
            detail = "timeout" if proc is None else f"rc={proc.returncode}"
            log(f"[{i}/{len(accepted)}] {vid} NO ENGLISH CAPTIONS YET ({detail}) -- "
                "skipped this week, retried next run")
            no_captions.append(vid)

    REPORT["no_caption_video_ids"] = no_captions

    if harvested:
        existing = []
        if os.path.exists(VIDEO_IDS):
            with open(VIDEO_IDS) as handle:
                existing = [line.strip() for line in handle if line.strip()]
        added = [r["video_id"] for r in harvested if r["video_id"] not in set(existing)]
        if added:
            with open(VIDEO_IDS, "w") as handle:
                handle.write("\n".join(existing + added) + "\n")
            log(f"appended {len(added)} id(s) to {os.path.relpath(VIDEO_IDS, ROOT)}")

    log(f"harvested with captions: {len(harvested)} | awaiting captions: {len(no_captions)}")
    return harvested


# ---------------------------------------------------------------------------
# 4. normalize + enrich
# ---------------------------------------------------------------------------

def regenerate_playlist_members():
    """raw/playlist_members.json from the FRESH all_playlists.json, no refetch.

    playlist_tracks.py uses this file as a cache and only fetches when it is absent,
    so leaving a stale copy in place is how the enrichment silently misses a new
    track playlist. Reproduces its own filter: playlists restricted to our video ids,
    empty playlists dropped.
    """
    with open(ALL_PLAYLISTS) as handle:
        playlists = json.load(handle)
    ours = {rec["video_id"] for rec in load_index()}
    members = {}
    for name, vids in playlists.items():
        hit = [v for v in vids if v in ours]
        if hit:
            members[name] = hit
    with open(PLAYLIST_MEMBERS, "w") as handle:
        json.dump(members, handle, indent=2, ensure_ascii=False)
    log(f"regenerated {os.path.relpath(PLAYLIST_MEMBERS, ROOT)} "
        f"({len(members)} playlists covering {len(ours)} talks)")


def normalize_and_enrich(snapshot, harvested):
    section("4. NORMALIZE + ENRICH")
    run_cmd([sys.executable, os.path.join(SCRIPTS, "normalize.py")], step="normalize")
    run_cmd([sys.executable, os.path.join(SCRIPTS, "join_schedule.py")], step="join_schedule")
    regenerate_playlist_members()
    run_cmd([sys.executable, os.path.join(SCRIPTS, "playlist_tracks.py")], step="playlist_tracks")

    after = {rec["video_id"]: rec for rec in load_index()}
    problems = []
    for vid, prior in snapshot.items():
        now = after.get(vid)
        if now is None:
            problems.append(f"  video_id {vid} ({prior['slug']}) DISAPPEARED from index.json")
            continue
        if now["slug"] != prior["slug"]:
            problems.append(f"  {vid}: slug {prior['slug']!r} -> {now['slug']!r}")
        if now["word_count"] != prior["word_count"]:
            problems.append(f"  {vid} ({prior['slug']}): word_count "
                            f"{prior['word_count']} -> {now['word_count']}")
    if problems:
        fail("normalize", "the refresh mutated pre-existing talks, which an incremental "
                          "refresh must never do:\n" + "\n".join(problems))

    new_ids = [v for v in after if v not in snapshot]
    # A harvested candidate that never reached the index was absorbed into an existing
    # slug by normalize.py's re-upload dedup. Expected, and worth naming in the report.
    deduped = [r["video_id"] for r in harvested if r["video_id"] not in after]
    REPORT["deduped_video_ids"] = deduped

    log()
    log(f"pre-existing talks unchanged: {len(snapshot)}")
    log(f"new talks in index.json:      {len(new_ids)}")
    if deduped:
        log(f"deduplicated by slug (re-uploads of existing talks): {deduped}")
    return [after[v] for v in new_ids]


# ---------------------------------------------------------------------------
# 5. pass A
# ---------------------------------------------------------------------------

def pass_a():
    section("5. PASS A -- per-talk distillation")
    import run_passA

    runlog = os.path.join(PASSA, "_runlog.jsonl")
    start_line = count_lines(runlog)
    wanted = {rec["slug"] for rec in load_index()} - run_passA.SKIP_SLUGS

    for attempt in range(1, PASS_ATTEMPTS + 1):
        missing = sorted(s for s in wanted if not run_passA.done(s))
        if not missing:
            break
        log(f"attempt {attempt}/{PASS_ATTEMPTS}: {len(missing)} talk(s) outstanding")
        run_cmd([sys.executable, os.path.join(SCRIPTS, "run_passA.py"),
                 "--concurrency", PASS_CONCURRENCY], step="passA", check=False)

    emit_usage(read_runlog_tail(runlog, start_line))

    missing = sorted(s for s in wanted if not run_passA.done(s))
    if missing:
        fail("passA", f"{len(missing)} talk(s) still have no valid Pass A output after "
                      f"{PASS_ATTEMPTS} attempts: {missing}")
    log(f"Pass A complete for all {len(wanted)} distillable talks.")


# ---------------------------------------------------------------------------
# 6. quote gate
# ---------------------------------------------------------------------------

def quote_gate(new_slugs):
    section("6. QUOTE GATE -- deterministic verbatim verification")

    def quote_counts():
        return {slug: len(load_passa(slug)["passA"].get("notable_quotes") or [])
                for slug in new_slugs if os.path.exists(os.path.join(PASSA, f"{slug}.json"))}

    before = quote_counts()
    run_cmd([sys.executable, os.path.join(SCRIPTS, "drop_unverified_quotes.py")],
            capture=True, step="quote_gate")
    after = quote_counts()

    total_before = sum(before.values())
    total_after = sum(after.values())
    dropped = total_before - total_after
    share = dropped / total_before if total_before else 0.0
    log()
    log(f"new talks' quotes: {total_before} extracted, {total_after} verbatim, "
        f"{dropped} dropped ({share*100:.2f}%)")
    if share > QUOTE_DROP_CEILING:
        detail = ", ".join(f"{s}: {before[s]}->{after.get(s, 0)}"
                           for s in sorted(before) if after.get(s, 0) != before[s])
        fail("quote_gate",
             f"{share*100:.1f}% of the new talks' quotes failed verbatim verification, above "
             f"the {QUOTE_DROP_CEILING*100:.0f}% ceiling. That rate is the transcript-corruption "
             "signature described in BUILD.md (caption word-gluing), not normal model behaviour. "
             f"Per talk: {detail}")

    total = 0
    for slug in passa_slugs():
        total += len(load_passa(slug)["passA"].get("notable_quotes") or [])
    REPORT["quotes_total"] = total
    log(f"corpus quotes after verification: {total}")


# ---------------------------------------------------------------------------
# 7. concepts
# ---------------------------------------------------------------------------

def build_raw_concepts():
    counter = collections.Counter()
    for slug in sorted(passa_slugs()):
        for raw in load_passa(slug)["passA"].get("concepts") or []:
            if isinstance(raw, str) and raw.strip():
                counter[raw.strip().lower()] += 1
    path = os.path.join(CONCEPTS, "raw_concepts.tsv")
    with open(path, "w") as handle:
        for string, count in counter.most_common():
            handle.write(f"{count}\t{string}\n")
    log(f"raw_concepts.tsv rebuilt: {len(counter)} distinct strings "
        f"from {len(passa_slugs())} Pass A files")
    return dict(counter)


def build_concept_talks(mapping, skip_slugs):
    out = {}
    for slug in sorted(passa_slugs()):
        if slug in skip_slugs:
            continue
        for raw in load_passa(slug)["passA"].get("concepts") or []:
            if not isinstance(raw, str):
                continue
            concept = mapping.get(raw.strip().lower())
            if not concept or concept == "DROP":
                continue
            out.setdefault(concept, [])
            if slug not in out[concept]:
                out[concept].append(slug)
    return out


def concepts_step():
    section("7. CONCEPTS -- vocabulary assignment and concept/talk rebuild")
    import run_passA
    import run_conceptsB

    with open(os.path.join(CONCEPTS, "concept_talks.json")) as handle:
        previous = json.load(handle)
    with open(os.path.join(CONCEPTS, "canonical.json")) as handle:
        vocab = json.load(handle)
    canonical_names = [c["concept"] for c in vocab["canonical"]]

    raw_counts = build_raw_concepts()

    with open(os.path.join(CONCEPTS, "mapping.json")) as handle:
        mapping = json.load(handle)["mapping"]
    todo = [s for s in raw_counts if s not in mapping]
    log(f"{len(raw_counts)} raw strings | {len(todo)} unmapped and needing assignment")

    if todo:
        os.makedirs(run_conceptsB.BATCHDIR, exist_ok=True)
        existing = [int(m.group(1)) for m in
                    (re.match(r"batch_(\d+)\.json$", fn)
                     for fn in os.listdir(run_conceptsB.BATCHDIR)) if m]
        start = (max(existing) + 1) if existing else 0
        batches = [todo[i:i + CONCEPT_BATCH_SIZE]
                   for i in range(0, len(todo), CONCEPT_BATCH_SIZE)]
        log(f"{len(batches)} new batch(es) starting at index {start} "
            "(existing batches are never renumbered or rewritten)")
        with ThreadPoolExecutor(max_workers=CONCEPT_CONCURRENCY) as pool:
            results = list(pool.map(
                lambda pair: run_conceptsB.run_batch(start + pair[0], vocab, pair[1], 900),
                enumerate(batches)))
        bad = [r for r in results if r[0] in ("fail", "timeout")]
        if bad:
            fail("concepts", f"{len(bad)} concept-assignment batch(es) failed: {bad}")

    merged = run_conceptsB.merge(vocab, raw_counts)
    stats = merged["stats"]
    if stats["unassigned"] or stats["invented_concepts"]:
        fail("concepts",
             f"concept mapping did not validate: {stats['unassigned']} unassigned, "
             f"{stats['invented_concepts']} invented concept(s). Both must be zero -- an "
             "invented concept means the model was allowed to extend a vocabulary that is "
             "fixed by design.")
    log(f"mapping validated: {stats['mapped']} mapped, {stats['dropped']} dropped, "
        "0 unassigned, 0 invented")

    current = build_concept_talks(merged["mapping"], run_passA.SKIP_SLUGS)

    vanished = [c for c in previous if c not in current]
    if vanished:
        fail("concepts", f"{len(vanished)} concept(s) lost every talk and disappeared from "
                         f"concept_talks.json: {vanished}. A canonical concept with no talks "
                         "cannot have a Pass C page, so this needs a human.")
    with open(os.path.join(CONCEPTS, "concept_talks.json"), "w") as handle:
        json.dump(current, handle, indent=2, ensure_ascii=False)

    changed = sorted(c for c in current
                     if set(current[c]) != set(previous.get(c, [])))
    REPORT["concepts_total"] = len(canonical_names)
    REPORT["concepts_regenerated"] = len(changed)
    log(f"concept_talks.json rebuilt: {len(current)} concepts, {len(changed)} with a "
        "changed talk set")
    for concept in changed:
        log(f"  changed: {concept} ({len(previous.get(concept, []))} -> {len(current[concept])} talks)")
    return changed, canonical_names


# ---------------------------------------------------------------------------
# 8. pass C
# ---------------------------------------------------------------------------

def pass_c(changed, canonical_names):
    section("8. PASS C -- cross-talk re-synthesis for concepts whose talk set moved")
    import run_passC

    if changed:
        stale = os.path.join(RAW, f"passC.stale-{time.strftime('%Y%m%d')}")
        os.makedirs(stale, exist_ok=True)
        moved = 0
        for concept in changed:
            src = os.path.join(PASSC, f"{run_passC.slugify(concept)}.json")
            if os.path.exists(src):
                shutil.move(src, os.path.join(stale, os.path.basename(src)))
                moved += 1
        log(f"moved {moved} superseded Pass C file(s) -> {os.path.relpath(stale, ROOT)}")

        runlog = os.path.join(PASSC, "_runlog.jsonl")
        start_line = count_lines(runlog)
        for attempt in range(1, PASS_ATTEMPTS + 1):
            missing = [c for c in changed if not run_passC.done(run_passC.slugify(c))]
            if not missing:
                break
            log(f"attempt {attempt}/{PASS_ATTEMPTS}: {len(missing)} concept(s) outstanding")
            run_cmd([sys.executable, os.path.join(SCRIPTS, "run_passC.py"),
                     "--concurrency", PASS_CONCURRENCY,
                     "--concepts", ",".join(missing)], step="passC", check=False)
        emit_usage(read_runlog_tail(runlog, start_line))

        missing = [c for c in changed if not run_passC.done(run_passC.slugify(c))]
        if missing:
            fail("passC", f"{len(missing)} concept(s) still have no valid Pass C output after "
                          f"{PASS_ATTEMPTS} attempts: {missing}")
    else:
        log("no concept's talk set changed; nothing to re-synthesize.")

    rc, out = run_cmd([sys.executable, os.path.join(SCRIPTS, "verify_passC_quotes.py")],
                      capture=True, check=False, step="passC_verify")
    checked = re.search(r"concepts checked:\s*(\d+)", out)
    verbatim = re.search(r"evidence_quotes verbatim:\s*(\d+)/(\d+)", out)
    if rc != 0:
        fail("passC_verify", "verify_passC_quotes.py reported unverifiable evidence quotes, "
                             "which is a possible fabrication. Nothing was pushed.")
    if not checked or int(checked.group(1)) != len(canonical_names):
        got = checked.group(1) if checked else "?"
        fail("passC_verify", f"Pass C covers {got} concepts but the canonical vocabulary has "
                             f"{len(canonical_names)}. Every canonical concept needs a synthesis.")
    if not verbatim or verbatim.group(1) != verbatim.group(2):
        fail("passC_verify", "Pass C evidence quotes are not 100% verbatim against Pass A.")
    log(f"Pass C gate: {checked.group(1)}/{len(canonical_names)} concepts, "
        f"{verbatim.group(1)}/{verbatim.group(2)} evidence quotes verbatim.")


# ---------------------------------------------------------------------------
# 9. rebuild
# ---------------------------------------------------------------------------

def rebuild():
    section("9. REBUILD -- speaker index, wiki, graph explorer")
    run_cmd([sys.executable, os.path.join(SCRIPTS, "build_speaker_index.py"),
             "--root", ROOT], capture=True, step="build_speaker_index")
    rc, out = run_cmd([sys.executable, os.path.join(SCRIPTS, "build_wiki.py"),
                       "--root", ROOT, "--verify"], capture=True, step="build_wiki")

    links = re.search(r"Link integrity:\s*(\d+) relative links checked,\s*(\d+) broken", out)
    if not links:
        fail("build_wiki", "build_wiki.py --verify printed no link-integrity line; the verify "
                           "report shape changed and this gate can no longer be trusted.")
    if int(links.group(2)) != 0:
        fail("build_wiki", f"{links.group(2)} broken relative link(s) in the rebuilt wiki.")

    counts = re.search(
        r"Page counts: talks=(\d+) concepts=(\d+) speakers=(\d+) "
        r"\(expected (\d+)/(\d+)/(\d+) from source data\)", out)
    if not counts:
        fail("build_wiki", "build_wiki.py --verify printed no page-count line.")
    got = counts.group(1, 2, 3)
    expected = counts.group(4, 5, 6)
    if got != expected:
        fail("build_wiki", f"page counts {got} do not match the source data {expected}.")
    if "MISMATCH" in out:
        fail("build_wiki", "the wiki's quote count does not reconcile with Pass A.")

    run_cmd([sys.executable, os.path.join(SCRIPTS, "build_graph_explorer.py"),
             "--root", ROOT], capture=True, step="build_graph_explorer")
    log(f"wiki verified: {links.group(1)} links, 0 broken; pages {got} match source data.")


# ---------------------------------------------------------------------------
# 10. count sync
# ---------------------------------------------------------------------------

def corpus_counts():
    talks = len(load_index())
    with open(os.path.join(CONCEPTS, "canonical.json")) as handle:
        concepts = len(json.load(handle)["canonical"])
    speakers = len(glob.glob(os.path.join(ROOT, "wiki", "speakers", "*.md")))
    quotes = sum(len(load_passa(s)["passA"].get("notable_quotes") or []) for s in passa_slugs())
    maturity = collections.Counter()
    for path in glob.glob(os.path.join(PASSC, "*.json")):
        if os.path.basename(path).startswith(("_", ".")):
            continue
        with open(path) as handle:
            maturity[(json.load(handle).get("passC") or {}).get("maturity")] += 1
    return {"talks": talks, "concepts": concepts, "speakers": speakers, "quotes": quotes,
            "maturity": maturity}


def sub_once(path, pattern, replacement, edits):
    """Anchored replacement that MUST fire exactly once. Loud beats silent."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    new_text, n = re.subn(pattern, replacement, text)
    if n != 1:
        fail("count_sync",
             f"pattern matched {n} time(s) in {os.path.relpath(path, REPO)} (expected exactly 1):\n"
             f"  {pattern}\nThe hand-maintained counts in that file have drifted from what this "
             "job knows how to update. Fix the file or the pattern by hand; the run stopped "
             "before committing anything.")
    if new_text != text:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(new_text)
        edits.append(os.path.relpath(path, REPO))


def count_sync(before, after):
    section("10. COUNT SYNC -- hand-maintained files that carry corpus numbers")

    settled = after["maturity"].get("settled", 0)
    REPORT["maturity"] = {k: v for k, v in after["maturity"].items() if k}
    log(f"maturity distribution: {dict(after['maturity'])}")
    if settled:
        fail("count_sync",
             f"{settled} concept(s) now come back as SETTLED practice. The repo's headline claim "
             "is 'zero settled', which is prose, not a count -- a cron must not reword it. "
             "Nothing was committed; a human needs to rewrite that claim.")

    def n(value):
        return re.escape(str(value))

    def c(value):
        return re.escape(f"{value:,}")

    bt, bc, bs, bq = before["talks"], before["concepts"], before["speakers"], before["quotes"]
    at, ac, asp, aq = after["talks"], after["concepts"], after["speakers"], after["quotes"]
    bm, am = before["maturity"], after["maturity"]
    bcons, bcont, bfront = bm.get("consolidating", 0), bm.get("contested", 0), bm.get("frontier", 0)
    acons, acont, afront = am.get("consolidating", 0), am.get("contested", 0), am.get("frontier", 0)

    root_readme = os.path.join(REPO, "README.md")
    event_readme = os.path.join(ROOT, "README.md")
    skill = os.path.join(REPO, "skills", "event-wiki", "SKILL.md")
    plugin = os.path.join(REPO, ".claude-plugin", "plugin.json")
    marketplace = os.path.join(REPO, ".claude-plugin", "marketplace.json")
    grader_dir = os.path.join(REPO, "evals", "metadata-lookup-corpus-size", "graders")
    correct_counts = os.path.join(grader_dir, "correct_counts.md")

    edits = []

    sub_once(root_readme,
             rf"{n(bt)} talks, {n(bc)} concepts, {n(bs)} speakers, almost a million words",
             f"{at} talks, {ac} concepts, {asp} speakers, almost a million words", edits)
    sub_once(root_readme,
             rf"Headline finding: of\n{n(bc)} concepts synthesized across those talks, zero came "
             rf"back settled practice \({n(bcons)}\nconsolidating, {n(bcont)} contested, "
             rf"{n(bfront)} frontier\)",
             f"Headline finding: of\n{ac} concepts synthesized across those talks, zero came "
             f"back settled practice ({acons}\nconsolidating, {acont} contested, "
             f"{afront} frontier)", edits)
    sub_once(root_readme,
             rf"{c(bq)} quotes checked character for character",
             f"{aq:,} quotes checked character for character", edits)

    sub_once(event_readme,
             rf"wiki built from {n(bt)} talks at the AI Engineer",
             f"wiki built from {at} talks at the AI Engineer", edits)
    sub_once(event_readme,
             rf"July 2, 2026\): {n(bc)} concepts, {n(bs)} speakers, and a",
             f"July 2, 2026): {ac} concepts, {asp} speakers, and a", edits)
    sub_once(event_readme,
             rf"This corpus covers the {n(bt)} that had been published",
             f"This corpus covers the {at} that had been published", edits)
    sub_once(event_readme,
             rf"of the {n(bc)} concepts synthesized across those {n(bt)} talks, zero are\n"
             rf"settled practice\. {n(bcons)} are consolidating, {n(bcont)} contested, "
             rf"{n(bfront)} frontier\.",
             f"of the {ac} concepts synthesized across those {at} talks, zero are\n"
             f"settled practice. {acons} are consolidating, {acont} contested, "
             f"{afront} frontier.", edits)

    sub_once(skill, rf"\(AIEWF 2026, {n(bt)} talks\)", f"(AIEWF 2026, {at} talks)", edits)
    sub_once(skill, rf"\) — {n(bt)}\npublished talks", f") — {at}\npublished talks", edits)
    sub_once(skill, rf"\({n(bt)} for aiewf-2026\.\)", f"({at} for aiewf-2026.)", edits)
    sub_once(skill, rf"\({n(bc)} for aiewf-2026\.\)", f"({ac} for aiewf-2026.)", edits)
    sub_once(skill, rf"\({n(bs)} for aiewf-2026\.\)", f"({asp} for aiewf-2026.)", edits)

    sub_once(plugin,
             rf"Currently indexed: AI Engineer World's Fair 2026 \({n(bt)} talks\)",
             f"Currently indexed: AI Engineer World's Fair 2026 ({at} talks)", edits)
    sub_once(marketplace,
             rf"currently AI Engineer World's Fair 2026 \({n(bt)} talks, {n(bc)} concepts, "
             rf"{n(bs)} speakers\)",
             f"currently AI Engineer World's Fair 2026 ({at} talks, {ac} concepts, "
             f"{asp} speakers)", edits)
    sub_once(marketplace,
             rf"Currently indexed: AI Engineer World's Fair 2026 \({n(bt)} talks, {n(bc)} "
             rf"concepts, {n(bs)} speakers\)",
             f"Currently indexed: AI Engineer World's Fair 2026 ({at} talks, {ac} "
             f"concepts, {asp} speakers)", edits)

    sub_once(correct_counts,
             rf"The corpus has {n(bt)} talks, {n(bc)} concepts, and {n(bs)} speakers",
             f"The corpus has {at} talks, {ac} concepts, and {asp} speakers", edits)

    # Patch version bump, applied identically to both manifests so they cannot drift.
    with open(plugin, encoding="utf-8") as handle:
        version = json.load(handle)["version"]
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        fail("count_sync", f"plugin.json version {version!r} is not major.minor.patch; "
                           "refusing to guess a bump.")
    new_version = f"{parts[0]}.{parts[1]}.{int(parts[2]) + 1}"
    for path in (plugin, marketplace):
        sub_once(path, rf'"version": "{n(version)}"', f'"version": "{new_version}"', edits)
    log(f"plugin version {version} -> {new_version}")

    # The regex grader is named for the number it asserts, so the count change renames
    # the file as well as its pattern.
    old_grader = os.path.join(grader_dir, f"mentions_{bt}.md")
    new_grader = os.path.join(grader_dir, f"mentions_{at}.md")
    if not os.path.exists(old_grader):
        fail("count_sync", f"expected the regex grader at {os.path.relpath(old_grader, REPO)}; "
                           "it is missing or already renamed.")
    sub_once(old_grader, rf'pattern: "{n(bt)}"', f'pattern: "{at}"', edits)
    if old_grader != new_grader:
        subprocess.run(["git", "-C", REPO, "mv", os.path.relpath(old_grader, REPO),
                        os.path.relpath(new_grader, REPO)], check=True, capture_output=True)
        edits.append(f"{os.path.relpath(old_grader, REPO)} -> {os.path.relpath(new_grader, REPO)}")

    # BUILD.md's counts sit inside dated narrative prose ("as of the 2026-08-19 refresh"),
    # which is not a mechanical edit. Named here so it is not silently forgotten.
    REPORT["docs_needing_human_update"] = ["events/aiewf-2026/BUILD.md"]

    log()
    for edit in edits:
        log(f"  updated {edit}")
    log(f"{len(edits)} count-bearing edit(s). BUILD.md carries dated prose and was left "
        "for a human.")


# ---------------------------------------------------------------------------
# 11. eval gate
# ---------------------------------------------------------------------------

def eval_gate():
    section("11. EVAL GATE -- the repo's own 10-case suite")
    rc, out = run_cmd([sys.executable, os.path.join(REPO, "evals", "run.py")],
                      cwd=REPO, capture=True, check=False, step="evals")

    failed = re.findall(r"^\[\d+/\d+\] (\S+) \.\.\. FAIL", out, re.M)
    summary = re.search(r"(\d+)/(\d+) passing", out)
    if not summary:
        fail("evals", "evals/run.py printed no pass summary; the harness did not complete.")
    passed, total = int(summary.group(1)), int(summary.group(2))
    log(f"first pass: {passed}/{total}")

    if failed:
        # One retry per failed case, for harness flakiness only. A case that fails twice
        # is a real regression and blocks the push.
        still_failing = []
        for case in failed:
            log(f"retrying {case} once (harness flakiness allowance)")
            rrc, rout = run_cmd([sys.executable, os.path.join(REPO, "evals", "run.py"),
                                 "--case", case], cwd=REPO, capture=True, check=False,
                                step="evals")
            if rrc != 0:
                still_failing.append(case)
        if still_failing:
            REPORT["evals"] = {"passed": passed, "total": total, "failed": still_failing}
            fail("evals", f"{len(still_failing)} eval case(s) failed twice: {still_failing}. "
                          "Nothing was committed or pushed.")
        passed = total

    REPORT["evals"] = {"passed": passed, "total": total, "failed": []}
    log(f"eval gate: {passed}/{total} passing.")


# ---------------------------------------------------------------------------
# 12. commit + push
# ---------------------------------------------------------------------------

def commit_and_push(new_records, before, after, no_push):
    section("12. COMMIT" + ("" if no_push else " + PUSH"))

    # Staged by explicit path rather than a blanket `add -A`, for two reasons.
    #
    # feed.xml and add_episode.py belong to the podcast pipeline and are out of this
    # job's remit; they are excluded rather than assumed clean, because they are
    # routinely dirty in this working tree.
    #
    # And this repo is worked on by hand between runs -- on 2026-08-19 it already held
    # two unrelated untracked event directories. A 2:15 AM `add -A` would have swept
    # someone's half-finished work into a public push. These four paths are exactly
    # what the refresh writes, so the narrower spec is also the complete one.
    pathspec = [
        "events/aiewf-2026", "README.md", ".claude-plugin", "skills", "evals",
        ":(exclude)feed.xml", ":(exclude,glob)**/add_episode.py",
    ]
    run_cmd(["git", "-C", REPO, "add", "-A", "--"] + pathspec,
            cwd=REPO, capture=True, step="commit")

    rc, staged = run_cmd(["git", "-C", REPO, "diff", "--cached", "--name-only"],
                         cwd=REPO, capture=True, check=False, step="commit")
    if not staged.strip():
        log("nothing staged; skipping the commit.")
        return

    lines = [f"AIEWF 2026 corpus refresh: {len(new_records)} newly published "
             f"talk{'s' if len(new_records) != 1 else ''} "
             f"({before['talks']} -> {after['talks']})", ""]
    for rec in new_records:
        speakers = ", ".join(rec.get("speakers") or []) or "unattributed"
        org = rec.get("org") or "unknown org"
        track = rec.get("track") or "no track"
        lines.append(f"- {rec['title']} — {speakers}, {org} [{track}]")
    lines += [
        "",
        f"Concepts: {after['concepts']} canonical, {REPORT['concepts_regenerated']} "
        "re-synthesized in Pass C.",
        f"Quotes: {after['quotes']:,} verbatim-verified. Speakers: {after['speakers']}.",
        f"Eval suite: {REPORT['evals']['passed']}/{REPORT['evals']['total']} passing.",
        "",
        "Generated by scripts/refresh_corpus.py (aiewf-corpus-refresh cron).",
        "",
        "Co-Authored-By: Claude Opus <noreply@anthropic.com>",
    ]
    message = "\n".join(lines)

    run_cmd(["git", "-C", REPO, "commit", "-m", message], cwd=REPO, capture=True, step="commit")
    REPORT["committed"] = True
    rc, sha = run_cmd(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                      cwd=REPO, capture=True, step="commit")
    log(f"committed {sha.strip()}")

    if no_push:
        log("--no-push: leaving the commit local.")
        return
    run_cmd(["git", "-C", REPO, "push", "origin", "main"], cwd=REPO, capture=True, step="push")
    REPORT["pushed"] = True
    log("pushed to origin/main.")


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def final_report(new_records, before, after):
    section("RUN REPORT")
    log(f"New talks: {len(new_records)}")
    for rec in new_records:
        speakers = ", ".join(rec.get("speakers") or []) or "unattributed"
        log(f"  {rec['title']} — {speakers}, {rec.get('org') or 'unknown org'} "
            f"({rec.get('track') or 'no track'})")
        log(f"    {rec.get('url')}")
    log()
    log(f"Corpus:   talks {before['talks']} -> {after['talks']} | "
        f"concepts {before['concepts']} -> {after['concepts']} | "
        f"speakers {before['speakers']} -> {after['speakers']} | "
        f"quotes {before['quotes']:,} -> {after['quotes']:,}")
    log(f"Maturity: {dict(after['maturity'])} (settled must stay 0)")
    log(f"Concepts re-synthesized in Pass C: {REPORT['concepts_regenerated']}")
    log(f"Still private on the official playlists: {REPORT['still_private']}")
    if REPORT["deduped_video_ids"]:
        log(f"Re-uploads deduplicated by slug: {REPORT['deduped_video_ids']}")
    if REPORT["no_caption_video_ids"]:
        log(f"Awaiting English captions (retried next run): {REPORT['no_caption_video_ids']}")
    log(f"Track-only candidates: {REPORT['track_only_total']} eligible overall, "
        f"{len(REPORT['track_only_candidates'])} newly surfaced for human review")
    for row in REPORT["track_only_candidates"]:
        log(f"  {row['video_id']} {row['upload_date']} {row['title']}")
    log(f"Evals: {REPORT['evals']['passed']}/{REPORT['evals']['total']} passing")
    log(f"Committed: {REPORT['committed']} | Pushed: {REPORT['pushed']}")
    log(f"Left for a human: {REPORT['docs_needing_human_update']}")


# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-push", action="store_true",
                        help="commit locally but do not push to origin")
    parser.add_argument("--dry-run", action="store_true",
                        help="discovery and triage only; ingest nothing, touch no data/")
    args = parser.parse_args()

    sys.path.insert(0, SCRIPTS)
    REPORT["dry_run"] = args.dry_run
    started = time.time()

    log(f"AIEWF 2026 corpus refresh — {time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    log(f"project root: {ROOT}")
    log(f"repo root:    {REPO}")
    log(f"mode: {'DRY RUN' if args.dry_run else ('no-push' if args.no_push else 'full')}")

    before = corpus_counts()
    REPORT["talks_before"] = before["talks"]

    _, vid2pl, _main_names, main_candidates, track_only = discover()
    accepted = triage(vid2pl, main_candidates, track_only)

    if args.dry_run:
        section("DRY RUN COMPLETE")
        log(f"{len(accepted)} talk(s) would be ingested; nothing under data/ was touched.")
        for row in accepted:
            log(f"  {row['video_id']} {row['upload_date']} {row['title']}")
        REPORT["new_talks"] = len(accepted)
        REPORT["talks_after"] = before["talks"]
        finish("ok", message=f"dry run: {len(accepted)} candidate(s) ready to ingest")

    if not accepted:
        section("NO-OP -- nothing new published this week")
        log(f"corpus unchanged at {before['talks']} talks.")
        log(f"still private on the official playlists: {REPORT['still_private']}")
        log(f"track-only eligible overall:             {REPORT['track_only_total']} "
            f"({len(REPORT['track_only_candidates'])} new this run)")
        REPORT["talks_after"] = before["talks"]
        finish("ok", message="no new talks; data/ untouched")

    snapshot = {rec["video_id"]: {"slug": rec["slug"], "word_count": rec["word_count"]}
                for rec in load_index()}

    harvested = harvest(accepted)
    if not harvested:
        section("NO-OP -- candidates found but none have English captions yet")
        log(f"{len(accepted)} candidate(s) will be retried next run.")
        REPORT["talks_after"] = before["talks"]
        finish("ok", message="candidates await captions; data/ untouched")

    new_records = normalize_and_enrich(snapshot, harvested)
    REPORT["new_talks"] = len(new_records)
    REPORT["new_talk_details"] = [
        {"title": r["title"], "speakers": r.get("speakers") or [], "org": r.get("org") or "",
         "track": r.get("track") or "", "url": r.get("url", "")} for r in new_records]

    pass_a()
    quote_gate([r["slug"] for r in new_records])
    changed, canonical_names = concepts_step()
    pass_c(changed, canonical_names)
    rebuild()

    after = corpus_counts()
    REPORT["talks_after"] = after["talks"]
    count_sync(before, after)
    eval_gate()
    commit_and_push(new_records, before, after, args.no_push)
    final_report(new_records, before, after)

    log()
    log(f"Total wall clock: {(time.time() - started) / 60:.1f} min")
    finish("ok", message=f"{len(new_records)} new talk(s) ingested")


if __name__ == "__main__":
    main()
