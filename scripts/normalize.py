#!/usr/bin/env python3
"""Turn raw yt-dlp captions + metadata into timestamped markdown + an index."""
import json, os, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAPS = ROOT / "raw" / "caps"
OUT = ROOT / "data" / "transcripts"
OUT.mkdir(parents=True, exist_ok=True)

# The channel is inconsistent: em dash, en dash, and spaced hyphen all appear
# as the "Title <sep> Speaker, Org" separator.
SEPS = (" — ", " – ", " - ")


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:80].strip("-")


def parse_title(raw: str):
    """'Talk Title <sep> Speaker, Org' -> (title, [speakers], org). Tolerant of panels."""
    # Prefer the last separator that leaves a plausible speaker tail (short, no
    # trailing period) so titles containing their own dashes survive intact.
    best = None
    for sep in SEPS:
        if sep in raw:
            head, tail = raw.rsplit(sep, 1)
            tail = tail.strip()
            if head.strip() and 0 < len(tail.split()) <= 12:
                if best is None or len(head) > len(best[0]):
                    best = (head.strip(), tail)
    if not best:
        return raw.strip(), [], ""
    title, tail = best
    parts = [p.strip() for p in tail.split(",")]
    if len(parts) >= 2:
        return title, [parts[0]], ", ".join(parts[1:])
    return title, [tail], ""


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


records = {}
for info_path in sorted(CAPS.glob("*.info.json")):
    vid = info_path.name.replace(".info.json", "")
    cap_path = CAPS / f"{vid}.en.json3"
    if not cap_path.exists():
        continue
    info = json.loads(info_path.read_text())
    raw_title = info.get("title", "")
    title, speakers, org = parse_title(raw_title)
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
