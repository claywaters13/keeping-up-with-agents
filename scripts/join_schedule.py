#!/usr/bin/env python3
"""Join harvested YouTube talks to the official 561-session schedule.

Adds track / speakers / abstract to index.json. Matching is fuzzy because
YouTube titles are lightly edited versions of the scheduled titles.
"""
import json, re, unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
idx = json.loads((ROOT / "data" / "index.json").read_text())
sched = json.loads((ROOT / "raw" / "sessions.json").read_text())["sessions"]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return " ".join(s.split())


def score(a: str, b: str) -> float:
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    base = SequenceMatcher(None, na, nb).ratio()
    ta, tb = set(na.split()), set(nb.split())
    jac = len(ta & tb) / len(ta | tb) if ta | tb else 0
    # containment rewards YouTube titles that truncate or extend the scheduled one
    cont = len(ta & tb) / min(len(ta), len(tb)) if ta and tb else 0
    return max(base, jac, cont * 0.95)


matched = unmatched = 0
for rec in idx:
    best, best_s = None, 0.0
    for s in sched:
        v = score(rec["title"], s.get("title", ""))
        if v > best_s:
            best, best_s = s, v
    if best and best_s >= 0.62:
        rec["track"] = best.get("track") or ""
        rec["session_type"] = best.get("type") or ""
        rec["day"] = best.get("day") or ""
        rec["room"] = best.get("room") or ""
        rec["abstract"] = (best.get("description") or "").strip()
        sched_speakers = best.get("speakers") or []
        if sched_speakers:
            rec["speakers"] = sched_speakers
        rec["match_score"] = round(best_s, 3)
        rec["scheduled_title"] = best.get("title")
        matched += 1
    else:
        rec.setdefault("track", "")
        rec.setdefault("abstract", "")
        rec["match_score"] = round(best_s, 3)
        unmatched += 1

(ROOT / "data" / "index.json").write_text(json.dumps(idx, indent=2, ensure_ascii=False))

tracks = {}
for r in idx:
    tracks[r.get("track") or "(unmatched)"] = tracks.get(r.get("track") or "(unmatched)", 0) + 1

print(f"matched:   {matched}/{len(idx)}")
print(f"unmatched: {unmatched}")
print(f"no speakers: {sum(1 for r in idx if not r['speakers'])}")
print(f"\ntracks ({len(tracks)}):")
for t, c in sorted(tracks.items(), key=lambda x: -x[1]):
    print(f"  {c:3d}  {t}")
