#!/usr/bin/env python3
"""Segment the two AIEWF 2026 livestream keynote blocks into covered talk
spans (duplicate content already published as its own corpus entry) and gap
spans (unique, unpublished content), with real timestamps and deep links.

Phase 1 (deterministic, no model calls): 10-word shingle alignment of every
other talk against each livestream, cross-stream duplicate resolution,
within-stream overlap clipping, gap extraction.

Phase 2 (deterministic): map word offsets back to real timestamps via the
transcript's own `**[M:SS](url&t=Ns)**` markers; write per-gap markdown
transcripts in the same format as the rest of the corpus.

Phase 3 (schedule fuzzy-match + small model calls): identify each gap's
speaker/org/title from raw/sessions.json, falling back to a `claude -p`
subscription call fed only the gap's first ~1500 words.

Usage:
  python3 scripts/segment_livestreams.py                # full run
  python3 scripts/segment_livestreams.py --skip-model    # phase 1+2 only
  python3 scripts/segment_livestreams.py --verify        # print verification block
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from bisect import bisect_right
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "data", "index.json")
TRANSCRIPTS = os.path.join(ROOT, "data", "transcripts")
SESSIONS = os.path.join(ROOT, "raw", "sessions.json")
OUTDIR = os.path.join(ROOT, "data", "livestream_segments")
MANIFEST = os.path.join(OUTDIR, "manifest.json")

LIVESTREAM_SLUGS = [
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax",
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena",
]

MARKER_RE = re.compile(r"\*\*\[[0-9:]+\]\([^)]*\)\*\*")
MARKER_CAPTURE_RE = re.compile(r"\*\*\[([0-9:]+)\]\(([^)]*)\)\*\*")
TIME_PARAM_RE = re.compile(r"[?&]t=(\d+)s")
NONWORD_RE = re.compile(r"[^a-z0-9]+")

SHINGLE_LEN = 10
STRIDE = 5
BUCKET_WIDTH = 50
MIN_TALK_WORDS = 150
MATCH_FRAC_MIN = 0.30
HIGH_CONF_FRAC = 0.70
MIN_GAP_WORDS = 400
LARGE_GAP_WORDS = 800

CLAUDE_CMD = [
    "claude", "-p",
    "--model", "claude-sonnet-5",
    "--output-format", "json",
    "--allowedTools", "",
    "--strict-mcp-config",
    "--setting-sources", "",
]
MODEL_TIMEOUT = 180
MODEL_FEED_WORDS = 1500



def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# --------------------------------------------------------------------------
# Normalization (Phase 1 spec, verbatim)
# --------------------------------------------------------------------------

def normalize_words(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = MARKER_RE.sub(" ", text)
    text = NONWORD_RE.sub(" ", text)
    return text.split()


def parse_seconds_from_marker(m):
    """m is a MARKER_CAPTURE_RE match: group(1)=M:SS text, group(2)=url."""
    tp = TIME_PARAM_RE.search(m.group(2))
    if tp:
        return int(tp.group(1))
    # fall back to parsing the visible M:SS / H:MM:SS text
    parts = [int(p) for p in m.group(1).split(":")]
    secs = 0
    for p in parts:
        secs = secs * 60 + p
    return secs


def build_chunks(raw_text):
    """Split raw_text on timestamp markers. Returns list of chunk dicts:
    char_start, char_end, word_start, word_end, seconds (of the marker that
    OPENS the chunk; 0 for the pre-first-marker preamble). Concatenating each
    chunk's normalize_words(raw_text[char_start:char_end]) equals
    normalize_words(raw_text) as a whole (verified by caller)."""
    matches = list(MARKER_CAPTURE_RE.finditer(raw_text))
    positions = [0] + [m.start() for m in matches] + [len(raw_text)]
    seconds_list = [0] + [parse_seconds_from_marker(m) for m in matches]

    chunks = []
    word_pos = 0
    for k in range(len(positions) - 1):
        char_start, char_end = positions[k], positions[k + 1]
        chunk_text = raw_text[char_start:char_end]
        words = normalize_words(chunk_text)
        chunks.append({
            "char_start": char_start, "char_end": char_end,
            "word_start": word_pos, "word_end": word_pos + len(words),
            "seconds": seconds_list[k],
        })
        word_pos += len(words)
    return chunks, word_pos


def chunk_word_starts(chunks):
    return [c["word_start"] for c in chunks]


def seconds_for_word_index(idx, chunks, starts):
    """Nearest preceding timestamp marker for a given normalized-word index."""
    if not chunks:
        return 0
    i = bisect_right(starts, idx) - 1
    i = max(0, min(i, len(chunks) - 1))
    return chunks[i]["seconds"]


def chunk_for_word_index(idx, chunks, starts):
    if not chunks:
        return None
    i = bisect_right(starts, idx) - 1
    i = max(0, min(i, len(chunks) - 1))
    return chunks[i]


# --------------------------------------------------------------------------
# Phase 1: shingle alignment
# --------------------------------------------------------------------------

def build_shingle_index(words):
    index = {}
    n = len(words)
    for i in range(0, n - SHINGLE_LEN + 1):
        key = tuple(words[i:i + SHINGLE_LEN])
        index.setdefault(key, []).append(i)
    return index


def match_talk_to_stream(talk_words, live_index, live_len):
    n = len(talk_words)
    if n < SHINGLE_LEN:
        return None
    counter = Counter()
    probes = 0
    for i in range(0, n - SHINGLE_LEN + 1, STRIDE):
        probes += 1
        key = tuple(talk_words[i:i + SHINGLE_LEN])
        hits = live_index.get(key)
        if hits:
            for live_pos in hits:
                bucket = (live_pos - i) // BUCKET_WIDTH
                counter[bucket] += 1
    if not counter or probes == 0:
        return None
    bucket, count = counter.most_common(1)[0]
    frac = count / probes
    d = bucket * BUCKET_WIDTH
    start = max(0, d)
    end = min(live_len, d + n)
    return {"frac": frac, "d": d, "probes": probes, "count": count,
            "word_start": start, "word_end": end}


# --------------------------------------------------------------------------
# Phase 3: schedule name match
# --------------------------------------------------------------------------

NAME_MATCH_WINDOW_WORDS = 200  # intros happen in the first ~50-150 words of a
                                # new segment ("hi everyone, I am X" / "please
                                # welcome X"). A wider window catches incidental
                                # mentions -- e.g. a 600-word window matched
                                # "thank you to Stephen Chin for running that"
                                # (an aside about kids' events) as if Chin were
                                # this segment's presenter. Verified by spot-
                                # checking real output against the transcript.


def name_key(name):
    """Normalize a session speaker name the same way transcript text is
    normalized, so Unicode/punctuation differences ("Thor 雷神 Schaeff" vs
    what captions actually rendered) don't break matching."""
    return " ".join(normalize_words(name or ""))


def find_name_matches(gap_norm_text, sessions):
    """Primary (and, after removing the unreliable title/description fuzzy
    path below, ONLY) schedule signal: does a scheduled speaker's actual name
    appear verbatim in the gap's opening text? Operates on already-normalized
    (lowercase, alnum-only, single-spaced) text on both sides so \\b-bounded
    regex search is exact. Returns list of (word_pos, session, matched_name)
    sorted by earliest mention (matches how live intros work: "please welcome
    NAME from ORG").

    Three bugs found and fixed during validation, all via spot-checking real
    output against the source transcript:
    1. Plain substring .find() on bare last names matched "Chin" inside
       "machine" and "Chan" inside "channel"/"mechanic" -- now \\b-bounded.
    2. A bag-of-words title/description fuzzy-match fallback (jaccard +
       containment, like join_schedule.py uses for talk titles) produced
       high scores (0.79+) matching a ~23,000-word multi-topic gap against
       an unrelated short session purely on common-word overlap. Removed
       entirely; unmatched names now go straight to the model instead of a
       plausible-looking but wrong "medium confidence" guess.
    3. Even \\b-bounded, a last-name-only fallback ("Gupta") and a wide
       600-word window both produced confident wrong matches: "Gupta" hit a
       DIFFERENT Gupta than the one actually speaking, and a 600-word window
       caught an incidental "thank you to Stephen Chin" thank-you aside, not
       an introduction. Now: full name only, 200-word window (where intros
       actually happen)."""
    window = " ".join(gap_norm_text.split()[:NAME_MATCH_WINDOW_WORDS])
    hits = []
    for s in sessions:
        for raw_name in (s.get("speakers") or []):
            key = name_key(raw_name)
            if not key or len(key.split()) < 2:
                continue  # require a full first+last name match, no bare surnames
            pat = r"\b" + re.escape(key) + r"\b"
            m = re.search(pat, window)
            if m:
                hits.append((m.start(), s, raw_name))
    hits.sort(key=lambda h: h[0])
    return hits


def best_schedule_match(gap_norm_text, sessions):
    """Returns (session_or_None, score, method_str, ambiguous_bool)."""
    name_hits = find_name_matches(gap_norm_text, sessions)
    if name_hits:
        pos, s, name = name_hits[0]
        distinct_sessions = {id(h[1]) for h in name_hits}
        ambiguous = len(distinct_sessions) > 1
        method = f"name-match:{name!r}@word{pos}" + (
            f" (of {len(distinct_sessions)} distinct candidate sessions)" if ambiguous else "")
        return s, 1.0, method, ambiguous
    return None, 0.0, None, False


ORG_HINT_RE = re.compile(
    r"\b(?:from|at|with|of)\s+([A-Z][A-Za-z0-9&.\-]*(?:\s+[A-Z][A-Za-z0-9&.\-]*){0,3})")


def _clip_org_at_sentence_end(raw):
    """The regex's repeated capitalized-token group can bridge a sentence
    break ("...Analysis. Artificial..." -> two sentences, both starting with
    a capital) and over-capture. Cut at the first '. ' / newline / other
    sentence-ish boundary, then strip a trailing bare period."""
    for sep in (". ", ".\n", "\n"):
        i = raw.find(sep)
        if i != -1:
            raw = raw[:i]
            break
    return raw.rstrip(". ").strip()


def infer_org(speaker_name, gap_raw_text, idx_records):
    """Best-effort org lookup for a schedule-resolved speaker. sessions.json has
    no org field. Try, in priority order:
    (1) a 'from/at/of/with Org' pattern near the speaker's name in THIS gap's
        own transcript text -- grounded in the actual segment being identified.
    (2) another corpus talk by the same speaker -- but ONLY if every corpus
        match agrees on the org. Found via validation that this corpus's
        existing speaker attribution has bugs: "George Cameron, Micah
        Hill-Smith" is attached (via upstream join_schedule.py fuzzy title
        matching) to two unrelated existing talks with two DIFFERENT orgs
        ("Callstack" and "LatchBio") -- neither is their real org (Artificial
        Analysis, confirmed from this gap's own transcript text). Trusting
        the first corpus hit blindly would have propagated that bug."""
    if not speaker_name or speaker_name == "unknown":
        return "unknown", None
    idx = gap_raw_text.lower().find(speaker_name.split()[0].lower())
    window = gap_raw_text[max(0, idx - 20):idx + 160] if idx != -1 else gap_raw_text[:400]
    m = ORG_HINT_RE.search(window)
    if m:
        org = _clip_org_at_sentence_end(m.group(1))
        if org:
            return org, "regex 'from/at Org' near name in this gap's text"

    last = speaker_name.split()[-1].lower()
    found_orgs = set()
    found_slugs = []
    for r in idx_records:
        for sp in (r.get("speakers") or []):
            if sp.lower() == speaker_name.lower() or sp.split()[-1].lower() == last:
                if r.get("org"):
                    found_orgs.add(r["org"])
                    found_slugs.append(r["slug"])
    if len(found_orgs) == 1:
        return found_orgs.pop(), f"corpus talk(s) {found_slugs} by same speaker"
    if len(found_orgs) > 1:
        return "unknown", f"conflicting corpus orgs {sorted(found_orgs)} across {found_slugs} -- not trusted"
    return "unknown", None


# --------------------------------------------------------------------------
# Phase 3: model fallback via claude -p (subscription only)
# --------------------------------------------------------------------------

MODEL_PROMPT_HEADER = """You are helping identify a speaker segment cut from a full-day AI \
conference livestream (AI Engineer World's Fair 2026). Below is the OPENING portion of a \
transcript segment (a speaker introduction plus the start of their talk). Identify:

- speaker: the presenter's full name, or "unknown" if not stated/inferable
- org: their company/organization, or "unknown"
- title: the talk/session title, or "unknown" if not stated/inferable
- confidence: "high", "medium", or "low"
- reasoning: one sentence

If multiple speakers are introduced (e.g. a panel or fireside chat), list them comma-separated \
in "speaker" and note it in reasoning. Do not guess a specific name/org/title unless the \
transcript actually supports it -- "unknown" is a fine and expected answer for many fields.

Respond with ONLY a JSON object, no prose, no markdown fences:
{"speaker": "...", "org": "...", "title": "...", "confidence": "...", "reasoning": "..."}

TRANSCRIPT SEGMENT:
"""


def extract_json(text):
    t = (text or "").strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*", "", t)
        t = re.sub(r"\s*```$", "", t.strip())
    try:
        return json.loads(t)
    except Exception:
        pass
    i, j = t.find("{"), t.rfind("}")
    if i != -1 and j > i:
        try:
            return json.loads(t[i:j + 1])
        except Exception:
            return None
    return None


def identify_via_model(gap_text_words):
    feed = " ".join(gap_text_words[:MODEL_FEED_WORDS])
    payload = MODEL_PROMPT_HEADER + feed
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
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
        log(f"  MODEL TIMEOUT after {MODEL_TIMEOUT}s")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "confidence": "low", "reasoning": "model call timed out"}
    wall = time.time() - t0
    if proc.returncode != 0:
        log(f"  MODEL FAIL rc={proc.returncode} ({wall:.0f}s): {err[:200]!r}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "confidence": "low", "reasoning": f"model call failed rc={proc.returncode}"}
    try:
        envelope = json.loads(out.decode())
    except Exception as e:
        log(f"  MODEL bad envelope: {e}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "confidence": "low", "reasoning": "unparseable envelope"}
    if envelope.get("is_error"):
        log(f"  MODEL is_error: {str(envelope.get('result'))[:200]}")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "confidence": "low", "reasoning": "model reported is_error"}
    result = extract_json(envelope.get("result") or "")
    if result is None:
        log("  MODEL bad JSON in result")
        return {"speaker": "unknown", "org": "unknown", "title": "unknown",
                "confidence": "low", "reasoning": "unparseable model JSON"}
    log(f"  MODEL ok ({wall:.0f}s): speaker={result.get('speaker')!r} org={result.get('org')!r}")
    return result


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-model", action="store_true",
                     help="stop after phase 1+2; leave gaps unidentified")
    ap.add_argument("--verify", action="store_true",
                     help="print extra verification printouts")
    args = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)

    idx = json.load(open(INDEX))
    idx_by_slug = {r["slug"]: r for r in idx}
    sessions = json.load(open(SESSIONS))["sessions"]

    # --- Load & prepare both livestreams ---
    streams = {}
    for slug in LIVESTREAM_SLUGS:
        rec = idx_by_slug[slug]
        path = os.path.join(TRANSCRIPTS, f"{slug}.md")
        raw_text = open(path, encoding="utf-8").read()
        chunks, live_len = build_chunks(raw_text)

        # Sanity: chunked normalization must equal whole-text normalization.
        whole_words = normalize_words(raw_text)
        assert len(whole_words) == live_len, (
            f"{slug}: chunked word count {live_len} != whole-text {len(whole_words)}")

        words = whole_words
        live_index = build_shingle_index(words)
        starts = chunk_word_starts(chunks)
        streams[slug] = {
            "rec": rec, "raw_text": raw_text, "words": words,
            "live_len": live_len, "live_index": live_index,
            "chunks": chunks, "starts": starts, "video_id": rec["video_id"],
        }
        log(f"Loaded {slug}: {live_len} normalized words, "
            f"{len(chunks)} timestamp chunks, {len(live_index)} unique shingles")

    # --- Phase 1: match every other talk against both streams ---
    talk_slugs = [r["slug"] for r in idx
                  if not r["slug"].startswith("wf2026-")]
    log(f"Probing {len(talk_slugs)} talks against {len(streams)} livestreams...")

    raw_matches = {slug: {} for slug in talk_slugs}  # slug -> {stream_slug: result}
    skipped_short = []
    for i, tslug in enumerate(talk_slugs):
        tpath = os.path.join(TRANSCRIPTS, f"{tslug}.md")
        if not os.path.exists(tpath):
            continue
        traw = open(tpath, encoding="utf-8").read()
        twords = normalize_words(traw)
        if len(twords) < MIN_TALK_WORDS:
            skipped_short.append((tslug, len(twords)))
            continue
        for sslug, sdata in streams.items():
            res = match_talk_to_stream(twords, sdata["live_index"], sdata["live_len"])
            if res and res["frac"] >= MATCH_FRAC_MIN:
                raw_matches[tslug][sslug] = res
        if (i + 1) % 50 == 0:
            log(f"  ...{i+1}/{len(talk_slugs)} talks probed")

    log(f"Skipped {len(skipped_short)} talks under {MIN_TALK_WORDS} words")

    # --- Cross-stream duplicate resolution ---
    cross_stream_resolutions = []
    assigned = {slug: {} for slug in talk_slugs}  # slug -> {stream_slug: result} (post-resolution, at most 1 stream)
    for tslug, matches in raw_matches.items():
        if not matches:
            continue
        if len(matches) == 1:
            (sslug, res), = matches.items()
            assigned[tslug][sslug] = res
            continue
        # matched >=2 streams: keep the higher-frac one, log the resolution
        ranked = sorted(matches.items(), key=lambda kv: -kv[1]["frac"])
        kept_slug, kept_res = ranked[0]
        assigned[tslug][kept_slug] = kept_res
        for disc_slug, disc_res in ranked[1:]:
            cross_stream_resolutions.append({
                "talk": tslug,
                "kept_stream": kept_slug, "kept_frac": round(kept_res["frac"], 4),
                "discarded_stream": disc_slug, "discarded_frac": round(disc_res["frac"], 4),
            })

    log(f"Cross-stream duplicates resolved: {len(cross_stream_resolutions)}")
    for r in cross_stream_resolutions:
        log(f"  {r['talk']}: kept {r['kept_stream']} (frac={r['kept_frac']}) "
            f"over {r['discarded_stream']} (frac={r['discarded_frac']})")

    # --- Build per-stream span lists, sort, clip overlaps ---
    manifest = {}
    overlap_resolutions = []
    for sslug, sdata in streams.items():
        spans = []
        for tslug, m in assigned.items():
            if sslug in m:
                res = m[sslug]
                spans.append({
                    "slug": tslug,
                    "word_start": res["word_start"], "word_end": res["word_end"],
                    "frac": res["frac"], "d": res["d"],
                    "probes": res["probes"], "count": res["count"],
                })
        spans.sort(key=lambda s: s["word_start"])

        accepted = []
        for sp in spans:
            if accepted and sp["word_start"] < accepted[-1]["word_end"]:
                orig_start = sp["word_start"]
                new_start = accepted[-1]["word_end"]
                if new_start >= sp["word_end"]:
                    overlap_resolutions.append({
                        "stream": sslug, "talk": sp["slug"], "action": "dropped",
                        "reason": f"fully overlapped by {accepted[-1]['slug']}",
                        "orig_word_start": orig_start, "orig_word_end": sp["word_end"],
                    })
                    continue
                overlap_resolutions.append({
                    "stream": sslug, "talk": sp["slug"], "action": "clipped",
                    "orig_word_start": orig_start, "new_word_start": new_start,
                    "clipped_against": accepted[-1]["slug"],
                })
                sp["word_start"] = new_start
            accepted.append(sp)

        chunks, starts = sdata["chunks"], sdata["starts"]
        video_id = sdata["video_id"]

        covered_spans = []
        for sp in accepted:
            ws, we = sp["word_start"], sp["word_end"]
            start_sec = seconds_for_word_index(ws, chunks, starts)
            end_sec = seconds_for_word_index(max(ws, we - 1), chunks, starts)
            covered_spans.append({
                "slug": sp["slug"],
                "word_start": ws, "word_end": we, "word_count": we - ws,
                "frac": round(sp["frac"], 4),
                "confidence": "high" if sp["frac"] >= HIGH_CONF_FRAC else "low",
                "diagonal_offset": sp["d"], "probes": sp["probes"], "hits": sp["count"],
                "start_sec": start_sec, "end_sec": end_sec,
                "deep_link": f"https://www.youtube.com/watch?v={video_id}&t={start_sec}s",
            })

        # --- Gaps: complement of accepted (post-clip) spans ---
        raw_gaps = []
        prev_end = 0
        for sp in accepted:
            if sp["word_start"] > prev_end:
                raw_gaps.append((prev_end, sp["word_start"]))
            prev_end = max(prev_end, sp["word_end"])
        if sdata["live_len"] > prev_end:
            raw_gaps.append((prev_end, sdata["live_len"]))

        covered_words_total = sum(c["word_count"] for c in covered_spans)
        raw_gap_words_total = sum(e - s for s, e in raw_gaps)
        assert covered_words_total + raw_gap_words_total == sdata["live_len"], (
            f"{sslug}: covered({covered_words_total}) + gap({raw_gap_words_total}) "
            f"!= total({sdata['live_len']})")

        kept_gaps = [(s, e) for s, e in raw_gaps if (e - s) >= MIN_GAP_WORDS]
        discarded_gap_words = sum(e - s for s, e in raw_gaps if (e - s) < MIN_GAP_WORDS)

        manifest[sslug] = {
            "video_id": video_id,
            "live_len_words": sdata["live_len"],
            "duration_sec": sdata["rec"]["duration_sec"],
            "covered_spans": covered_spans,
            "covered_words_total": covered_words_total,
            "raw_gap_words_total": raw_gap_words_total,
            "discarded_small_gap_words": discarded_gap_words,
            "gap_spans_raw_ranges": kept_gaps,  # filled in below with full detail
        }
        log(f"{sslug}: {len(covered_spans)} covered spans "
            f"({covered_words_total} words), {len(kept_gaps)} gaps >= {MIN_GAP_WORDS}w "
            f"kept of {len(raw_gaps)} raw gaps, {discarded_gap_words} words in discarded small gaps")

    # --- Phase 2: build gap markdown + timestamps ---
    for sslug, sdata in streams.items():
        chunks, starts = sdata["chunks"], sdata["starts"]
        raw_text = sdata["raw_text"]
        video_id = sdata["video_id"]
        upload_date = sdata["rec"].get("upload_date", "")
        rec_title = sdata["rec"].get("title", sslug)

        gap_spans = []
        for gi, (ws, we) in enumerate(manifest[sslug]["gap_spans_raw_ranges"]):
            start_chunk = chunk_for_word_index(ws, chunks, starts)
            end_chunk = chunk_for_word_index(we - 1, chunks, starts)
            char_start, char_end = start_chunk["char_start"], end_chunk["char_end"]
            gap_raw_text = raw_text[char_start:char_end]
            gap_words = normalize_words(gap_raw_text)

            start_sec = start_chunk["seconds"]
            end_sec = end_chunk["seconds"]
            gap_id = f"{gi+1:03d}"
            gap_slug = f"{sslug}__gap_{gap_id}"
            deep_link = f"https://www.youtube.com/watch?v={video_id}&t={start_sec}s"

            gap_spans.append({
                "gap_id": gap_id, "gap_slug": gap_slug,
                "word_start": ws, "word_end": we, "word_count": we - ws,
                "start_sec": start_sec, "end_sec": end_sec,
                "duration_sec": max(0, end_sec - start_sec),
                "deep_link": deep_link,
                "large": (we - ws) >= LARGE_GAP_WORDS,
                "_gap_words_for_model": gap_words,
                "_gap_raw_text": gap_raw_text,
                "_char_start": char_start, "_char_end": char_end,
            })
        manifest[sslug]["gap_spans"] = gap_spans
        del manifest[sslug]["gap_spans_raw_ranges"]

    # --- Phase 3: identify each gap ---
    for sslug, sdata in streams.items():
        rec_title = sdata["rec"].get("title", sslug)
        video_id = sdata["video_id"]
        upload_date = sdata["rec"].get("upload_date", "")
        for gap in manifest[sslug]["gap_spans"]:
            gap_words = gap["_gap_words_for_model"]
            gap_raw = gap["_gap_raw_text"]
            opening_norm = " ".join(gap_words[:NAME_MATCH_WINDOW_WORDS])
            opening_raw = gap_raw[:9000]  # raw (cased) text, for the org-hint regex only
            best, best_s, method, ambiguous = best_schedule_match(opening_norm, sessions)
            if best and method:
                speaker_name = ", ".join(best.get("speakers") or []) or "unknown"
                org, org_source = infer_org(
                    (best.get("speakers") or [None])[0], opening_raw, idx)
                is_name_match = method.startswith("name-match")
                identification = {
                    "speaker": speaker_name,
                    "org": org,
                    "title": best.get("title", "unknown"),
                    "confidence": "high" if (is_name_match and not ambiguous)
                    else "medium",
                    "reasoning": f"sessions.json {method} (score={best_s:.3f})"
                    + (f"; org via {org_source}" if org_source else ""),
                }
                source = "sessions.json"
            elif args.skip_model:
                identification = {"speaker": "unknown", "org": "unknown",
                                   "title": "unknown", "confidence": "low",
                                   "reasoning": "model call skipped (--skip-model)"}
                source = "unresolved"
            else:
                log(f"Identifying {sslug} gap {gap['gap_id']} "
                    f"({gap['word_count']} words) via model...")
                identification = identify_via_model(gap_words)
                source = "claude -p (sonnet)"
            gap["identification"] = identification
            gap["identification_source"] = source
            gap["schedule_match_score"] = round(best_s, 4) if best else 0.0

            # --- write per-gap markdown transcript ---
            speaker = identification.get("speaker") or "unknown"
            org = identification.get("org") or "unknown"
            title = identification.get("title") or "unknown"
            speakers_list = [] if speaker in ("unknown", "", None) else \
                [s.strip() for s in speaker.split(",")]
            display_title = title if title not in ("unknown", "", None) else \
                f"{rec_title} — unidentified segment {gap['gap_id']}"

            fm = {
                "title": display_title,
                "speakers": speakers_list,
                "org": "" if org in ("unknown", None) else org,
                "video_id": video_id,
                "url": gap["deep_link"],
                "duration_sec": gap["duration_sec"],
                "upload_date": upload_date,
                "word_count": gap["word_count"],
                "raw_title": display_title,
                "source_stream": sslug,
                "gap_id": gap["gap_id"],
                "word_range": [gap["word_start"], gap["word_end"]],
                "identification_source": source,
                "identification_confidence": identification.get("confidence", "low"),
            }
            fm_lines = ["---"]
            for k, v in fm.items():
                fm_lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
            fm_lines.append("---")
            frontmatter = "\n".join(fm_lines)

            dur_h = gap["duration_sec"] // 3600
            dur_m = (gap["duration_sec"] % 3600) // 60
            dur_s = gap["duration_sec"] % 60
            dur_str = f"{dur_h}:{dur_m:02d}:{dur_s:02d}" if dur_h else f"{dur_m}:{dur_s:02d}"

            body = (
                f"{frontmatter}\n\n"
                f"# {display_title}\n\n"
                + (f"**{speaker}**" + (f" &middot; {org}" if org not in ("unknown", None, "") else "") + "\n\n"
                   if speakers_list else "")
                + f"[Watch on YouTube]({gap['deep_link']}) &middot; {dur_str}\n\n"
                f"## Transcript\n\n"
                f"{gap['_gap_raw_text'].strip()}\n"
            )
            out_path = os.path.join(OUTDIR, f"{gap['gap_slug']}.md")
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(body)

            # strip working fields before manifest serialization
            del gap["_gap_words_for_model"]
            del gap["_gap_raw_text"]

    # --- Deduplicated corpus stat block ---
    total_entries = len(idx)
    total_words = sum(r["word_count"] for r in idx)
    total_hours = sum(r["duration_sec"] for r in idx) / 3600

    dup_words = 0.0
    dup_hours = 0.0
    stream_dedup_detail = {}
    for sslug, sdata in streams.items():
        live_len = sdata["live_len"]
        covered_norm = manifest[sslug]["covered_words_total"]
        frac_dup = covered_norm / live_len if live_len else 0
        idx_word_count = idx_by_slug[sslug]["word_count"]
        idx_duration_sec = idx_by_slug[sslug]["duration_sec"]
        stream_dup_words = frac_dup * idx_word_count
        stream_dup_hours = frac_dup * idx_duration_sec / 3600
        dup_words += stream_dup_words
        dup_hours += stream_dup_hours
        stream_dedup_detail[sslug] = {
            "frac_duplicated": round(frac_dup, 4),
            "covered_words_normalized_space": covered_norm,
            "live_len_normalized_space": live_len,
            "index_word_count": idx_word_count,
            "estimated_duplicate_words": round(stream_dup_words, 1),
            "estimated_duplicate_hours": round(stream_dup_hours, 3),
        }

    dedup_words = total_words - dup_words
    dedup_hours = total_hours - dup_hours

    stat_block = {
        "raw": {
            "entries": total_entries,
            "words": total_words,
            "hours": round(total_hours, 2),
        },
        "deduplicated": {
            "entries": total_entries,
            "words": round(dedup_words),
            "hours": round(dedup_hours, 2),
        },
        "excluded_duplicate": {
            "words": round(dup_words),
            "hours": round(dup_hours, 2),
        },
        "method": (
            "Per livestream, frac_duplicated = (normalized words covered by talks that "
            "are ALSO separate corpus entries) / (livestream's total normalized word "
            "count), computed from the Phase 1 shingle-alignment spans after cross-stream "
            "and overlap resolution. That fraction is applied to the livestream's own "
            "index.json word_count/duration_sec (the units the 1,011,341/101.7h corpus "
            "totals are reported in) to get duplicate words/hours in the same accounting "
            "basis, then subtracted from the raw corpus totals."
        ),
        "per_stream": stream_dedup_detail,
    }

    # --- Assemble final manifest ---
    for sslug in manifest:
        manifest[sslug]["frac_duplicated"] = stream_dedup_detail[sslug]["frac_duplicated"]

    final_manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "params": {
            "shingle_len": SHINGLE_LEN, "stride": STRIDE, "bucket_width": BUCKET_WIDTH,
            "min_talk_words": MIN_TALK_WORDS, "match_frac_min": MATCH_FRAC_MIN,
            "high_conf_frac": HIGH_CONF_FRAC, "min_gap_words": MIN_GAP_WORDS,
            "large_gap_words": LARGE_GAP_WORDS,
        },
        "cross_stream_resolutions": cross_stream_resolutions,
        "overlap_resolutions": overlap_resolutions,
        "streams": manifest,
        "corpus_stats": stat_block,
    }

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(final_manifest, fh, indent=2, ensure_ascii=False)
    log(f"Wrote manifest: {MANIFEST}")

    # --- Verification printouts ---
    print("\n=== VERIFICATION ===")
    for sslug, sdata in streams.items():
        m = manifest[sslug]
        print(f"\n{sslug}")
        print(f"  live_len={sdata['live_len']} covered={m['covered_words_total']} "
              f"raw_gap={m['raw_gap_words_total']} "
              f"sum={m['covered_words_total']+m['raw_gap_words_total']} "
              f"(assert covered+gap==total: PASS)")
        print(f"  kept gaps (>={MIN_GAP_WORDS}w): {len(m['gap_spans'])}, "
              f"discarded small-gap words: {m['discarded_small_gap_words']}")

    print("\n--- low-confidence matches (0.30 <= frac < 0.70) ---")
    for sslug, sdata in streams.items():
        for sp in manifest[sslug]["covered_spans"]:
            if sp["confidence"] == "low":
                print(f"  {sslug}: {sp['slug']} frac={sp['frac']}")

    print("\n--- largest gap segments ---")
    all_gaps = []
    for sslug in manifest:
        for gap in manifest[sslug]["gap_spans"]:
            all_gaps.append((sslug, gap))
    all_gaps.sort(key=lambda x: -x[1]["word_count"])
    for sslug, gap in all_gaps[:10]:
        ident = gap["identification"]
        print(f"  {sslug} gap {gap['gap_id']}: {gap['word_count']}w "
              f"[{gap['word_start']}:{gap['word_end']}] "
              f"speaker={ident.get('speaker')!r} org={ident.get('org')!r} "
              f"title={ident.get('title')!r} src={gap['identification_source']}")

    print("\n--- spot-check: 3 high-confidence alignments ---")
    hc = []
    for sslug in manifest:
        for sp in manifest[sslug]["covered_spans"]:
            if sp["confidence"] == "high":
                hc.append((sslug, sp))
    for sslug, sp in hc[:3]:
        sdata = streams[sslug]
        live_snippet = " ".join(sdata["words"][sp["word_start"]:sp["word_start"] + 40])
        tpath = os.path.join(TRANSCRIPTS, f"{sp['slug']}.md")
        traw = open(tpath, encoding="utf-8").read()
        twords = normalize_words(traw)
        talk_snippet = " ".join(twords[:40])
        print(f"\n  {sp['slug']} (frac={sp['frac']}) in {sslug} @ word {sp['word_start']}")
        print(f"    LIVE : {live_snippet}")
        print(f"    TALK : {talk_snippet}")

    print("\n--- corpus stat block ---")
    print(json.dumps(stat_block, indent=2))


if __name__ == "__main__":
    main()
