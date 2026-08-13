#!/usr/bin/env python3
"""Find AIEWF 2026 talks that live only in topical track playlists.

The two main 2026 playlists (Complete + Online Track) miss talks that were
filed only under a track or sponsor playlist. Those playlists are cross-year,
so we exclude anything that also appears in a Europe / CODE / 2025 playlist.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YTDLP = "/tmp/ytdlp-env/bin/yt-dlp"
CACHE = ROOT / "raw" / "all_playlists.json"

have = {r["video_id"] for r in json.loads((ROOT / "data" / "index.json").read_text())}


def run(args, timeout=180):
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=timeout).stdout
    except subprocess.TimeoutExpired:
        return ""


if CACHE.exists():
    pl = json.loads(CACHE.read_text())
else:
    raw = run([YTDLP, "--flat-playlist", "--print", "%(id)s|%(title)s",
               "https://www.youtube.com/@aiDotEngineer/playlists"], timeout=300)
    entries = [l.split("|", 1) for l in raw.splitlines() if "|" in l]
    pl = {}
    for i, (pid, name) in enumerate(entries, 1):
        vids = run([YTDLP, "--flat-playlist", "--print", "%(id)s",
                    f"https://www.youtube.com/playlist?list={pid.strip()}"]).split()
        pl[name.strip()] = vids
        print(f"[{i}/{len(entries)}] {name.strip()}: {len(vids)}", file=sys.stderr)
    CACHE.write_text(json.dumps(pl, indent=2, ensure_ascii=False))

# Playlists that mark a video as belonging to a DIFFERENT event.
OTHER_EVENT = re.compile(r"europe|code 20|world's fair 2024|world's fair 2025|"
                         r"summit|2023|2024|: ai engineer world's fair 2025", re.I)

other_event_vids = set()
for name, vids in pl.items():
    if OTHER_EVENT.search(name):
        other_event_vids.update(vids)

candidates = set()
for name, vids in pl.items():
    if OTHER_EVENT.search(name):
        continue
    for v in vids:
        if v not in have and v not in other_event_vids:
            candidates.add(v)

print(f"\nplaylists scanned:  {len(pl)}")
print(f"already harvested:  {len(have)}")
print(f"other-event videos: {len(other_event_vids)}")
print(f"candidates:         {len(candidates)}")
(ROOT / "raw" / "candidates.txt").write_text("\n".join(sorted(candidates)))
