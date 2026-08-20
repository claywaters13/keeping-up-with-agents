#!/usr/bin/env python3
"""Weekly incremental refresh of the YC Startup School 2026 corpus.

The port of `events/aiewf-2026/scripts/refresh_corpus.py` that BUILD.md's known
limitation #2 asks for. Same shape, same contract: twelve steps, each a hard gate,
exit code is the whole story, and "nothing new was published" is a SUCCESS that
leaves the working tree untouched.

    python3 scripts/refresh_corpus.py --dry-run     # discovery + triage only
    python3 scripts/refresh_corpus.py --no-push     # full run, commit but no push
    python3 scripts/refresh_corpus.py               # full run

WHAT DIFFERS FROM THE AIEWF ORCHESTRATOR, and why:

  * DISCOVERY IS ONE PLAYLIST, NOT A CHANNEL SWEEP. Startup School is single-track
    with one official playlist, so there is no cross-year topical playlist to mine,
    no track-only candidate class, and no human-approval file. Membership in
    PLEb7ftOB0yf0 *is* the provenance gate. That removes the entire contamination
    surface the AIEWF version spends most of its triage on.

  * NO SCHEDULE JOIN, NO PLAYLIST TRACKS. YC publishes no schedule feed and the
    event has no tracks, so `normalize.py` is the whole enrichment step. There is
    correspondingly no "re-run the enrichment or silently lose track/org" trap.

  * THE VOCABULARY IS FROZEN AT 36 AND THIS JOB MAY NEVER EXTEND IT. Unmapped
    concept strings are assigned against the existing canonical list, DROP included.
    Minting a canonical concept is a judgment about what the corpus is *about*, and
    an unattended weekly job is the wrong place for it. So instead of inventing, the
    run REPORTS: any string that got DROPped while appearing in 3+ talks is surfaced
    as "possible new concept, needs human review". That keeps the failure mode
    visible rather than silent, without letting a cron reshape the vocabulary.

  * PASS C ONLY COVERS CONCEPTS WITH 3+ TALKS (18 of 36 today), matching how the
    corpus was built. The verify gate therefore checks against that computed
    expectation rather than against the full canonical count.

Model access is subscription-only, through the event's own run_passA.py /
run_conceptsB.py / run_passC.py, all of which shell out to headless `claude -p`.
No Anthropic API key is used, required, or passed to any child.
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
PLAYLIST_MEMBERS = os.path.join(RAW, "playlist_members.json")
VIDEO_IDS = os.path.join(RAW, "video_ids.txt")
KNOWN_REUPLOADS = os.path.join(RAW, "known_reuploads.json")

YTDLP_ENV = "/tmp/ytdlp-env"
YTDLP = os.path.join(YTDLP_ENV, "bin", "yt-dlp")

PLAYLIST_ID = "PLEb7ftOB0yf0"
PLAYLIST_TITLE = "Startup School 2026"
PLAYLIST_URL = f"https://www.youtube.com/playlist?list={PLAYLIST_ID}"
CHANNEL = "Y Combinator"
CHANNEL_URL = "https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg"

LIVESTREAM_RE = re.compile(r"livestream|full day|day [12].*(track|stage)", re.I)
LIVESTREAM_MAX_SEC = 4 * 3600
# Startup School talks run 8 minutes to an hour; the longest in the build is 57
# minutes. Anything under two minutes is a trailer or a clip, not a session.
MIN_TALK_SEC = 120

QUOTE_DROP_CEILING = 0.05
PASS_ATTEMPTS = 3
CONCEPT_BATCH_SIZE = 100
CONCEPT_CONCURRENCY = 2
PASS_CONCURRENCY = "2"
# A concept needs this many tagged talks before Pass C synthesizes it, matching how
# the corpus was built (18 of 36 concepts cleared it).
PASSC_MIN_TALKS = 3
# A dropped concept string appearing in this many talks is a candidate for the
# canonical vocabulary and gets escalated to a human instead of vanishing.
NEW_CONCEPT_MIN_TALKS = 3

COMMIT_PATHSPEC = [
    "events/yc-startup-school-2026", "README.md", ".claude-plugin", "skills", "evals",
    ":(exclude)feed.xml", ":(exclude,glob)**/add_episode.py",
]

REPORT = {
    "event": "yc-startup-school-2026",
    "status": "failed",
    "dry_run": False,
    "failed_step": None,
    "message": "",
    "new_talks": 0,
    "new_talk_details": [],
    "deduped_video_ids": [],
    "reuploads_skipped": [],
    "reuploads_detected": [],
    "no_caption_video_ids": [],
    "talks_before": None,
    "talks_after": None,
    "concepts_total": None,
    "concepts_regenerated": 0,
    "concepts_synthesized": None,
    "quotes_total": None,
    "still_private": 0,
    "possible_new_concepts": [],
    "maturity": {},
    "evals": None,
    "committed": False,
    "pushed": False,
    "docs_needing_human_update": [],
}


# ---------------------------------------------------------------------------
# plumbing (kept deliberately identical to the AIEWF orchestrator)
# ---------------------------------------------------------------------------

def log(msg=""):
    print(msg, flush=True)


def section(title):
    log()
    log("=" * 78)
    log(title)
    log("=" * 78)


def finish(status, step=None, message=""):
    REPORT["status"] = status
    REPORT["failed_step"] = step
    REPORT["message"] = message
    if status != "ok":
        log()
        log(f"FAILED at {step}: {message}")
    log()
    log("YC_REFRESH_RESULT=" + json.dumps(REPORT, ensure_ascii=False, sort_keys=True))
    sys.exit(0 if status == "ok" else 1)


def fail(step, message):
    finish("failed", step, message)


def child_env():
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
    return env


def run_cmd(args, cwd=ROOT, capture=False, timeout=None, check=True, step=None):
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


def ensure_ytdlp():
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
        probe = subprocess.run([YTDLP, "--version"], capture_output=True, text=True, timeout=60)
        if probe.returncode != 0:
            raise RuntimeError(probe.stderr.strip())
    except Exception as exc:
        fail("ytdlp", f"could not create a working yt-dlp venv at {YTDLP_ENV}: {exc}")
    log(f"yt-dlp {probe.stdout.strip()} installed.")


def emit_usage(rows):
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


def load_known_reuploads():
    if os.path.exists(KNOWN_REUPLOADS):
        try:
            with open(KNOWN_REUPLOADS) as handle:
                data = json.load(handle)
            if isinstance(data, dict):
                return data
        except ValueError:
            log(f"WARN {os.path.relpath(KNOWN_REUPLOADS, ROOT)} is unreadable; treating it "
                "as empty, which costs one wasted ingest attempt, not correctness")
    return {}


def save_known_reuploads(data):
    tmp = KNOWN_REUPLOADS + ".tmp"
    with open(tmp, "w") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False, sort_keys=True)
    os.replace(tmp, KNOWN_REUPLOADS)


def resolve_absorbing_talk(video_id):
    info_path = os.path.join(CAPS, f"{video_id}.info.json")
    raw_title = ""
    if os.path.exists(info_path):
        try:
            with open(info_path) as handle:
                raw_title = json.load(handle).get("title") or ""
        except ValueError:
            raw_title = ""

    def norm(value):
        return " ".join((value or "").lower().split())

    if raw_title:
        for rec in load_index():
            if norm(rec.get("raw_title")) == norm(raw_title):
                return rec["slug"], rec["video_id"], raw_title
    return None, None, raw_title


def restore_tracked_paths(why):
    """Revert this event's own tracked paths to HEAD, and nothing else."""
    log(f"restoring tracked paths to HEAD ({why})")
    rc, listing = run_cmd(["git", "-c", "core.quotepath=false", "-C", REPO,
                           "status", "--porcelain", "--"] + COMMIT_PATHSPEC,
                          cwd=REPO, capture=True, check=False, step="restore")
    modified = []
    for line in listing.splitlines():
        if not line.strip() or line.startswith("??"):
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        modified.append(path.strip().strip('"'))
    if modified:
        run_cmd(["git", "-C", REPO, "checkout", "HEAD", "--"] + modified,
                cwd=REPO, capture=True, step="restore")
        for path in modified:
            log(f"  reverted {path}")
    else:
        log("  nothing to revert.")
    rc, dirty = run_cmd(["git", "-c", "core.quotepath=false", "-C", REPO,
                         "status", "--porcelain", "--"] + COMMIT_PATHSPEC,
                        cwd=REPO, capture=True, check=False, step="restore")
    if dirty.strip():
        log("NOTE: these paths are still not clean after the restore. Nothing was "
            "deleted; a human should look:")
        for line in dirty.strip().splitlines():
            log(f"  {line}")
    else:
        log("tracked paths are clean again.")


# ---------------------------------------------------------------------------
# 1. discovery
# ---------------------------------------------------------------------------

def discover():
    section("1. DISCOVERY -- re-fetch the official Startup School playlist")
    ensure_ytdlp()

    try:
        proc = subprocess.run([YTDLP, "--flat-playlist", "--print",
                               "%(id)s|%(title)s", PLAYLIST_URL],
                              capture_output=True, text=True, timeout=300, env=child_env())
    except subprocess.TimeoutExpired:
        fail("discovery", f"timed out listing {PLAYLIST_URL}")
    members = []
    for line in proc.stdout.splitlines():
        if "|" in line:
            vid, title = line.split("|", 1)
            members.append({"video_id": vid.strip(), "title": title.strip()})
    if proc.returncode != 0 or not members:
        fail("discovery", f"could not list {PLAYLIST_URL} (rc={proc.returncode}); "
                          "the previous playlist_members.json was left untouched")
    log(f"{len(members)} videos on the playlist")

    # Same integrity gate as the AIEWF version: a partial or shape-changed fetch
    # written over the manifest would read downstream as "YC deleted a bunch of
    # talks". One playlist means one number to check.
    known = {rec["video_id"] for rec in load_index()}
    seen = {m["video_id"] for m in members}
    covered = len(known & seen) / len(known) if known else 1.0
    log(f"coverage of the existing corpus by the fresh fetch: {covered*100:.1f}%")
    if covered < 0.95:
        fail("discovery", f"the fresh playlist fetch only accounts for {covered*100:.1f}% of the "
                          f"{len(known)} talks already in the corpus, which reads as a partial or "
                          "malformed fetch; refusing to overwrite raw/playlist_members.json")

    if os.path.exists(PLAYLIST_MEMBERS):
        backup = f"{PLAYLIST_MEMBERS}.bak-{time.strftime('%Y%m%d')}"
        shutil.copy2(PLAYLIST_MEMBERS, backup)
        log(f"previous manifest backed up -> {os.path.relpath(backup, ROOT)}")
    manifest = {
        "playlist_id": PLAYLIST_ID, "playlist_title": PLAYLIST_TITLE,
        "playlist_url": PLAYLIST_URL, "channel": CHANNEL, "channel_url": CHANNEL_URL,
        "fetched_at": time.strftime("%Y-%m-%d"), "video_count": len(members),
        "videos": members,
    }
    with open(PLAYLIST_MEMBERS, "w") as handle:
        json.dump(manifest, handle, indent=2, ensure_ascii=False)
    log(f"wrote {os.path.relpath(PLAYLIST_MEMBERS, ROOT)} ({len(members)} videos)")

    candidates = [m["video_id"] for m in members if m["video_id"] not in known]
    log(f"already in the corpus: {len(known)}")
    log(f"candidates:            {len(candidates)}")
    return candidates


# ---------------------------------------------------------------------------
# 2. triage
# ---------------------------------------------------------------------------

def fetch_meta(video_ids, batch_size=40):
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


def triage(candidates):
    section("2. TRIAGE -- provenance and shape gates on every candidate")
    accepted, private, rejected, malformed = [], [], [], []

    known_reuploads = load_known_reuploads()
    skipped = [v for v in candidates if v in known_reuploads]
    candidates = [v for v in candidates if v not in known_reuploads]
    REPORT["reuploads_skipped"] = skipped
    for vid in skipped:
        entry = known_reuploads[vid]
        log(f"  {vid} KNOWN RE-UPLOAD, skipped -- absorbed into "
            f"{entry.get('absorbed_into_slug') or 'an existing talk'}"
            f" ({entry.get('existing_video_id') or 'video id unresolved'}), "
            f"detected {entry.get('detected', 'unknown')}")

    log(f"fetching metadata for {len(candidates)} candidate(s)")
    meta = fetch_meta(candidates)
    for vid in candidates:
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
        seconds = int(duration) if duration.isdigit() else 0
        if LIVESTREAM_RE.search(title) or seconds > LIVESTREAM_MAX_SEC:
            malformed.append(vid)
            log(f"  {vid} REJECT livestream/compilation: {title}")
            continue
        if seconds < MIN_TALK_SEC:
            # Playlist membership is the only provenance signal this event has, so a
            # trailer or clip added to the playlist would otherwise sail through.
            malformed.append(vid)
            log(f"  {vid} REJECT too short to be a session ({seconds}s): {title}")
            continue
        accepted.append({"video_id": vid, "upload_date": upload_date,
                         "duration": duration, "title": title})
        log(f"  {vid} ACCEPT {upload_date} {seconds}s: {title}")

    REPORT["still_private"] = len(private)
    log()
    log(f"accepted for ingestion: {len(accepted)}")
    log(f"known re-uploads skipped: {len(skipped)}")
    log(f"still private/unavailable: {len(private)}")
    log(f"rejected (pre-2026): {len(rejected)}")
    log(f"rejected (not a session): {len(malformed)}")
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
# 4. normalize
# ---------------------------------------------------------------------------

def noop_all_reuploads(before):
    section("NO-OP -- every candidate was a re-upload of an existing talk")
    restore_tracked_paths("no new talks after slug dedup")
    log(f"corpus unchanged at {before['talks']} talks.")
    log(f"re-uploads recorded for future runs: {REPORT['reuploads_detected']}")
    REPORT["talks_after"] = before["talks"]
    finish("ok", message="all accepted candidates were re-uploads; data/ restored")


def normalize_step(snapshot, harvested):
    section("4. NORMALIZE")
    # normalize.py is the whole enrichment step for this event: no schedule join and
    # no playlist_tracks pass, because Startup School is single-track and YC ships no
    # schedule feed. That also means no "re-run the enrichment or silently lose the
    # track" trap to guard against here.
    run_cmd([sys.executable, os.path.join(SCRIPTS, "normalize.py")], step="normalize")

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
    deduped = [r["video_id"] for r in harvested if r["video_id"] not in after]
    REPORT["deduped_video_ids"] = deduped
    if deduped:
        known = load_known_reuploads()
        detected = time.strftime("%Y-%m-%d")
        for vid in deduped:
            slug, existing_vid, raw_title = resolve_absorbing_talk(vid)
            known[vid] = {"absorbed_into_slug": slug, "existing_video_id": existing_vid,
                          "raw_title": raw_title, "detected": detected}
            log(f"recorded re-upload {vid} -> {slug or 'UNRESOLVED'} "
                f"({existing_vid or 'video id unresolved'})")
        save_known_reuploads(known)
        REPORT["reuploads_detected"] = deduped

    log()
    log(f"pre-existing talks unchanged: {len(snapshot)}")
    log(f"new talks in index.json:      {len(new_ids)}")
    return [after[v] for v in new_ids]


# ---------------------------------------------------------------------------
# 5-6. pass A + quote gate
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
    log(f"Pass A complete for all {len(wanted)} talks.")


def quote_gate(new_slugs):
    section("6. QUOTE GATE -- deterministic verbatim verification")

    def quote_counts():
        return {slug: len(load_passa(slug)["passA"].get("notable_quotes") or [])
                for slug in new_slugs if os.path.exists(os.path.join(PASSA, f"{slug}.json"))}

    before = quote_counts()
    run_cmd([sys.executable, os.path.join(SCRIPTS, "drop_unverified_quotes.py")],
            capture=True, step="quote_gate")
    after = quote_counts()

    total_before, total_after = sum(before.values()), sum(after.values())
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
             "signature described in events/aiewf-2026/BUILD.md (caption word-gluing), not "
             f"normal model behaviour. Per talk: {detail}")

    total = sum(len(load_passa(s)["passA"].get("notable_quotes") or []) for s in passa_slugs())
    REPORT["quotes_total"] = total
    log(f"corpus quotes after verification: {total}")


# ---------------------------------------------------------------------------
# 7. concepts
# ---------------------------------------------------------------------------

def build_raw_concepts():
    counter = collections.Counter()
    for slug in sorted(passa_slugs()):
        for raw in set(load_passa(slug)["passA"].get("concepts") or []):
            if isinstance(raw, str) and raw.strip():
                counter[raw.strip()] += 1
    path = os.path.join(CONCEPTS, "raw_concepts.tsv")
    with open(path, "w") as handle:
        for string, count in counter.most_common():
            handle.write(f"{count}\t{string}\n")
    log(f"raw_concepts.tsv rebuilt: {len(counter)} distinct strings "
        f"from {len(passa_slugs())} Pass A files")
    return dict(counter)


def concepts_step():
    section("7. CONCEPTS -- assignment against the FROZEN vocabulary")
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
    log(f"vocabulary is FROZEN at {len(canonical_names)} concepts; this job assigns into "
        "it or DROPs, and never extends it")

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
             "invented concept means the model was allowed to extend a vocabulary this "
             "job is not permitted to change.")
    log(f"mapping validated: {stats['mapped']} mapped, {stats['dropped']} dropped, "
        "0 unassigned, 0 invented")

    # The escape valve for a frozen vocabulary. A string this job DROPped that shows
    # up across several talks is exactly what a new canonical concept looks like
    # before anyone has named it -- so it gets escalated rather than silently binned.
    # This is the one place where "the cron did the safe thing" could still be the
    # wrong thing, so it must be loud in the report and the email.
    newly = [s for s in todo if merged["mapping"].get(s) == "DROP"
             and raw_counts.get(s, 0) >= NEW_CONCEPT_MIN_TALKS]
    REPORT["possible_new_concepts"] = [{"raw": s, "talks": raw_counts[s]}
                                       for s in sorted(newly, key=lambda x: -raw_counts[x])]
    if newly:
        log()
        log(f"POSSIBLE NEW CONCEPTS ({len(newly)}) -- dropped by the frozen vocabulary but "
            f"appearing in {NEW_CONCEPT_MIN_TALKS}+ talks. A human should decide whether the "
            "canonical list should grow:")
        for row in REPORT["possible_new_concepts"]:
            log(f"  {row['talks']} talks: {row['raw']!r}")

    rc, _ = run_cmd([sys.executable, os.path.join(SCRIPTS, "build_concept_talks.py")],
                    capture=True, check=False, step="concepts")
    if rc != 0:
        fail("concepts", "build_concept_talks.py reported unmapped concept strings, so the "
                         "concept/talk map is incomplete.")

    with open(os.path.join(CONCEPTS, "concept_talks.json")) as handle:
        current = json.load(handle)
    changed = sorted(c for c in current if set(current[c]) != set(previous.get(c, [])))
    REPORT["concepts_total"] = len(canonical_names)
    REPORT["concepts_regenerated"] = 0
    log(f"concept_talks.json rebuilt: {len(current)} concepts with >=1 talk, "
        f"{len(changed)} with a changed talk set")
    return changed, current, canonical_names


# ---------------------------------------------------------------------------
# 8. pass C
# ---------------------------------------------------------------------------

def pass_c(changed, concept_talks):
    section("8. PASS C -- cross-talk re-synthesis for concepts whose talk set moved")
    import run_passC

    # Only concepts with enough talks get a synthesis at all, matching how the corpus
    # was built. Anything thinner ships as definition + talk list, and its page says so.
    eligible = {c for c, talks in concept_talks.items() if len(talks) >= PASSC_MIN_TALKS}
    regen = [c for c in changed if c in eligible]
    log(f"{len(eligible)} concept(s) meet the {PASSC_MIN_TALKS}-talk synthesis threshold; "
        f"{len(regen)} of the {len(changed)} changed concept(s) need re-synthesis")
    REPORT["concepts_regenerated"] = len(regen)

    if regen:
        stale = os.path.join(RAW, f"passC.stale-{time.strftime('%Y%m%d')}")
        os.makedirs(stale, exist_ok=True)
        moved = 0
        for concept in regen:
            src = os.path.join(PASSC, f"{run_passC.slugify(concept)}.json")
            if os.path.exists(src):
                shutil.move(src, os.path.join(stale, os.path.basename(src)))
                moved += 1
        log(f"moved {moved} superseded Pass C file(s) -> {os.path.relpath(stale, ROOT)}")

        runlog = os.path.join(PASSC, "_runlog.jsonl")
        start_line = count_lines(runlog)
        for attempt in range(1, PASS_ATTEMPTS + 1):
            missing = [c for c in regen if not run_passC.done(run_passC.slugify(c))]
            if not missing:
                break
            log(f"attempt {attempt}/{PASS_ATTEMPTS}: {len(missing)} concept(s) outstanding")
            run_cmd([sys.executable, os.path.join(SCRIPTS, "run_passC.py"),
                     "--concurrency", PASS_CONCURRENCY,
                     "--min-talks", str(PASSC_MIN_TALKS),
                     "--concepts", ",".join(missing)], step="passC", check=False)
        emit_usage(read_runlog_tail(runlog, start_line))

        missing = [c for c in regen if not run_passC.done(run_passC.slugify(c))]
        if missing:
            fail("passC", f"{len(missing)} concept(s) still have no valid Pass C output after "
                          f"{PASS_ATTEMPTS} attempts: {missing}")
    else:
        log("no synthesized concept's talk set changed; nothing to re-synthesize.")

    rc, out = run_cmd([sys.executable, os.path.join(SCRIPTS, "verify_passC_quotes.py")],
                      capture=True, check=False, step="passC_verify")
    checked = re.search(r"concepts checked:\s*(\d+)", out)
    verbatim = re.search(r"evidence_quotes verbatim:\s*(\d+)/(\d+)", out)
    if rc != 0:
        fail("passC_verify", "verify_passC_quotes.py reported unverifiable evidence quotes, "
                             "which is a possible fabrication. Nothing was pushed.")
    if not checked or int(checked.group(1)) != len(eligible):
        got = checked.group(1) if checked else "?"
        fail("passC_verify", f"Pass C covers {got} concepts but {len(eligible)} meet the "
                             f"{PASSC_MIN_TALKS}-talk threshold. Every eligible concept needs a "
                             "synthesis, and no ineligible one should have a stale file.")
    if not verbatim or verbatim.group(1) != verbatim.group(2):
        fail("passC_verify", "Pass C evidence quotes are not 100% verbatim against Pass A.")
    REPORT["concepts_synthesized"] = len(eligible)
    log(f"Pass C gate: {checked.group(1)}/{len(eligible)} eligible concepts, "
        f"{verbatim.group(1)}/{verbatim.group(2)} evidence quotes verbatim.")


# ---------------------------------------------------------------------------
# 9. rebuild
# ---------------------------------------------------------------------------

def rebuild():
    section("9. REBUILD -- speaker index and wiki")
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
    got, expected = counts.group(1, 2, 3), counts.group(4, 5, 6)
    if got != expected:
        fail("build_wiki", f"page counts {got} do not match the source data {expected}.")
    if "MISMATCH" in out:
        fail("build_wiki", "the wiki's quote count does not reconcile with Pass A.")
    log(f"wiki verified: {links.group(1)} links, 0 broken; pages {got} match source data.")


# ---------------------------------------------------------------------------
# 10. count sync
# ---------------------------------------------------------------------------

def corpus_counts():
    index = load_index()
    with open(os.path.join(CONCEPTS, "canonical.json")) as handle:
        concepts = len(json.load(handle)["canonical"])
    speakers = len(glob.glob(os.path.join(ROOT, "wiki", "speakers", "*.md")))
    quotes = sum(len(load_passa(s)["passA"].get("notable_quotes") or []) for s in passa_slugs())
    synthesized = len([f for f in glob.glob(os.path.join(PASSC, "*.json"))
                       if not os.path.basename(f).startswith(("_", "."))])
    maturity = collections.Counter()
    for path in glob.glob(os.path.join(PASSC, "*.json")):
        if os.path.basename(path).startswith(("_", ".")):
            continue
        with open(path) as handle:
            maturity[(json.load(handle).get("passC") or {}).get("maturity")] += 1
    return {"talks": len(index), "concepts": concepts, "speakers": speakers,
            "quotes": quotes, "synthesized": synthesized, "maturity": maturity,
            "words": sum(r.get("word_count") or 0 for r in index),
            "hours": sum(r.get("duration_sec") or 0 for r in index) / 3600}


def sub_once(path, pattern, replacement, edits):
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


def sub_once_fn(path, pattern, repl_fn, edits):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    new_text, n = re.subn(pattern, repl_fn, text)
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
    REPORT["maturity"] = {k: v for k, v in after["maturity"].items() if k}
    log(f"maturity distribution: {dict(after['maturity'])}")
    if after["maturity"].get("settled", 0):
        fail("count_sync",
             f"{after['maturity']['settled']} concept(s) now come back as SETTLED practice. "
             "Both this event's README and the repo root state zero settled, which is prose, "
             "not a count -- a cron must not reword it. Nothing was committed.")

    def n(value):
        return re.escape(str(value))

    bt, bc, bs = before["talks"], before["concepts"], before["speakers"]
    at, ac, asp = after["talks"], after["concepts"], after["speakers"]
    bq, aq, bsy, asy = before["quotes"], after["quotes"], before["synthesized"], after["synthesized"]

    root_readme = os.path.join(REPO, "README.md")
    event_readme = os.path.join(ROOT, "README.md")
    skill = os.path.join(REPO, "skills", "event-wiki", "SKILL.md")
    plugin = os.path.join(REPO, ".claude-plugin", "plugin.json")
    marketplace = os.path.join(REPO, ".claude-plugin", "marketplace.json")
    grader_dir = os.path.join(REPO, "evals", "yc-metadata-lookup-corpus-size", "graders")
    edits = []

    # Root README, YC section. Anchors stop inside the YC paragraph on purpose: the
    # AIEWF numbers live above it and are another job's business.
    sub_once(root_readme, rf"{n(bt)} talks and firesides",
             f"{at} talks and firesides", edits)
    sub_once(root_readme,
             rf"distilled into {n(bc)}\nconcepts and {n(bq)} verified quotes",
             f"distilled into {ac}\nconcepts and {aq} verified quotes", edits)

    quote_delta = aq - bq

    def bump_combined_quotes(match):
        current = int(match.group(1).replace(",", ""))
        return f"{current + quote_delta:,} quotes{match.group(2)}checked character for"

    sub_once_fn(root_readme, r"([\d,]+) quotes([^.]{0,40}?)checked character for",
                bump_combined_quotes, edits)

    # SKILL.md: every anchor ends at the YC number so the AIEWF ones are untouchable.
    sub_once(skill, rf"and Y Combinator Startup School 2026 \({n(bt)} talks\)",
             f"and Y Combinator Startup School 2026 ({at} talks)", edits)
    sub_once(skill, rf"\) — {n(bt)} published\n  talks and firesides",
             f") — {at} published\n  talks and firesides", edits)
    # Talks and speakers are BOTH 14 for this event, so these two lines are
    # indistinguishable on the number alone. Each is anchored on the sentence that
    # precedes it, and the AIEWF figure is matched with \d+ and written straight back
    # through the match so this job cannot alter it.
    sub_once_fn(skill,
                rf"(duration\. \(\d+ for aiewf-2026, ){n(bt)}( for yc-startup-school-2026\.\))",
                lambda m: f"{m.group(1)}{at}{m.group(2)}", edits)
    sub_once_fn(skill,
                rf"(quotes\. \(\d+ for aiewf-2026, ){n(bs)}( for yc-startup-school-2026\.\))",
                lambda m: f"{m.group(1)}{asp}{m.group(2)}", edits)
    sub_once(skill,
             rf"{n(bc)} for\n  yc-startup-school-2026 — of which {n(bsy)} carry a synthesis",
             f"{ac} for\n  yc-startup-school-2026 — of which {asy} carry a synthesis", edits)

    # The YC triple appears TWICE in marketplace.json (top-level description and
    # plugins[0].description) and once in plugin.json, so each gets its own anchor on
    # the phrase that introduces it. The AIEWF triple is matched with \d+ and written
    # back through the match: this job reads it, never rewrites it.
    def yc_triple(prefix):
        return (rf"({prefix}AI Engineer World's Fair 2026 \(\d+ talks, \d+ concepts, \d+ "
                rf"speakers\) and Y Combinator Startup School 2026 \()"
                rf"{n(bt)} talks, {n(bc)} concepts, {n(bs)} speakers(\))")

    def write_yc_triple(match):
        return f"{match.group(1)}{at} talks, {ac} concepts, {asp} speakers{match.group(2)}"

    sub_once_fn(plugin, yc_triple("Currently indexed: "), write_yc_triple, edits)
    sub_once_fn(marketplace, yc_triple("currently "), write_yc_triple, edits)
    sub_once_fn(marketplace, yc_triple("Currently indexed: "), write_yc_triple, edits)

    # Event README stats table.
    sub_once(event_readme, rf"\| Talks \| {n(bt)} \({n(bt)} included, 0 excluded\) \|",
             f"| Talks | {at} ({at} included, 0 excluded) |", edits)
    sub_once(event_readme, rf"\| Speakers \| {n(bs)} \|", f"| Speakers | {asp} |", edits)
    sub_once(event_readme,
             rf"\| Concepts with cross-talk synthesis \| {n(bsy)} \(those tagged by "
             rf"{n(PASSC_MIN_TALKS)}\+ talks\) \|",
             f"| Concepts with cross-talk synthesis | {asy} (those tagged by "
             f"{PASSC_MIN_TALKS}+ talks) |", edits)
    sub_once(event_readme, rf"\| Verified quotes \| {n(bq)}, 100% verbatim",
             f"| Verified quotes | {aq}, 100% verbatim", edits)
    before_words = f"{before['words']:,}"
    before_hours = f"{before['hours']:.1f}"
    sub_once(event_readme, rf"\| Words \| {n(before_words)} \|",
             f"| Words | {after['words']:,} |", edits)
    sub_once(event_readme, rf"\| Hours \| {n(before_hours)} \|",
             f"| Hours | {after['hours']:.1f} |", edits)

    sub_once(os.path.join(grader_dir, "correct_counts.md"),
             rf"corpus has {n(bt)} talks, {n(bc)} concepts, and {n(bs)} speakers",
             f"corpus has {at} talks, {ac} concepts, and {asp} speakers", edits)

    with open(plugin, encoding="utf-8") as handle:
        version = json.load(handle)["version"]
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        fail("count_sync", f"plugin.json version {version!r} is not major.minor.patch.")
    new_version = f"{parts[0]}.{parts[1]}.{int(parts[2]) + 1}"
    for path in (plugin, marketplace):
        sub_once(path, rf'"version": "{n(version)}"', f'"version": "{new_version}"', edits)
    log(f"plugin version {version} -> {new_version}")

    old_grader = os.path.join(grader_dir, f"mentions_{bt}.md")
    new_grader = os.path.join(grader_dir, f"mentions_{at}.md")
    if not os.path.exists(old_grader):
        fail("count_sync", f"expected the regex grader at {os.path.relpath(old_grader, REPO)}.")
    sub_once(old_grader, rf'pattern: "{n(bt)}"', f'pattern: "{at}"', edits)
    if old_grader != new_grader:
        subprocess.run(["git", "-C", REPO, "mv", os.path.relpath(old_grader, REPO),
                        os.path.relpath(new_grader, REPO)], check=True, capture_output=True)
        edits.append(f"{os.path.relpath(old_grader, REPO)} -> {os.path.relpath(new_grader, REPO)}")

    REPORT["docs_needing_human_update"] = ["events/yc-startup-school-2026/BUILD.md"]
    log()
    for edit in edits:
        log(f"  updated {edit}")
    log(f"{len(edits)} count-bearing edit(s). BUILD.md carries dated prose and was left "
        "for a human.")


# ---------------------------------------------------------------------------
# 11-12. evals, commit, push
# ---------------------------------------------------------------------------

def eval_gate():
    section("11. EVAL GATE -- the repo's own suite")
    rc, out = run_cmd([sys.executable, os.path.join(REPO, "evals", "run.py")],
                      cwd=REPO, capture=True, check=False, step="evals")
    failed = re.findall(r"^\[\d+/\d+\] (\S+) \.\.\. FAIL", out, re.M)
    summary = re.search(r"(\d+)/(\d+) passing", out)
    if not summary:
        fail("evals", "evals/run.py printed no pass summary; the harness did not complete.")
    passed, total = int(summary.group(1)), int(summary.group(2))
    log(f"first pass: {passed}/{total}")
    if failed:
        still_failing = []
        for case in failed:
            log(f"retrying {case} once (harness flakiness allowance)")
            rrc, _ = run_cmd([sys.executable, os.path.join(REPO, "evals", "run.py"),
                              "--case", case], cwd=REPO, capture=True, check=False, step="evals")
            if rrc != 0:
                still_failing.append(case)
        if still_failing:
            REPORT["evals"] = {"passed": passed, "total": total, "failed": still_failing}
            fail("evals", f"{len(still_failing)} eval case(s) failed twice: {still_failing}. "
                          "Nothing was committed or pushed.")
        passed = total
    REPORT["evals"] = {"passed": passed, "total": total, "failed": []}
    log(f"eval gate: {passed}/{total} passing.")


def commit_and_push(new_records, before, after, no_push):
    section("12. COMMIT" + ("" if no_push else " + PUSH"))
    run_cmd(["git", "-C", REPO, "add", "-A", "--"] + COMMIT_PATHSPEC,
            cwd=REPO, capture=True, step="commit")
    rc, staged = run_cmd(["git", "-C", REPO, "diff", "--cached", "--name-only"],
                         cwd=REPO, capture=True, check=False, step="commit")
    if not staged.strip():
        log("nothing staged; skipping the commit.")
        return

    lines = [f"YC Startup School 2026 refresh: {len(new_records)} newly published "
             f"talk{'s' if len(new_records) != 1 else ''} "
             f"({before['talks']} -> {after['talks']})", ""]
    for rec in new_records:
        speakers = ", ".join(rec.get("speakers") or []) or "unattributed"
        lines.append(f"- {rec['title']} — {speakers}")
    lines += [
        "",
        f"Concepts: {after['concepts']} canonical (frozen), {REPORT['concepts_regenerated']} "
        "re-synthesized in Pass C.",
        f"Quotes: {after['quotes']} verbatim-verified. Speakers: {after['speakers']}.",
        f"Eval suite: {REPORT['evals']['passed']}/{REPORT['evals']['total']} passing.",
    ]
    if REPORT["possible_new_concepts"]:
        lines += ["", f"{len(REPORT['possible_new_concepts'])} dropped concept string(s) appear "
                      "in 3+ talks and may deserve a canonical concept; see the run report."]
    lines += ["", "Generated by scripts/refresh_corpus.py (event-corpus-refresh cron).",
              "", "Co-Authored-By: Claude Opus <noreply@anthropic.com>"]

    run_cmd(["git", "-C", REPO, "commit", "-m", "\n".join(lines)],
            cwd=REPO, capture=True, step="commit")
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


def final_report(new_records, before, after):
    section("RUN REPORT")
    log(f"New talks: {len(new_records)}")
    for rec in new_records:
        log(f"  {rec['title']} — {', '.join(rec.get('speakers') or []) or 'unattributed'}")
        log(f"    {rec.get('url')}")
    log()
    log(f"Corpus:   talks {before['talks']} -> {after['talks']} | "
        f"concepts {after['concepts']} (frozen) | "
        f"speakers {before['speakers']} -> {after['speakers']} | "
        f"quotes {before['quotes']} -> {after['quotes']}")
    log(f"Synthesized concepts (>={PASSC_MIN_TALKS} talks): {after['synthesized']}")
    log(f"Maturity: {dict(after['maturity'])}")
    log(f"Still private/unavailable: {REPORT['still_private']}")
    if REPORT["possible_new_concepts"]:
        log(f"POSSIBLE NEW CONCEPTS needing a human decision "
            f"({len(REPORT['possible_new_concepts'])}):")
        for row in REPORT["possible_new_concepts"]:
            log(f"  {row['talks']} talks: {row['raw']}")
    log(f"Evals: {REPORT['evals']['passed']}/{REPORT['evals']['total']} passing")
    log(f"Committed: {REPORT['committed']} | Pushed: {REPORT['pushed']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    sys.path.insert(0, SCRIPTS)
    REPORT["dry_run"] = args.dry_run
    started = time.time()

    log(f"YC Startup School 2026 corpus refresh — {time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    log(f"project root: {ROOT}")
    log(f"repo root:    {REPO}")
    log(f"mode: {'DRY RUN' if args.dry_run else ('no-push' if args.no_push else 'full')}")

    before = corpus_counts()
    REPORT["talks_before"] = before["talks"]

    candidates = discover()
    accepted = triage(candidates)

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
        REPORT["talks_after"] = before["talks"]
        finish("ok", message="no new talks; data/ untouched")

    snapshot = {rec["video_id"]: {"slug": rec["slug"], "word_count": rec["word_count"]}
                for rec in load_index()}
    harvested = harvest(accepted)
    if not harvested:
        section("NO-OP -- candidates found but none have English captions yet")
        REPORT["talks_after"] = before["talks"]
        finish("ok", message="candidates await captions; data/ untouched")

    new_records = normalize_step(snapshot, harvested)
    if not new_records:
        noop_all_reuploads(before)

    REPORT["new_talks"] = len(new_records)
    REPORT["new_talk_details"] = [
        {"title": r["title"], "speakers": r.get("speakers") or [], "org": r.get("org") or "",
         "track": "", "url": r.get("url", "")} for r in new_records]

    pass_a()
    quote_gate([r["slug"] for r in new_records])
    changed, concept_talks, canonical_names = concepts_step()
    pass_c(changed, concept_talks)
    rebuild()

    after = corpus_counts()
    REPORT["talks_after"] = after["talks"]
    REPORT["concepts_synthesized"] = after["synthesized"]
    count_sync(before, after)
    eval_gate()
    commit_and_push(new_records, before, after, args.no_push)
    final_report(new_records, before, after)

    log()
    log(f"Total wall clock: {(time.time() - started) / 60:.1f} min")
    finish("ok", message=f"{len(new_records)} new talk(s) ingested")


if __name__ == "__main__":
    main()
