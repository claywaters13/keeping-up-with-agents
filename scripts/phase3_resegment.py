#!/usr/bin/env python3
"""Phase 3 (redo): identify who speaks in each of the 10 existing livestream
gaps, sub-segmenting the large ones by scheduled session.

Does NOT touch Phase 1 (shingle alignment) or Phase 2 (timestamp mapping)
outputs. Reuses their deterministic utility functions (normalize_words,
build_chunks, seconds_for_word_index, find_name_matches, infer_org,
identify_via_model) from segment_livestreams.py, and reads gap word_start/
word_end/start_sec/end_sec straight from the existing manifest.json -- those
numbers are not recomputed or altered here.

Method, per gap:
  1. Continuation check: if the gap immediately follows a low/partial-
     confidence covered talk that didn't capture the talk's full word count,
     check whether the gap's opening words are actually the tail of that
     same talk (shingle probe against the talk's own transcript). If so,
     strip that prefix off as "continuation of <slug>" before doing anything
     else, so it isn't misidentified as new content.
  2. Fit a per-stream affine wall_clock = a*stream_sec + b map from the
     verified anchors (iterative outlier removal, threshold 120s).
  3. Project the (remaining) gap's stream-time window through the map to a
     wall-clock window, and pull every Main-Stage session on that stream's
     day whose scheduled time overlaps it (with a padding margin).
  4. For each candidate session, search the gap's own text for its actual
     speaker name(s) (bounded regex on normalized text, same approach as
     the original Phase 3). Matches found = real sub-segment boundaries.
     Candidates never mentioned are dropped (not actually aired).
  5. Segments before the first match / between matches / unresolved gaps
     get "unresolved" (or "continuation") status. Segments >=800 words with
     no schedule resolution go to a `claude -p` model call, capped at 10
     total. Segments <400 words are dropped from the talk set (but counted
     for conservation).

Usage:
  python3 scripts/phase3_resegment.py             # full run
  python3 scripts/phase3_resegment.py --no-model  # skip model calls (report gaps that would need them)
"""
import argparse
import bisect as _bisect
import json
import os
import re
import subprocess
import sys
import time
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from segment_livestreams import (  # noqa: E402
    normalize_words, build_chunks, seconds_for_word_index, chunk_for_word_index,
    name_key, infer_org, extract_json, CLAUDE_CMD,
)

INDEX = os.path.join(ROOT, "data", "index.json")
TRANSCRIPTS = os.path.join(ROOT, "data", "transcripts")
SESSIONS = os.path.join(ROOT, "raw", "sessions.json")
OUTDIR = os.path.join(ROOT, "data", "livestream_segments")
MANIFEST = os.path.join(OUTDIR, "manifest.json")

STREAM_DAY = {
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax": "Day 2 — Session Day 1",
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena": "Day 3 — Session Day 2",
}

ANCHORS = {
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax": [
        (627, "9:05am"), (1697, "9:25am"), (5532, "10:25am"),
        (20880, "2:50pm"), (22727, "3:20pm"), (24482, "3:45pm"), (29513, "5:10pm"),
    ],
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena": [
        (947, "9:05am"), (2123, "9:25am"), (3208, "9:45am"),
        (7315, "10:45am"), (10170, "11:40am"),
    ],
}

RESID_THRESHOLD = 120
WINDOW_PAD_SEC = 1200  # 20 min padding on candidate-session lookup, given
                        # observed fit residuals up to ~85s and possible
                        # further local drift away from anchors.
MIN_GAP_WORDS = 400
LARGE_GAP_WORDS = 800
MODEL_FEED_WORDS = 1200
MODEL_CALL_CAP = 10
MODEL_TIMEOUT = 300  # 5 min hard cap per call, per task instructions

CONTINUATION_TAIL_WORDS = 250   # how far into the preceding talk's own
                                 # transcript we look for its true tail
CONTINUATION_PROBE_LEN = 8      # shingle length for the continuation probe
CONTINUATION_SEARCH_WORDS = 500  # how far into the gap's opening we search


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# --------------------------------------------------------------------------
# Time map fitting
# --------------------------------------------------------------------------

def parse_clock(s):
    s = s.strip().lower()
    ap = s[-2:]
    s = s[:-2]
    h, m = s.split(":")
    h = int(h) % 12
    if ap == "pm":
        h += 12
    return h * 3600 + int(m) * 60


def linreg(pairs):
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    den = sum((x - xbar) ** 2 for x in xs)
    a = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / den
    b = ybar - a * xbar
    resid = [y - (a * x + b) for x, y in zip(xs, ys)]
    return a, b, resid


def fit_time_map(anchor_list, label, report):
    pairs = [(x, parse_clock(wc)) for x, wc in anchor_list]
    kept = list(zip(pairs, anchor_list))  # ((x,y_sec), (x, wc_str))
    round_n = 0
    history = []
    while True:
        round_n += 1
        a, b, resid = linreg([p for p, _ in kept])
        history.append({
            "round": round_n, "a": a, "b": b,
            "anchors": [{"stream_sec": p[0][0], "wall_clock": p[1][1],
                         "residual_sec": round(r, 1)} for p, r in zip(kept, resid)],
        })
        if not resid:
            break
        worst_i = max(range(len(resid)), key=lambda i: abs(resid[i]))
        if abs(resid[worst_i]) <= RESID_THRESHOLD or len(kept) <= 3:
            break
        kept.pop(worst_i)
    dropped = [wc for p, wc in zip([p for p, _ in kept], []) ]  # placeholder unused
    report[label] = history
    return a, b, history


# --------------------------------------------------------------------------
# Schedule
# --------------------------------------------------------------------------

def parse_range(time_str):
    a, b = time_str.split("-")
    return parse_clock(a), parse_clock(b)


def load_day_schedule(sessions, day):
    out = []
    for s in sessions:
        if s.get("day") == day and s.get("room") == "Main Stage":
            st, en = parse_range(s["time"])
            out.append({
                "title": s["title"], "start_sec": st, "end_sec": en,
                "speakers": s.get("speakers") or [], "track": s.get("track"),
                "room": s.get("room"), "time": s["time"], "type": s.get("type"),
                "description": s.get("description", ""),
            })
    out.sort(key=lambda s: s["start_sec"])
    return out


def overlaps(a0, a1, b0, b1):
    return a0 < b1 and b0 < a1


# --------------------------------------------------------------------------
# Name matching within an arbitrary text window (generalization of the
# original find_name_matches, which only looked at the first 200 words --
# here we need to find intros anywhere inside a large multi-talk gap).
# --------------------------------------------------------------------------

# ASR/caption transcription regularly mangles names (transliteration
# variants, dropped/added syllables: "Zixuan Li" -> "Zishan Lee", "Thom Wolf"
# -> "Thomas Wolf"), so exact full-name matching alone misses real mentions.
# Candidate pools here are already narrowed to a handful of sessions by the
# time-window overlap, so a single-token (surname/given-name) fallback is
# much safer here than it would be searching the full 561-session schedule
# (the original Phase 3's reason for avoiding bare-surname matches).
COMMON_WORD_STOPLIST = {
    "song", "may", "will", "grant", "rich", "will", "cook", "gold", "young",
    "hill", "long", "field", "stone", "wood", "park", "king", "bell",
}


def find_all_name_matches(norm_words, candidates):
    """norm_words: list of normalized words (gap-local). candidates: list of
    schedule session dicts. Returns list of (word_pos, session, name,
    match_type), sorted by position, one entry per (session, earliest hit).
    match_type is "full" (both given+surname matched) or "partial" (single
    token fallback -- lower confidence)."""
    text = " ".join(norm_words)
    word_starts_char = []
    pos = 0
    for w in norm_words:
        word_starts_char.append(pos)
        pos += len(w) + 1
    import bisect

    def char_to_word(c):
        i = bisect.bisect_right(word_starts_char, c) - 1
        return max(0, i)

    hits = []
    for s in candidates:
        best = None  # (char_pos, name, match_type)
        for raw_name in s["speakers"]:
            key = name_key(raw_name)
            if not key:
                continue
            tokens = key.split()
            if len(tokens) >= 2:
                pat = r"\b" + re.escape(key) + r"\b"
                m = re.search(pat, text)
                if m and (best is None or m.start() < best[0]):
                    best = (m.start(), raw_name, "full")
            # fallback: individual tokens (surname first, then given name)
            for tok in ([tokens[-1], tokens[0]] if len(tokens) >= 2 else tokens):
                if len(tok) < 4 or tok in COMMON_WORD_STOPLIST:
                    continue
                pat = r"\b" + re.escape(tok) + r"\b"
                m = re.search(pat, text)
                if m and (best is None or (best[2] == "partial" and m.start() < best[0])):
                    if best is None or best[2] == "partial":
                        best = (m.start(), raw_name, "partial")
        if best:
            wpos = char_to_word(best[0])
            hits.append((wpos, s, best[1], best[2]))
    hits.sort(key=lambda h: h[0])
    return hits


# --------------------------------------------------------------------------
# Continuation check
# --------------------------------------------------------------------------

def check_continuation(prev_slug, idx_by_slug, gap_words):
    """Does the gap's opening continue prev_slug's own talk past what the
    covered span captured? Returns (end_word_idx_in_gap, prev_slug) or None."""
    if not prev_slug or prev_slug not in idx_by_slug:
        return None
    tpath = os.path.join(TRANSCRIPTS, f"{prev_slug}.md")
    if not os.path.exists(tpath):
        return None
    traw = open(tpath, encoding="utf-8").read()
    twords = normalize_words(traw)
    tail = twords[-CONTINUATION_TAIL_WORDS:]
    if len(tail) < CONTINUATION_PROBE_LEN:
        return None
    search_space = gap_words[:CONTINUATION_SEARCH_WORDS]
    # Build shingle set of tail, search for latest matching shingle in the
    # gap's opening (closest to the talk's true end = longest continuation).
    best_end = None
    for i in range(0, len(tail) - CONTINUATION_PROBE_LEN + 1):
        shingle = tuple(tail[i:i + CONTINUATION_PROBE_LEN])
        for j in range(0, len(search_space) - CONTINUATION_PROBE_LEN + 1):
            if tuple(search_space[j:j + CONTINUATION_PROBE_LEN]) == shingle:
                end = j + CONTINUATION_PROBE_LEN
                if best_end is None or end > best_end:
                    best_end = end
    if best_end is None:
        return None
    return best_end


# --------------------------------------------------------------------------
# Model fallback
# --------------------------------------------------------------------------

MODEL_PROMPT_HEADER = """You are helping identify a speaker segment cut from a full-day AI \
conference livestream (AI Engineer World's Fair 2026). Below is the OPENING portion of a \
transcript segment. It may be a talk, a break, a sponsor reel, or an MC transition. Identify:

- speaker: the presenter's full name, or "unknown" if not stated/inferable
- org: their company/organization, or "unknown"
- title: the talk/session title, or "unknown" if not stated/inferable
- segment_type: one of "talk", "break", "sponsor", "mc_transition", "other"
- confidence: "high", "medium", or "low"
- reasoning: one sentence

If multiple speakers are introduced (e.g. a panel or fireside chat), list them comma-separated \
in "speaker" and note it in reasoning. Do not guess a specific name/org/title unless the \
transcript actually supports it -- "unknown" is a fine and expected answer for many fields.

Respond with ONLY a JSON object, no prose, no markdown fences:
{"speaker": "...", "org": "...", "title": "...", "segment_type": "...", "confidence": "...", "reasoning": "..."}

TRANSCRIPT SEGMENT:
"""


def identify_via_model_capped(words, state):
    if state["calls"] >= MODEL_CALL_CAP:
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": "model call cap (10) reached"}, "cap_reached"
    feed = " ".join(words[:MODEL_FEED_WORDS])
    payload = MODEL_PROMPT_HEADER + feed
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
    state["calls"] += 1
    t0 = time.time()
    try:
        proc = subprocess.Popen(
            CLAUDE_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, cwd=ROOT, env=env,
        )
        out, err = proc.communicate(payload.encode(), timeout=MODEL_TIMEOUT)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
        log(f"  MODEL TIMEOUT after {MODEL_TIMEOUT}s (call {state['calls']}/{MODEL_CALL_CAP})")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": "model call timed out"}, "claude -p (sonnet)"
    wall = time.time() - t0
    if proc.returncode != 0:
        log(f"  MODEL FAIL rc={proc.returncode} ({wall:.0f}s): {err[:200]!r}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": f"model call failed rc={proc.returncode}"}, "claude -p (sonnet)"
    try:
        envelope = json.loads(out.decode())
    except Exception as e:
        log(f"  MODEL bad envelope: {e}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": "unparseable envelope"}, "claude -p (sonnet)"
    if envelope.get("is_error"):
        log(f"  MODEL is_error: {str(envelope.get('result'))[:200]}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": "model reported is_error"}, "claude -p (sonnet)"
    result = extract_json(envelope.get("result") or "")
    if result is None:
        log("  MODEL bad JSON in result")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "segment_type": "other", "confidence": "low",
                "reasoning": "unparseable model JSON"}, "claude -p (sonnet)"
    log(f"  MODEL ok ({wall:.0f}s, call {state['calls']}/{MODEL_CALL_CAP}): "
        f"speaker={result.get('speaker')!r} title={result.get('title')!r} "
        f"type={result.get('segment_type')!r}")
    return result, "claude -p (sonnet)"


def slugify(title):
    t = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    t = re.sub(r"-+", "-", t)
    return t[:80] or "untitled"


def word_total(talk_slug):
    tpath = os.path.join(TRANSCRIPTS, f"{talk_slug}.md")
    if not os.path.exists(tpath):
        return None
    return len(normalize_words(open(tpath, encoding="utf-8").read()))


def build_stream_data(sslug, manifest_stream):
    raw_text = open(os.path.join(TRANSCRIPTS, f"{sslug}.md"), encoding="utf-8").read()
    chunks, live_len = build_chunks(raw_text)
    assert live_len == manifest_stream["live_len_words"], (
        f"{sslug}: rebuilt live_len {live_len} != manifest {manifest_stream['live_len_words']}")
    words = normalize_words(raw_text)
    assert len(words) == live_len
    starts = [c["word_start"] for c in chunks]
    return {"raw_text": raw_text, "chunks": chunks, "words": words, "starts": starts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-model", action="store_true")
    args = ap.parse_args()

    idx = json.load(open(INDEX))
    idx_by_slug = {r["slug"]: r for r in idx}
    sessions = json.load(open(SESSIONS))["sessions"]
    manifest = json.load(open(MANIFEST))

    fit_report = {}
    model_state = {"calls": 0}
    global_stats = {
        "sub_segments_total": 0, "from_schedule": 0, "from_model": 0,
        "unresolved": 0, "dropped_small": 0, "continuation": 0,
        "dropped_small_words": 0, "continuation_words": 0,
    }

    verify_examples = []  # for verification printout: (title, description, transcript_snippet)
    used_filenames = set()

    if not args.no_model:
        old_gap_files = [f for f in os.listdir(OUTDIR) if "__gap_" in f and f.endswith(".md")]
        for f in old_gap_files:
            os.remove(os.path.join(OUTDIR, f))
        log(f"Removed {len(old_gap_files)} old gap_NNN.md files (superseded by sub-segment files)")

    for sslug, day in STREAM_DAY.items():
        mstream = manifest["streams"][sslug]
        video_id = mstream["video_id"]
        sdata = build_stream_data(sslug, mstream)
        chunks, words, starts, raw_text = sdata["chunks"], sdata["words"], sdata["starts"], sdata["raw_text"]

        a, b, hist = fit_time_map(ANCHORS[sslug], sslug, fit_report)
        log(f"{sslug}: fitted wall_clock = {a:.6f}*stream_sec + {b:.2f} "
            f"({len(hist[-1]['anchors'])}/{len(ANCHORS[sslug])} anchors kept, "
            f"max|resid|={max(abs(x['residual_sec']) for x in hist[-1]['anchors']):.1f}s)")

        covered_spans = mstream["covered_spans"]
        # Sessions already claimed by a Phase 1 covered_span (a duplicate
        # talk with its own corpus entry) must NOT be re-proposed as a
        # candidate for a nearby gap -- otherwise a session like "Memory
        # Harnesses..." that Phase 1 already matched with high confidence
        # gets a second, spurious slice carved out of the adjacent gap
        # purely because the candidate-window padding reaches back into it.
        already_covered_titles = set()
        for sp in covered_spans:
            r = idx_by_slug.get(sp["slug"])
            if r and r.get("title"):
                already_covered_titles.add(r["title"].strip().lower())

        schedule_full = load_day_schedule(sessions, day)
        schedule = [s for s in schedule_full if s["title"].strip().lower() not in already_covered_titles]
        log(f"{sslug}: {len(schedule)}/{len(schedule_full)} Main-Stage sessions on {day} "
            f"available as gap candidates ({len(schedule_full)-len(schedule)} already covered by Phase 1)")

        # map: gap word_start -> preceding covered span (if adjacent)
        prev_by_gap_start = {sp["word_end"]: sp for sp in covered_spans}

        gap_finalized_pairs = []  # (gap, finalized) -- identification done, files not yet written
        for gap in mstream["gap_spans"]:
            gid = gap["gap_id"]
            g_ws, g_we = gap["word_start"], gap["word_end"]
            # Use the authoritative GLOBAL word list sliced by word index --
            # NOT normalize_words(raw_text[char_start:char_end]), which can
            # over-capture a few extra words because Phase 2's char_start/
            # char_end snap to the containing timestamp-marker CHUNK
            # boundary, not the exact word boundary. This keeps our word
            # accounting bit-exact with word_count = word_end - word_start.
            gap_words_full = words[g_ws:g_we]
            assert len(gap_words_full) == gap["word_count"], (
                f"{sslug} gap {gid}: {len(gap_words_full)} != {gap['word_count']}")

            sub_segments = []

            # --- continuation check ---
            remaining_start_local = 0
            prev_sp = prev_by_gap_start.get(g_ws)
            if prev_sp is not None and prev_sp["confidence"] == "low":
                prev_slug = prev_sp["slug"]
                talk_total = word_total(prev_slug)
                if talk_total is not None and prev_sp["word_count"] < talk_total:
                    cont_end = check_continuation(prev_slug, idx_by_slug, gap_words_full)
                    if cont_end:
                        sub_segments.append({
                            "kind": "continuation", "of_slug": prev_slug,
                            "local_start": 0, "local_end": cont_end,
                        })
                        remaining_start_local = cont_end
                        log(f"{sslug} gap {gid}: continuation of '{prev_slug}' "
                            f"detected, {cont_end} words")

            remaining_words = gap_words_full[remaining_start_local:]
            if remaining_words:
                g0 = g_ws + remaining_start_local
                g1 = g_we
                sec0 = seconds_for_word_index(g0, chunks, starts)
                sec1 = seconds_for_word_index(max(g0, g1 - 1), chunks, starts)
                wc0 = a * sec0 + b - WINDOW_PAD_SEC
                wc1 = a * sec1 + b + WINDOW_PAD_SEC
                candidates = [s for s in schedule if overlaps(s["start_sec"], s["end_sec"], wc0, wc1)]
                candidates.sort(key=lambda s: s["start_sec"])

                # --- PRIMARY split: project each candidate's scheduled start
                # through the fitted time map to a word position, and split
                # the gap there. This is what the task spec asks for
                # directly ("split the gap at those session boundaries").
                chunk_seconds = [c["seconds"] for c in chunks]
                chunk_wordstarts = [c["word_start"] for c in chunks]

                def word_for_wallclock(wc_sec):
                    stream_sec = (wc_sec - b) / a
                    i = _bisect.bisect_right(chunk_seconds, stream_sec) - 1
                    i = max(0, min(i, len(chunks) - 1))
                    return chunk_wordstarts[i]

                # Boundaries at BOTH each candidate's scheduled start AND end
                # -- not just start -- so that dead air between sessions
                # (lunch break, transitions) becomes its own leftover
                # interval instead of being swallowed into the previous
                # talk's segment.
                cand_spans = []  # (start_wp, end_wp, candidate)
                for c in candidates:
                    swp = max(g0, min(g1, word_for_wallclock(c["start_sec"])))
                    ewp = max(g0, min(g1, word_for_wallclock(c["end_sec"])))
                    if ewp < swp:
                        ewp = swp
                    cand_spans.append((swp, ewp, c))

                all_bounds = sorted(set([g0, g1] + [s for s, e, c in cand_spans] + [e for s, e, c in cand_spans]))

                segs = []
                for i in range(len(all_bounds) - 1):
                    seg_start, seg_end = all_bounds[i], all_bounds[i + 1]
                    if seg_end <= seg_start:
                        continue
                    mid = (seg_start + seg_end) / 2
                    cand = None
                    for swp, ewp, c in cand_spans:
                        if swp <= mid < ewp or (swp == ewp and swp == seg_start):
                            cand = c
                            break
                    if cand is not None:
                        segs.append({"kind": "schedule", "local_start": seg_start,
                                     "local_end": seg_end, "session": cand})
                    else:
                        segs.append({"kind": "leftover", "local_start": seg_start,
                                     "local_end": seg_end})

                # --- SECONDARY confirmation pass: for each time-derived
                # "schedule" segment, search its own text (plus a little
                # slack into neighboring segments, since intros happen a
                # beat before/after the nominal boundary) for the assigned
                # candidate's name, to set a confidence/QA signal. This does
                # NOT change the split points -- only the identification
                # confidence -- since the time map is the primary splitter
                # per the task spec.
                for seg in segs:
                    if seg["kind"] != "schedule":
                        continue
                    lo = max(g_ws, seg["local_start"] - 150)
                    hi = min(g_we, seg["local_end"] + 150)
                    window_words = words[lo:hi]
                    hits = find_all_name_matches(window_words, [seg["session"]])
                    if hits:
                        seg["matched_name"] = hits[0][2]
                        seg["match_type"] = hits[0][3]
                    else:
                        seg["matched_name"] = None
                        seg["match_type"] = None

                sub_segments.extend(
                    {**s, "local_start": s["local_start"] - g_ws, "local_end": s["local_end"] - g_ws}
                    for s in segs
                )

            # --- finalize each sub-segment: global coords, sizes, ids ---
            finalized = []
            for si, s in enumerate(sub_segments):
                gs = g_ws + s["local_start"]
                ge = g_ws + s["local_end"]
                wc = ge - gs
                sec_s = seconds_for_word_index(gs, chunks, starts)
                sec_e = seconds_for_word_index(max(gs, ge - 1), chunks, starts)
                chunk_s = chunk_for_word_index(gs, chunks, starts)
                chunk_e = chunk_for_word_index(max(gs, ge - 1), chunks, starts)
                raw_snip = raw_text[chunk_s["char_start"]:chunk_s["char_start"] + 4000]
                finalized.append({
                    "sub_id": f"{gid}.{si+1:02d}",
                    "kind": s["kind"],
                    "word_start": gs, "word_end": ge, "word_count": wc,
                    "start_sec": sec_s, "end_sec": sec_e,
                    "duration_sec": max(0, sec_e - sec_s),
                    "deep_link": f"https://www.youtube.com/watch?v={video_id}&t={sec_s}s",
                    "_raw_snip": raw_snip,
                    "_char_start": chunk_s["char_start"], "_char_end": chunk_e["char_end"],
                    "_of_slug": s.get("of_slug"),
                    "_session": s.get("session"),
                    "_matched_name": s.get("matched_name"),
                    "_match_type": s.get("match_type"),
                })

            # --- apply size rules / decide identification ---
            for fs in finalized:
                wc = fs["word_count"]
                global_stats["sub_segments_total"] += 1
                if fs["kind"] == "continuation":
                    fs["identification"] = {
                        "speaker": None, "org": None, "title": None,
                        "note": f"continuation of already-published talk '{fs['_of_slug']}' "
                                f"past what Phase 1's alignment captured",
                    }
                    fs["identification_source"] = "continuation-of-covered-talk"
                    fs["confidence"] = "high"
                    fs["disposition"] = "duplicate"
                    global_stats["continuation"] += 1
                    global_stats["continuation_words"] += wc
                    continue
                if wc < MIN_GAP_WORDS:
                    fs["identification"] = {"speaker": None, "org": None, "title": None}
                    fs["identification_source"] = "dropped-small"
                    fs["confidence"] = "n/a"
                    fs["disposition"] = "dropped"
                    global_stats["dropped_small"] += 1
                    global_stats["dropped_small_words"] += wc
                    continue
                if fs["kind"] == "schedule":
                    sess = fs["_session"]
                    speaker_name = ", ".join(sess["speakers"]) or "unknown"
                    org, org_source = infer_org(sess["speakers"][0] if sess["speakers"] else None,
                                                 fs["_raw_snip"], idx)
                    fs["identification"] = {
                        "speaker": speaker_name, "org": org, "title": sess["title"],
                        "track": sess["track"], "room": sess["room"],
                        "scheduled_time": sess["time"],
                        "matched_name": fs["_matched_name"],
                        "match_type": fs["_match_type"],
                    }
                    fs["identification_source"] = (
                        "sessions.json (time+name confirmed)" if fs["_match_type"]
                        else "sessions.json (time-window match, unconfirmed by transcript text)")
                    fs["confidence"] = {"full": "high", "partial": "medium"}.get(fs["_match_type"], "low")
                    fs["disposition"] = "talk"
                    global_stats["from_schedule"] += 1
                    continue
                # leftover: unresolved by schedule
                if wc >= LARGE_GAP_WORDS and not args.no_model:
                    words_slice = gap_words_full[fs["word_start"] - g_ws: fs["word_end"] - g_ws]
                    result, source = identify_via_model_capped(words_slice, model_state)
                    fs["identification"] = result
                    fs["identification_source"] = source
                    fs["confidence"] = result.get("confidence", "low")
                    fs["disposition"] = ("talk" if result.get("speaker", "unknown") not in
                                          (None, "unknown", "") else "unresolved")
                    global_stats["from_model"] += 1
                else:
                    fs["identification"] = {
                        "speaker": None, "org": None, "title": None,
                        "note": "below model-call threshold (800w) or model calls skipped; "
                                "likely a break, sponsor reel, or MC transition",
                    }
                    fs["identification_source"] = "unresolved"
                    fs["confidence"] = "low"
                    fs["disposition"] = "unresolved"
                    global_stats["unresolved"] += 1

            gap_finalized_pairs.append((gap, finalized))

        # --- cross-gap duplicate-claim detection ---
        # The per-gap candidate window (padded +/-20min for time-map slop)
        # can overlap a neighboring gap's window, so the SAME scheduled
        # session can get independently (and wrongly) proposed as the
        # time-derived match for two different gaps -- e.g. "Thom Wolf
        # keynote" or "Getting the most out of Codex" each got claimed
        # twice in testing. Only the first (gap-order) claim keeps its
        # computed confidence; later claims of the same title are flagged
        # and capped at low confidence for manual review, since they're
        # either a genuine continuation of an unusually long session or a
        # misassignment from time-map drift, and this method can't tell
        # which without a person looking at the transcript.
        claimed_titles = {}
        for gap, finalized in gap_finalized_pairs:
            for fs in finalized:
                if fs["disposition"] == "talk" and fs["identification_source"].startswith("sessions.json"):
                    title = fs["identification"]["title"]
                    # key on (title, speakers) not title alone -- the schedule
                    # legitimately reuses generic titles like "Closing Keynote"
                    # for two different sessions with different speakers.
                    key = (title, fs["identification"].get("speaker"))
                    if key in claimed_titles:
                        fs["identification"]["duplicate_schedule_claim"] = (
                            f"session '{title}' was already assigned to sub-segment "
                            f"{claimed_titles[key]} earlier in this stream -- this may be a "
                            f"continuation of that same long-running session, or a "
                            f"misassignment from time-map drift / overlapping candidate "
                            f"windows. Needs manual review.")
                        fs["confidence"] = "low"
                        fs["identification_source"] += " [DUPLICATE CLAIM -- see identification.duplicate_schedule_claim]"
                    else:
                        claimed_titles[key] = fs["sub_id"]

        # --- write per-sub-segment markdown files (talk + unresolved
        # only; dropped and duplicate/continuation segments don't get
        # their own file, matching how covered_spans already work) ---
        new_gaps = []
        for gap, finalized in gap_finalized_pairs:
            gid = gap["gap_id"]
            for fs in finalized:
                if fs["disposition"] not in ("talk", "unresolved"):
                    continue
                ident = fs["identification"]
                speaker = ident.get("speaker") or "unknown"
                org = ident.get("org") or "unknown"
                title = ident.get("title") or "unknown"
                speakers_list = [] if speaker in ("unknown", "", None) else \
                    [x.strip() for x in speaker.split(",")]
                rec_title = idx_by_slug.get(sslug, {}).get("title", sslug)
                if title not in ("unknown", "", None):
                    display_title = title
                else:
                    seg_type = ident.get("segment_type", "segment")
                    display_title = f"{rec_title} — unidentified {seg_type} ({fs['sub_id']})"

                base_slug = slugify(display_title)
                fname = f"{base_slug}.md"
                n = 2
                while fname in used_filenames:
                    fname = f"{base_slug}-{n}.md"
                    n += 1
                used_filenames.add(fname)
                fs["_filename"] = fname

                dur = fs["duration_sec"]
                dur_h, rem = divmod(dur, 3600)
                dur_m, dur_s = divmod(rem, 60)
                dur_str = f"{dur_h}:{dur_m:02d}:{dur_s:02d}" if dur_h else f"{dur_m}:{dur_s:02d}"

                fm = {
                    "title": display_title,
                    "speakers": speakers_list,
                    "org": "" if org in ("unknown", None) else org,
                    "track": ident.get("track", ""),
                    "video_id": video_id,
                    "url": fs["deep_link"],
                    "duration_sec": dur,
                    "word_count": fs["word_count"],
                    "source_stream": sslug,
                    "gap_id": gid,
                    "sub_id": fs["sub_id"],
                    "word_range": [fs["word_start"], fs["word_end"]],
                    "identification_source": fs["identification_source"],
                    "identification_confidence": fs["confidence"],
                }
                if ident.get("duplicate_schedule_claim"):
                    fm["duplicate_schedule_claim_warning"] = ident["duplicate_schedule_claim"]
                fm_lines = ["---"]
                for k, v in fm.items():
                    fm_lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
                fm_lines.append("---")
                body_text = raw_text[fs["_char_start"]:fs["_char_end"]].strip()
                body = (
                    "\n".join(fm_lines) + "\n\n"
                    f"# {display_title}\n\n"
                    + (f"**{speaker}**" + (f" &middot; {org}" if org not in ("unknown", None, "") else "") + "\n\n"
                       if speakers_list else "")
                    + f"[Watch on YouTube]({fs['deep_link']}) &middot; {dur_str}\n\n"
                    f"## Transcript\n\n{body_text}\n"
                )
                with open(os.path.join(OUTDIR, fname), "w", encoding="utf-8") as fh:
                    fh.write(body)

            new_gaps.append({
                "gap_id": gid, "word_start": gap["word_start"], "word_end": gap["word_end"],
                "word_count": gap["word_count"], "start_sec": gap["start_sec"],
                "end_sec": gap["end_sec"], "deep_link": gap["deep_link"],
                "sub_segments": finalized,
            })

        # strip working/internal fields (raw text snippets, full session
        # dicts, etc.) before serialization -- they were only needed to
        # compute identification and write the .md files above.
        for gap in new_gaps:
            for fs in gap["sub_segments"]:
                for k in list(fs.keys()):
                    if k.startswith("_"):
                        del fs[k]

        mstream["gap_spans_resegmented"] = new_gaps
        mstream["time_map"] = {
            "a": a, "b": b,
            "fit_history": hist,
            "formula": "wall_clock_sec_of_day = a * stream_sec + b",
        }

        # Strip the OLD, deficient whole-gap identification fields (every
        # gap "unresolved"/null from the first, failed Phase 3 run) so the
        # manifest has one authoritative source of identification --
        # gap_spans_resegmented -- instead of two disagreeing ones. The
        # structural word_start/word_end/start_sec/end_sec/deep_link fields
        # (genuine Phase 1/2 output) are left untouched.
        for gap in mstream["gap_spans"]:
            for stale_key in ("identification", "identification_source", "schedule_match_score"):
                gap.pop(stale_key, None)

    # attach model call count + fit report to manifest
    manifest["phase3_resegmentation"] = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model_calls_used": model_state["calls"],
        "model_call_cap": MODEL_CALL_CAP,
        "stats": global_stats,
        "known_issues": [
            "Sub-segments with identification_source containing "
            "'time-window match, unconfirmed by transcript text' were split "
            "purely by projecting the schedule through the fitted affine "
            "time map, with no name match confirming the assigned session. "
            "These are lower-precision than time+name-confirmed matches: "
            "spot-checking found at least one confirmed-wrong case (the "
            "software-factories stream's gap 005, split into 'Rise of the "
            "Software Factory' / 'Orchestras, not Factories' by the time "
            "map, but the actual transcript content there is 'The Agentic "
            "AI Engineer' by Mutagent's co-founder/CEO -- a talk that does "
            "not appear anywhere in raw/sessions.json at all, so it was "
            "never a candidate). Treat unconfirmed low-confidence schedule "
            "matches as provisional and worth a human read before publishing.",
            "Sub-segments flagged with identification.duplicate_schedule_claim "
            "got the same schedule session assigned twice across different "
            "gaps (candidate windows from neighboring gaps can overlap). "
            "The later claim is downgraded to low confidence; only the "
            "earlier one should be trusted without review.",
            "'first-steps-toward-automated-ai-research' (autoresearch "
            "stream) was re-checked per the task's verification step 5: "
            "it is a REAL but PARTIAL alignment, not a bad/coincidental "
            "match. Its low frac (0.37) and truncated span (2227 of 3301 "
            "words, ratio 0.67) come from two edge effects of Phase 1, not "
            "from a wrong match: (a) the front ~1239 words were reassigned "
            "to the preceding 'agents-in-production' talk by Phase 1's "
            "overlap-clipping step, and (b) the tail ~127-150 words were "
            "left outside the span because Phase 1's end boundary is a "
            "naive `diagonal_offset + talk_length` extrapolation rather "
            "than actual shingle evidence, and by the talk's end the real "
            "alignment had drifted off that projection. Phase 3's own "
            "continuation-check independently re-discovered this exact "
            "127-word tail and re-attached it to the correct talk in the "
            "following gap. Verified by direct text comparison: the "
            "covered span's last words ('...many different') and the "
            "following gap's first words ('i call them spaces of "
            "intelligence...') are literally one unbroken sentence in the "
            "talk's own transcript. Not fixed here per the hard constraint "
            "against redoing Phase 1.",
        ],
    }

    # Reconcile OUTDIR: remove any .md file that isn't one we just wrote
    # (a stale sub-segment file from an earlier run, e.g. renamed because
    # a model call gave a different answer on a re-run).
    if not args.no_model:
        current_files = {f for f in os.listdir(OUTDIR) if f.endswith(".md")}
        orphans = current_files - used_filenames
        for f in orphans:
            os.remove(os.path.join(OUTDIR, f))
        if orphans:
            log(f"Removed {len(orphans)} orphaned .md file(s) from a prior run: {sorted(orphans)}")

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
    log(f"Wrote manifest: {MANIFEST}")
    log(f"Model calls used: {model_state['calls']}/{MODEL_CALL_CAP}")
    log(f"Stats: {json.dumps(global_stats, indent=2)}")


if __name__ == "__main__":
    main()
