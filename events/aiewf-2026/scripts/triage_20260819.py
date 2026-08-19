#!/usr/bin/env python3
"""One-off triage for the 2026-08-19 corpus refresh.

Classifies every candidate video (raw/cand_meta_20260819.txt) into:
  ACCEPT      — in an official 2026 main playlist, uploaded 2026, plausible talk
  TRACK-ONLY  — 2026 upload, only in topical playlists; needs schedule cross-check
  LIVESTREAM  — full-day livestream compilations (excluded by design)
  REJECT      — pre-2026 upload date or other-event playlist membership
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
pl = json.load(open(ROOT / "raw" / "all_playlists.json"))
have = {r["video_id"] for r in json.load(open(ROOT / "data" / "index.json"))}

MAIN = {"AIE World's Fair 2026 Complete Playlist",
        "AI Engineer World's Fair Online Track 2026",
        "Generative Media: AI Engineer World's Fair 2026"}
OTHER_EVENT = re.compile(r"europe|code 20|world's fair 2024|world's fair 2025|"
                         r"summit|2023|2024|: ai engineer world's fair 2025", re.I)

vid2pl = {}
for name, vids in pl.items():
    for v in vids:
        vid2pl.setdefault(v, []).append(name)

sched = json.load(open(ROOT / "raw" / "sessions.json"))["sessions"]
sched_titles = " ||| ".join((s.get("title") or "").lower() for s in sched)

rows = []
for line in open(ROOT / "raw" / "cand_meta_20260819.txt"):
    line = line.strip()
    if not line or "|" not in line:
        continue
    vid, up, dur, title = line.split("|", 3)
    if vid in have:
        continue
    pls = vid2pl.get(vid, [])
    in_main = bool(set(pls) & MAIN)
    in_other = any(OTHER_EVENT.search(p) for p in pls)
    is_2026 = up.startswith("2026")
    is_livestream = bool(re.search(r"livestream|day [12].*(track|stage)|full day", title, re.I)) \
        or (dur.isdigit() and int(dur) > 14400)
    if not is_2026 or (in_other and not in_main):
        cls = "REJECT"
    elif is_livestream:
        cls = "LIVESTREAM"
    elif in_main:
        cls = "ACCEPT"
    else:
        cls = "TRACK-ONLY"
    rows.append((cls, vid, up, dur, title, ";".join(pls)))

order = {"ACCEPT": 0, "TRACK-ONLY": 1, "LIVESTREAM": 2, "REJECT": 3}
rows.sort(key=lambda r: (order[r[0]], r[2]))
for cls, vid, up, dur, title, pls in rows:
    print(f"{cls:10s} {vid} {up} {int(dur) if dur.isdigit() else '?':>5}s  {title}")
    if cls == "TRACK-ONLY":
        print(f"{'':10s}   playlists: {pls}")
from collections import Counter
print("\n", Counter(r[0] for r in rows))
