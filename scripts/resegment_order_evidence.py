#!/usr/bin/env python3
"""Phase 3 (rebuild #2): identify livestream gap content using SCHEDULE ORDER
plus TEXT EVIDENCE, not time-window projection.

Why the previous approach (phase3_resegment.py, superseded) failed: it fit an
affine stream-time -> wall-clock map and picked whichever scheduled session
overlapped that projected time window. The conference ran ~13 parallel
tracks, so a time window alone cannot disambiguate -- at 11:40am on Day 2
alone there are 13 different scheduled sessions running. Time is a weak
prior, never evidence.

This script instead uses two facts, both confirmed by direct inspection of
raw/sessions.json:

1. Every Phase-1 anchor (a covered span whose separately-published talk we
   can identify by real name) turns out to be a "Main Stage" session on the
   correct day. Day 2 Main Stage has exactly 19 sessions; Day 3 Main Stage
   has exactly 18. These counts match each livestream's content almost
   exactly. So each livestream IS (up to a handful of off-schedule cutaways)
   the Main Stage feed for its day, which prunes the 13-parallel-track
   problem down to ~18-19 candidates *before* any text search happens.
2. Clay's governing assumption: schedule ORDER was followed even though
   TIMES drifted, and each speaker presented exactly one scheduled session.
   So within a bracket between two confirmed anchors, the only candidates
   are the Main Stage sessions whose schedule order falls between the
   anchors' schedule indices -- and a monotonic (order-preserving) DP chooses
   the subset with real textual evidence, maximizing total evidence weight.

Anything without a strong textual signal (full name adjacent, distinctive
surname, or a distinctive multi-word title phrase) is discarded, not guessed.

Usage:
  python3 scripts/resegment_order_evidence.py               # full run, writes manifest + gap markdown
  python3 scripts/resegment_order_evidence.py --report-only # print verification report, don't write files
"""
import argparse
import json
import os
import re
import sys
import time
import unicodedata
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from segment_livestreams import (  # noqa: E402
    normalize_words, build_chunks, seconds_for_word_index, chunk_for_word_index,
)

INDEX = os.path.join(ROOT, "data", "index.json")
TRANSCRIPTS = os.path.join(ROOT, "data", "transcripts")
SESSIONS = os.path.join(ROOT, "raw", "sessions.json")
OUTDIR = os.path.join(ROOT, "data", "livestream_segments")
MANIFEST = os.path.join(OUTDIR, "manifest.json")

LIVESTREAM_SLUGS = [
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax",
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena",
]

STREAM_DAY = {
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax": "Day 2 — Session Day 1",
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena": "Day 3 — Session Day 2",
}

MIN_SEGMENT_WORDS = 400

# --------------------------------------------------------------------------
# Name / text normalization
# --------------------------------------------------------------------------

def norm_name(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z ]", " ", s)
    return " ".join(s.split())


def split_speaker_field(field):
    """YouTube-title-derived speaker strings sometimes glue multiple people
    together ('Tisha Chawla & Susheem Koul'). Split on common separators."""
    parts = re.split(r",| & | and |/", field)
    return [p.strip() for p in parts if p.strip()]


def parse_time_start(t):
    """'9:05am-9:25am' -> minutes since midnight of the start time."""
    start = t.split("-")[0].strip().lower()
    ap = start[-2:]
    hm = start[:-2]
    h, mi = hm.split(":")
    h = int(h) % 12
    if ap == "pm":
        h += 12
    return h * 60 + int(mi)


TITLE_STOPWORDS = set("""
a an the of to in on for with at from by is are was were be been being
your you we our their his her its it this that these those and or but not
how what why when where who which as it's we're don't dont ai the a2a mcp
""".split())

COMMON_SURNAME_STOP = set("""
king young hall green white black short long field hill cook stone gray
grey short good best new day west east north south main first last
""".split())


def title_phrase_candidates(title):
    """Contiguous runs of >=3 words from the normalized title where NONE of
    the words is a generic stopword -- 'distinctive multi-word phrase',
    per Clay's instruction, NOT individual keywords."""
    words = norm_name(title).split()
    n = len(words)
    out = []
    i = 0
    while i < n:
        if words[i] in TITLE_STOPWORDS or len(words[i]) < 3:
            i += 1
            continue
        j = i
        while j < n and words[j] not in TITLE_STOPWORDS and len(words[j]) >= 3:
            j += 1
        run = words[i:j]
        if len(run) >= 3:
            # emit the longest run, and also its first 3-4 word prefix as a
            # slightly more lenient fallback (titles are often abbreviated
            # or reworded when spoken aloud)
            out.append(run)
        i = j + 1
    return out


MC_PATTERNS = [
    "please welcome", "give it up for", "our next speaker", "take it away",
    "let's welcome", "lets welcome", "welcome to the stage",
    "join me in welcoming", "put your hands together", "next up we have",
    "please give a warm welcome",
]

ORG_HINT_RE = re.compile(
    r"\b(?:from|at|with|of)\s+([A-Z][A-Za-z0-9&.\-]*(?:\s+[A-Z][A-Za-z0-9&.\-]*){0,3})")


def _clip_org_at_sentence_end(raw):
    for sep in (". ", ".\n", "\n"):
        i = raw.find(sep)
        if i != -1:
            raw = raw[:i]
            break
    return raw.rstrip(". ").strip()


# --------------------------------------------------------------------------
# Schedule loading / dedup / Main Stage ordering
# --------------------------------------------------------------------------

def load_dedup_sessions():
    sessions = json.load(open(SESSIONS))["sessions"]
    seen = {}
    order = []
    dupes_removed = 0
    for s in sessions:
        key = (s["title"].strip().lower(), tuple(sorted(sp.strip().lower() for sp in (s.get("speakers") or []))))
        if key in seen:
            dupes_removed += 1
            continue
        seen[key] = s
        order.append(s)
    return order, dupes_removed


def build_mainstage_order(sessions, day):
    ms = [s for s in sessions if s.get("day") == day and s.get("room") == "Main Stage"]
    ms_sorted = sorted(ms, key=lambda x: parse_time_start(x["time"]))
    for i, s in enumerate(ms_sorted):
        s["schedule_index"] = i
    return ms_sorted


# --------------------------------------------------------------------------
# Anchor matching: Phase-1 covered spans -> Main Stage schedule entries
# --------------------------------------------------------------------------

def find_anchors(covered_spans, idx_by_slug, mainstage_list):
    ms_names = []
    for s in mainstage_list:
        names = [norm_name(sp) for sp in (s.get("speakers") or [])]
        ms_names.append(names)

    raw_anchors = []
    for sp in covered_spans:
        r = idx_by_slug.get(sp["slug"], {})
        speakers = r.get("speakers") or []
        found = None
        for spk in speakers:
            for part in split_speaker_field(spk):
                nk = norm_name(part)
                if not nk or len(nk.split()) < 2:
                    continue
                for i, names in enumerate(ms_names):
                    if nk in names:
                        found = (i, mainstage_list[i], part)
                        break
                if found:
                    break
            if found:
                break
        if found:
            si, session, matched_name = found
            raw_anchors.append({
                "slug": sp["slug"], "word_start": sp["word_start"], "word_end": sp["word_end"],
                "schedule_index": si, "session_title": session["title"],
                "matched_speaker": matched_name,
            })

    raw_anchors.sort(key=lambda a: a["word_start"])

    # LIS over schedule_index (protects the order assumption against a
    # stray false-positive name match producing a non-monotonic anchor)
    n = len(raw_anchors)
    if n == 0:
        return [], []
    lengths = [1] * n
    prevs = [-1] * n
    for i in range(n):
        for j in range(i):
            if raw_anchors[j]["schedule_index"] < raw_anchors[i]["schedule_index"] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prevs[i] = j
    best_end = max(range(n), key=lambda i: lengths[i])
    chain_idx = set()
    i = best_end
    while i != -1:
        chain_idx.add(i)
        i = prevs[i]
    kept = [raw_anchors[i] for i in sorted(chain_idx)]
    dropped = [raw_anchors[i] for i in range(n) if i not in chain_idx]
    return kept, dropped


def build_speaker_org_lookup(idx_records):
    """speaker (normalized) -> org, but ONLY when every corpus talk by that
    speaker agrees on the org (same conflict-avoidance rule as
    segment_livestreams.infer_org, applied globally instead of per-gap)."""
    by_speaker = {}
    conflicted = set()
    for r in idx_records:
        org = r.get("org")
        if not org:
            continue
        for sp in (r.get("speakers") or []):
            key = norm_name(sp)
            if not key:
                continue
            if key in by_speaker and by_speaker[key] != org:
                conflicted.add(key)
            else:
                by_speaker[key] = org
    return {k: v for k, v in by_speaker.items() if k not in conflicted}


# --------------------------------------------------------------------------
# Evidence scoring
# --------------------------------------------------------------------------

W_FULL_NAME = 10
W_SURNAME = 7
W_TITLE_PHRASE_BASE = 8
W_ORG_BONUS = 3
W_MC_BONUS = 4


def find_all_word_positions(norm_words, phrase_words):
    """Return sorted list of word-index positions where phrase_words occurs
    as a contiguous run inside norm_words."""
    n, m = len(norm_words), len(phrase_words)
    if m == 0 or m > n:
        return []
    out = []
    first = phrase_words[0]
    for i in range(n - m + 1):
        if norm_words[i] != first:
            continue
        if norm_words[i:i + m] == phrase_words:
            out.append(i)
    return out


def score_candidate(session, norm_words, all_surnames_counter, org_lookup=None):
    """norm_words: normalized word list of ONE gap's text.
    Returns None if no strong signal found, else a dict with position,
    score, and a list of (type, detail, position) signals."""
    org_lookup = org_lookup or {}
    signals = []  # (type, weight, position, detail)

    speakers = session.get("speakers") or []
    # 1. full name adjacent (try natural order and reversed order, since
    #    ASR / title-derived speaker strings occasionally invert)
    for sp in speakers:
        toks = norm_name(sp).split()
        if len(toks) < 2:
            continue
        variants = {tuple(toks), (toks[0], toks[-1]), (toks[-1], toks[0])}
        for variant in variants:
            positions = find_all_word_positions(norm_words, list(variant))
            for pos in positions:
                signals.append(("full_name", W_FULL_NAME, pos, " ".join(variant)))

    # 2. distinctive surname (>=5 chars, unique across all 561 speakers,
    #    not a common-word false-positive)
    for sp in speakers:
        toks = norm_name(sp).split()
        if not toks:
            continue
        last = toks[-1]
        if len(last) >= 5 and all_surnames_counter.get(last, 0) == 1 and last not in COMMON_SURNAME_STOP:
            positions = find_all_word_positions(norm_words, [last])
            for pos in positions:
                signals.append(("surname", W_SURNAME, pos, last))

    # 3. distinctive title phrase (3+ consecutive content words)
    for run in title_phrase_candidates(session.get("title", "")):
        positions = find_all_word_positions(norm_words, run)
        weight = W_TITLE_PHRASE_BASE + max(0, len(run) - 3)
        for pos in positions:
            signals.append(("title_phrase", weight, pos, " ".join(run)))

    strong = [s for s in signals if s[0] in ("full_name", "surname", "title_phrase")]
    if not strong:
        return None

    # earliest strong hit anchors the segment boundary (that's where the
    # introduction / topic-establishing language happens)
    strong.sort(key=lambda s: s[2])
    best_pos = strong[0][2]

    # dedupe: take the max-weight signal per type for the score total
    by_type = {}
    for typ, w, pos, detail in signals:
        if typ not in by_type or w > by_type[typ][0]:
            by_type[typ] = (w, pos, detail)
    total = sum(w for w, _, _ in by_type.values())

    # 4. MC introduction pattern within +-150 words of the best strong hit
    window_lo = max(0, best_pos - 150)
    window_hi = min(len(norm_words), best_pos + 150)
    window_text = " ".join(norm_words[window_lo:window_hi])
    mc_hit = None
    for patt in MC_PATTERNS:
        if patt in window_text:
            mc_hit = patt
            break
    if mc_hit:
        total += W_MC_BONUS
        by_type["mc_pattern"] = (W_MC_BONUS, best_pos, mc_hit)

    # 5. org name near the name hit (only meaningful next to an actual name
    #    signal, so only checked when a full_name or surname hit exists)
    if "full_name" in by_type or "surname" in by_type:
        org_window_lo = max(0, best_pos - 100)
        org_window_hi = min(len(norm_words), best_pos + 100)
        org_window = norm_words[org_window_lo:org_window_hi]
        for sp in speakers:
            org = org_lookup.get(norm_name(sp))
            if not org:
                continue
            org_toks = [t for t in norm_name(org).split() if len(t) >= 4]
            for t in org_toks:
                if t in org_window:
                    total += W_ORG_BONUS
                    by_type["org_proximity"] = (W_ORG_BONUS, best_pos, f"{org!r} near name")
                    break
            if "org_proximity" in by_type:
                break

    snippet_lo = max(0, best_pos - 8)
    snippet_hi = min(len(norm_words), best_pos + 12)
    snippet = " ".join(norm_words[snippet_lo:snippet_hi])

    return {
        "position": best_pos, "score": total,
        "signals": [{"type": t, "weight": w, "position": p, "detail": d}
                     for t, (w, p, d) in by_type.items()],
        "snippet": snippet,
    }


# --------------------------------------------------------------------------
# Per-bracket candidate search + monotonic DP assignment
# --------------------------------------------------------------------------

def dp_select(items):
    """items: list of dicts with 'global_pos' and 'score', already sorted by
    schedule_index ascending. Choose the subsequence with strictly increasing
    global_pos that maximizes total score (order + position both must
    increase together)."""
    n = len(items)
    if n == 0:
        return []
    best = [items[i]["score"] for i in range(n)]
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if items[j]["global_pos"] < items[i]["global_pos"] and best[j] + items[i]["score"] > best[i]:
                best[i] = best[j] + items[i]["score"]
                prev[i] = j
    i_star = max(range(n), key=lambda i: best[i])
    chain = []
    i = i_star
    while i != -1:
        chain.append(items[i])
        i = prev[i]
    chain.reverse()
    return chain


def process_stream(sslug, sdata, mainstage_list, idx_by_slug, used_sessions, log):
    covered_spans = sdata["covered_spans"]
    gap_spans = sdata["gap_spans"]
    raw_text = sdata["raw_text"]

    anchors, dropped_anchors = find_anchors(covered_spans, idx_by_slug, mainstage_list)
    for d in dropped_anchors:
        log(f"  [anchor DROPPED -- broke order monotonicity] {d['slug']} "
            f"-> schedule_index {d['schedule_index']} {d['session_title']!r}")
    for a in anchors:
        log(f"  [anchor] {a['slug']:50s} word[{a['word_start']},{a['word_end']}] "
            f"-> schedule_index {a['schedule_index']:2d} {a['session_title']!r} "
            f"(matched speaker {a['matched_speaker']!r})")

    n_ms = len(mainstage_list)
    # brackets: (lo_index_exclusive, hi_index_exclusive, lo_word, hi_word)
    brackets = []
    if anchors:
        first = anchors[0]
        if first["schedule_index"] > 0:
            brackets.append((-1, first["schedule_index"], 0, first["word_start"]))
        for a, b in zip(anchors, anchors[1:]):
            if b["schedule_index"] - a["schedule_index"] > 1:
                brackets.append((a["schedule_index"], b["schedule_index"], a["word_end"], b["word_start"]))
        last = anchors[-1]
        if last["schedule_index"] < n_ms - 1:
            brackets.append((last["schedule_index"], n_ms, last["word_end"], sdata["live_len"]))
    else:
        brackets.append((-1, n_ms, 0, sdata["live_len"]))

    all_surnames_counter = sdata["surname_counter"]
    org_lookup = sdata["org_lookup"]

    assigned_segments = []
    discarded = []  # (word_start, word_end, reason)
    candidate_log = []  # for reporting: all candidates tried, whether assigned

    chunks, starts = sdata["chunks"], sdata["starts"]
    video_id = sdata["video_id"]

    for lo_i, hi_i, lo_w, hi_w in brackets:
        cand_sessions = [s for s in mainstage_list if lo_i < s["schedule_index"] < hi_i]
        bracket_gaps = [g for g in gap_spans if g["word_start"] >= lo_w and g["word_end"] <= hi_w]
        if not cand_sessions:
            for g in bracket_gaps:
                discarded.append((g["word_start"], g["word_end"], "no schedule candidates in this bracket"))
            continue
        if not bracket_gaps:
            # candidates exist by schedule order but no unidentified text
            # remains between the anchors (fully consumed by already-known
            # covered spans) -- nothing to search, nothing to assign.
            for s in cand_sessions:
                candidate_log.append({"session": s, "hit": None, "reason": "no gap text in bracket"})
            continue

        # cache normalized words per gap
        gap_words_cache = {}
        for g in bracket_gaps:
            gap_words_cache[g["gap_id"]] = normalize_words(raw_text[g["_char_start"]:g["_char_end"]])

        items = []
        for s in cand_sessions:
            sess_key = (s["title"].strip().lower(),
                        tuple(sorted(sp.strip().lower() for sp in (s.get("speakers") or []))))
            if sess_key in used_sessions:
                candidate_log.append({"session": s, "hit": None, "reason": "already used elsewhere (global one-use)"})
                continue
            best_hit = None
            best_gap = None
            for g in bracket_gaps:
                nw = gap_words_cache[g["gap_id"]]
                hit = score_candidate(s, nw, all_surnames_counter, org_lookup)
                if hit is None:
                    continue
                global_pos = g["word_start"] + hit["position"]
                if best_hit is None or global_pos < best_hit["global_pos"]:
                    hit["global_pos"] = global_pos
                    best_hit = hit
                    best_gap = g
            if best_hit is None:
                candidate_log.append({"session": s, "hit": None, "reason": "no strong evidence found"})
                continue
            items.append({
                "schedule_index": s["schedule_index"], "session": s,
                "gap": best_gap, "global_pos": best_hit["global_pos"],
                "local_pos": best_hit["position"], "score": best_hit["score"],
                "signals": best_hit["signals"], "snippet": best_hit["snippet"],
                "sess_key": sess_key,
            })

        items.sort(key=lambda it: it["schedule_index"])
        chain = dp_select(items)
        chosen_keys = {it["sess_key"] for it in chain}
        for it in items:
            if it["sess_key"] not in chosen_keys:
                candidate_log.append({
                    "session": it["session"], "hit": it,
                    "reason": "evidence found but dropped by monotonic DP (order/position conflict)",
                })
        for it in chain:
            candidate_log.append({"session": it["session"], "hit": it, "reason": "ASSIGNED"})
            used_sessions.add(it["sess_key"])

        # group chosen chain items by gap, build segment boundaries
        by_gap = {}
        for it in chain:
            by_gap.setdefault(it["gap"]["gap_id"], []).append(it)

        for g in bracket_gaps:
            hits_here = sorted(by_gap.get(g["gap_id"], []), key=lambda it: it["local_pos"])
            if not hits_here:
                discarded.append((g["word_start"], g["word_end"], "no assigned candidate hit in this gap"))
                continue
            # lead-in before first hit
            if hits_here[0]["local_pos"] > 0:
                lead_end = g["word_start"] + hits_here[0]["local_pos"]
                if lead_end > g["word_start"]:
                    discarded.append((g["word_start"], lead_end, "text before first evidence hit in this gap (unidentified -- may be MC banter, a transition, or off-schedule/cross-stream content)"))
            for k, it in enumerate(hits_here):
                seg_start = it["global_pos"]
                seg_end = hits_here[k + 1]["global_pos"] if k + 1 < len(hits_here) else g["word_end"]
                word_count = seg_end - seg_start
                if word_count < MIN_SEGMENT_WORDS:
                    discarded.append((seg_start, seg_end, f"segment under {MIN_SEGMENT_WORDS} words ({word_count}w)"))
                    continue
                start_sec = seconds_for_word_index(seg_start, chunks, starts)
                end_sec = seconds_for_word_index(max(seg_start, seg_end - 1), chunks, starts)
                assigned_segments.append({
                    "stream": sslug, "video_id": video_id,
                    "session_title": it["session"]["title"],
                    "speakers": it["session"].get("speakers") or [],
                    "schedule_index": it["schedule_index"],
                    "schedule_time": it["session"]["time"],
                    "word_start": seg_start, "word_end": seg_end, "word_count": word_count,
                    "start_sec": start_sec, "end_sec": end_sec,
                    "deep_link": f"https://www.youtube.com/watch?v={video_id}&t={start_sec}s",
                    "evidence_score": it["score"], "signals": it["signals"], "snippet": it["snippet"],
                    "gap_id": it["gap"]["gap_id"],
                })

    return anchors, dropped_anchors, assigned_segments, discarded, candidate_log


# --------------------------------------------------------------------------
# Markdown writer
# --------------------------------------------------------------------------

def slugify(title):
    s = norm_name(title)
    s = re.sub(r"\s+", "-", s.strip())
    return s[:80] or "segment"


def write_segment_md(seg, raw_text, chunks, starts, idx):
    ws, we = seg["word_start"], seg["word_end"]
    start_chunk = chunk_for_word_index(ws, chunks, starts)
    end_chunk = chunk_for_word_index(max(ws, we - 1), chunks, starts)
    char_start, char_end = start_chunk["char_start"], end_chunk["char_end"]
    body_text = raw_text[char_start:char_end].strip()

    dur = max(0, seg["end_sec"] - seg["start_sec"])
    dur_h, rem = divmod(dur, 3600)
    dur_m, dur_s = divmod(rem, 60)
    dur_str = f"{dur_h}:{dur_m:02d}:{dur_s:02d}" if dur_h else f"{dur_m}:{dur_s:02d}"

    slug = slugify(seg["session_title"])
    base_slug = slug
    n = 2
    while slug in idx:
        slug = f"{base_slug}-{n}"
        n += 1
    idx.add(slug)

    fm = {
        "title": seg["session_title"],
        "speakers": seg["speakers"],
        "org": "",
        "track": STREAM_TRACK.get(seg["stream"], ""),
        "video_id": seg["video_id"],
        "url": seg["deep_link"],
        "word_range": [ws, we],
        "word_count": seg["word_count"],
        "time_range_sec": [seg["start_sec"], seg["end_sec"]],
        "duration_sec": dur,
        "scheduled_time": seg["schedule_time"],
        "evidence_score": seg["evidence_score"],
        "evidence_signals": seg["signals"],
        "source_stream": seg["stream"],
        "gap_id": seg["gap_id"],
    }
    fm_lines = ["---"]
    for k, v in fm.items():
        fm_lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    fm_lines.append("---")
    frontmatter = "\n".join(fm_lines)

    speaker_line = ", ".join(seg["speakers"]) if seg["speakers"] else ""
    out = (
        f"{frontmatter}\n\n"
        f"# {seg['session_title']}\n\n"
        + (f"**{speaker_line}**\n\n" if speaker_line else "")
        + f"[Watch on YouTube]({seg['deep_link']}) &middot; {dur_str} &middot; scheduled {seg['schedule_time']}\n\n"
        f"## Transcript\n\n"
        f"{body_text}\n"
    )
    out_path = os.path.join(OUTDIR, f"{slug}.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return slug, out_path


STREAM_TRACK = {
    "wf2026-software-factories-keynotes-ft-microsoft-openai-openclaw-zai-glm-minimax": "Software Factories",
    "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena": "Autoresearch",
}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report-only", action="store_true", help="don't write manifest/markdown, just print the report")
    args = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)

    idx = json.load(open(INDEX))
    idx_by_slug = {r["slug"]: r for r in idx}

    all_sessions_raw = json.load(open(SESSIONS))["sessions"]
    dedup_sessions, dupes_removed = load_dedup_sessions()
    log(f"Schedule: {len(all_sessions_raw)} raw sessions -> {len(dedup_sessions)} after dedup "
        f"({dupes_removed} exact (title,speakers) duplicates removed)")

    manifest = json.load(open(MANIFEST))

    # surname frequency across ALL 561 (deduped) speakers, for distinctiveness
    all_surnames_counter = Counter()
    for s in dedup_sessions:
        for sp in (s.get("speakers") or []):
            toks = norm_name(sp).split()
            if toks:
                all_surnames_counter[toks[-1]] += 1

    org_lookup = build_speaker_org_lookup(idx)
    log(f"Speaker->org lookup: {len(org_lookup)} speakers with a consistent org across their corpus talk(s)")

    used_sessions = set()
    report = {}

    for sslug in LIVESTREAM_SLUGS:
        day = STREAM_DAY[sslug]
        mainstage_list = build_mainstage_order(dedup_sessions, day)
        log(f"\n=== {sslug} (day={day!r}) ===")
        log(f"Main Stage sessions on this day after dedup: {len(mainstage_list)}")
        for s in mainstage_list:
            log(f"  idx {s['schedule_index']:2d}  {s['time']:16s}  {s['title']!r}  {s.get('speakers')}")

        v = manifest["streams"][sslug]
        rec = idx_by_slug[sslug]
        path = os.path.join(TRANSCRIPTS, f"{sslug}.md")
        raw_text = open(path, encoding="utf-8").read()
        chunks, live_len = build_chunks(raw_text)
        starts = [c["word_start"] for c in chunks]

        sdata = {
            "covered_spans": v["covered_spans"], "gap_spans": v["gap_spans"],
            "raw_text": raw_text, "chunks": chunks, "starts": starts,
            "live_len": live_len, "video_id": v["video_id"],
            "surname_counter": all_surnames_counter, "org_lookup": org_lookup,
        }

        anchors, dropped_anchors, assigned_segments, discarded, candidate_log = process_stream(
            sslug, sdata, mainstage_list, idx_by_slug, used_sessions, log)

        report[sslug] = {
            "mainstage_count": len(mainstage_list),
            "anchors": anchors, "dropped_anchors": dropped_anchors,
            "assigned_segments": assigned_segments, "discarded": discarded,
            "candidate_log": candidate_log,
            "chunks": chunks, "starts": starts, "raw_text": raw_text,
        }

    # ---------------- report ----------------
    print("\n" + "=" * 78)
    print("VERIFICATION REPORT")
    print("=" * 78)

    total_assigned_words = 0
    total_discarded_words = 0
    all_slugs_written = set()
    written_files = []

    for sslug in LIVESTREAM_SLUGS:
        r = report[sslug]
        print(f"\n--- {sslug} ---")
        print(f"Main Stage sessions (this day, deduped): {r['mainstage_count']}")
        print(f"Anchors matched: {len(r['anchors'])} (dropped for order violation: {len(r['dropped_anchors'])})")
        print(f"Assigned segments: {len(r['assigned_segments'])}")
        for seg in sorted(r["assigned_segments"], key=lambda s: s["word_start"]):
            sig_str = "; ".join(f"{s['type']}={s['detail']!r}(w{s['weight']})" for s in seg["signals"])
            print(f"  [{seg['word_start']:6d},{seg['word_end']:6d}] {seg['word_count']:5d}w "
                  f"sched_idx={seg['schedule_index']:2d} @ {seg['schedule_time']}")
            print(f"    title: {seg['session_title']!r}  speakers: {seg['speakers']}")
            print(f"    evidence (score={seg['evidence_score']}): {sig_str}")
            print(f"    snippet: ...{seg['snippet']}...")
            total_assigned_words += seg["word_count"]

        disc_words = sum(e - s for s, e, _ in r["discarded"])
        total_discarded_words += disc_words
        print(f"Discarded/unidentified spans: {len(r['discarded'])}, {disc_words} words total")
        for s, e, reason in sorted(r["discarded"], key=lambda x: x[0]):
            print(f"  [{s:6d},{e:6d}] {e - s:5d}w  {reason}")

        print("Candidates NOT assigned (with reason):")
        for c in r["candidate_log"]:
            if c["reason"] == "ASSIGNED":
                continue
            s = c["session"]
            extra = f" (had evidence score={c['hit']['score']})" if c.get("hit") else ""
            print(f"  idx {s['schedule_index']:2d} {s['title']!r} {s.get('speakers')}: {c['reason']}{extra}")

    # duplicate-assignment check
    seen_keys = Counter()
    for sslug in LIVESTREAM_SLUGS:
        for seg in report[sslug]["assigned_segments"]:
            key = (seg["session_title"].strip().lower(), tuple(sorted(sp.lower() for sp in seg["speakers"])))
            seen_keys[key] += 1
    dupes = {k: v for k, v in seen_keys.items() if v > 1}
    print(f"\nGlobal one-use check: {len(seen_keys)} distinct sessions assigned, "
          f"{len(dupes)} assigned more than once (should be 0)")
    for k, v in dupes.items():
        print(f"  DUPLICATE: {k} assigned {v} times")

    print(f"\nTOTAL assigned words: {total_assigned_words}")
    print(f"TOTAL discarded/unidentified words: {total_discarded_words}")

    if args.report_only:
        return

    # ---------------- write markdown + manifest ----------------
    for sslug in LIVESTREAM_SLUGS:
        r = report[sslug]
        for seg in r["assigned_segments"]:
            slug, path = write_segment_md(seg, r["raw_text"], r["chunks"], r["starts"], all_slugs_written)
            seg["output_slug"] = slug
            seg["output_path"] = os.path.relpath(path, ROOT)
            written_files.append(path)
        manifest["streams"][sslug]["phase3_order_evidence"] = {
            "mainstage_count": r["mainstage_count"],
            "anchors": [{k: v for k, v in a.items()} for a in r["anchors"]],
            "dropped_anchors": r["dropped_anchors"],
            "assigned_segments": [{k: v for k, v in s.items() if k != "gap"} for s in r["assigned_segments"]],
            "discarded": [{"word_start": s, "word_end": e, "reason": reason} for s, e, reason in r["discarded"]],
        }

    manifest.pop("phase3_resegmentation", None)
    for sslug in LIVESTREAM_SLUGS:
        manifest["streams"][sslug].pop("gap_spans_resegmented", None)
        manifest["streams"][sslug].pop("time_map", None)

    manifest["generated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
    log(f"\nWrote manifest: {MANIFEST}")
    log(f"Wrote {len(written_files)} segment markdown files to {OUTDIR}")


if __name__ == "__main__":
    main()
