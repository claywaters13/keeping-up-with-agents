#!/usr/bin/env python3
"""Turn raw yt-dlp captions + metadata into timestamped markdown + an index.

Adapted from events/aiewf-2026/scripts/normalize.py. Two differences:

1. **Title parser.** AIEWF's channel uses "Talk Title <dash> Speaker, Org" (speaker
   LAST). Y Combinator uses "Speaker Name: Talk Title" (speaker FIRST, colon), with
   two variants: a role/org prefix on the speaker ("Waymo Co-CEO Dmitri Dolgov: ...")
   and a quoted talk title (Sam Altman: "Never a Better Time to Do a Startup").
   With only 14 titles every parse was hand-verified; corrections live in
   raw/title_overrides.json and win over the parser.

2. **No schedule join, no track playlists.** Startup School 2026 is a single-track
   event with one official playlist, so `track` is always "" and `playlists` is
   always that one playlist. There is no join_schedule.py / playlist_tracks.py
   enrichment to re-apply after regenerating index.json.

The caption glue fix from AIEWF is preserved verbatim (`if txt:`, not
`if txt.strip():`) -- see events/aiewf-2026/BUILD.md.
"""
import json, os, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAPS = ROOT / "raw" / "caps"
OUT = ROOT / "data" / "transcripts"
OUT.mkdir(parents=True, exist_ok=True)

OVERRIDES_PATH = ROOT / "raw" / "title_overrides.json"

PLAYLIST = "Startup School 2026"

# Role words that can appear in an "<Org> <Role> <Name>:" prefix. Anything at or
# before the last role word is org/role, not the person's name.
ROLE_WORDS = (
    r"co-?ceo|ceo|cto|coo|cfo|co-?founder|cofounder|founder|president|chair(?:man)?|"
    r"chief\s+\w+(?:\s+officer)?|director|head\s+of\s+\w+|partner|vp|professor|"
    r"creator|inventor|designer"
)
ROLE_PREFIX_RE = re.compile(rf"^(?P<pre>.*\b(?:{ROLE_WORDS}))\s+(?P<name>.+)$", re.IGNORECASE)

# Straight and curly quote pairs wrapping a whole talk title.
QUOTED_RE = re.compile("^[“\"‘'](?P<inner>.+)[”\"’']$")


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:80].strip("-")


def parse_title(raw: str):
    """'Speaker Name: Talk Title' -> (title, [speakers], org).

    Splits on the FIRST colon: the speaker leads, so a colon inside the talk
    title must not win. Falls back to (raw, [], "") when there is no colon.
    """
    if ":" not in raw:
        return raw.strip(), [], ""
    head, tail = raw.split(":", 1)
    head, title = head.strip(), tail.strip()

    m = QUOTED_RE.match(title)
    if m:
        title = m.group("inner").strip()

    if not head or not title:
        return raw.strip(), [], ""

    org = ""
    m = ROLE_PREFIX_RE.match(head)
    if m:
        name = m.group("name").strip()
        pre = m.group("pre").strip()
        # Only accept the split if what's left still looks like a person's name
        # (2-4 tokens). Guards against eating a genuine multi-word name.
        if 2 <= len(name.split()) <= 4:
            head = name
            # org = the prefix minus its trailing role words
            org = re.sub(rf"\s*\b(?:{ROLE_WORDS})\b\s*$", "", pre, flags=re.IGNORECASE).strip()

    return title, [head], org


def caption_text(path: Path):
    """json3 -> list of (start_seconds, text) paragraph blocks."""
    data = json.loads(path.read_text())
    words = []
    for ev in data.get("events", []):
        t = ev.get("tStartMs", 0) / 1000.0
        for seg in ev.get("segs", []) or []:
            txt = seg.get("utf8", "")
            # Keep whitespace-only segs: YouTube emits each caption line break as its
            # own "\n" seg, and that seg IS the word separator. Dropping it welds the
            # last word of each line onto the first word of the next ("moretools").
            if txt:
                words.append((t, txt))
    if not words:
        return []
    paras, buf, start, count = [], [], words[0][0], 0
    for t, w in words:
        buf.append(w)
        count += len(w.split())
        # break on sentence end once the block is substantial
        if count >= 110 and w.strip().endswith((".", "?", "!")):
            paras.append((start, "".join(buf)))
            buf, count, start = [], 0, t
    if buf:
        paras.append((start, "".join(buf)))
    return [(s, " ".join(p.split())) for s, p in paras if p.strip()]


def hhmmss(sec: float) -> str:
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


overrides = {}
if OVERRIDES_PATH.exists():
    overrides = json.loads(OVERRIDES_PATH.read_text())

records = {}
overridden = []
for info_path in sorted(CAPS.glob("*.info.json")):
    vid = info_path.name.replace(".info.json", "")
    cap_path = CAPS / f"{vid}.en.json3"
    if not cap_path.exists():
        continue
    info = json.loads(info_path.read_text())
    raw_title = info.get("title", "")
    title, speakers, org = parse_title(raw_title)

    # Hand-verified corrections win over the parser.
    ov = overrides.get(vid)
    if ov:
        title = ov.get("title", title)
        speakers = ov.get("speakers", speakers)
        org = ov.get("org", org)
        overridden.append(vid)

    slug = slugify(title) or vid
    paras = caption_text(cap_path)
    if not paras:
        continue
    words = sum(len(p.split()) for _, p in paras)
    url = f"https://www.youtube.com/watch?v={vid}"

    fm = {
        "title": title,
        "speakers": speakers,
        "org": org,
        "track": "",              # single-track event
        "playlists": [PLAYLIST],
        "video_id": vid,
        "url": url,
        "duration_sec": info.get("duration"),
        "upload_date": info.get("upload_date"),
        "word_count": words,
        "raw_title": raw_title,
    }
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines += ["---", "", f"# {title}", ""]
    if speakers:
        lines.append(f"**{', '.join(speakers)}**" + (f" &middot; {org}" if org else ""))
        lines.append("")
    lines.append(f"[Watch on YouTube]({url}) &middot; {hhmmss(info.get('duration') or 0)}")
    lines += ["", "## Transcript", ""]
    for start, text in paras:
        lines.append(f"**[{hhmmss(start)}]({url}&t={int(start)}s)** {text}")
        lines.append("")

    rec = {**fm, "slug": slug, "paragraphs": len(paras)}
    # Re-uploads and cross-playlist dupes collide on slug; keep the fullest copy.
    prior = records.get(slug)
    if prior and prior[0]["word_count"] >= words:
        continue
    records[slug] = (rec, "\n".join(lines))

for slug, (rec, body) in records.items():
    (OUT / f"{slug}.md").write_text(body)
index = [rec for rec, _ in records.values()]
index.sort(key=lambda r: r["title"].lower())
(ROOT / "data" / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False))

total_words = sum(r["word_count"] for r in index)
total_hours = sum((r["duration_sec"] or 0) for r in index) / 3600
print(f"talks:      {len(index)}")
print(f"words:      {total_words:,}")
print(f"hours:      {total_hours:.1f}")
print(f"est tokens: {int(total_words*1.35):,}")
print(f"no speaker parsed: {sum(1 for r in index if not r['speakers'])}")
print(f"title overrides applied: {len(overridden)} {overridden}")
print()
print("--- parsed titles (hand-verify all of these) ---")
for r in index:
    print(f"  {r['video_id']}  speakers={r['speakers']!r:<26} org={r['org']!r:<12} title={r['title']!r}")
