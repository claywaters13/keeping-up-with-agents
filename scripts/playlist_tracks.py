#!/usr/bin/env python3
"""Map each harvested video to the channel playlists it belongs to.

Playlist membership is authoritative for track assignment, unlike fuzzy title
matching against the schedule. A talk in several playlists gives us real graph
edges (e.g. both "Anthropic" and "Agentic Engineering").
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YTDLP = "/tmp/ytdlp-env/bin/yt-dlp"
CACHE = ROOT / "raw" / "playlist_members.json"

idx = json.loads((ROOT / "data" / "index.json").read_text())
ours = {r["video_id"] for r in idx}


def run(args, timeout=240):
    try:
        out = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return out.stdout
    except subprocess.TimeoutExpired:
        return ""


if CACHE.exists():
    members = json.loads(CACHE.read_text())
else:
    raw = run([YTDLP, "--flat-playlist", "--print", "%(id)s|%(title)s",
               "https://www.youtube.com/@aiDotEngineer/playlists"], timeout=300)
    playlists = []
    for line in raw.splitlines():
        if "|" in line:
            pid, name = line.split("|", 1)
            playlists.append((pid.strip(), name.strip()))
    print(f"playlists found: {len(playlists)}", file=sys.stderr)

    members = {}
    for i, (pid, name) in enumerate(playlists, 1):
        vids = run([YTDLP, "--flat-playlist", "--print", "%(id)s",
                    f"https://www.youtube.com/playlist?list={pid}"]).split()
        hit = [v for v in vids if v in ours]
        print(f"[{i}/{len(playlists)}] {name}: {len(hit)}/{len(vids)} ours", file=sys.stderr)
        if hit:
            members[name] = hit
    CACHE.write_text(json.dumps(members, indent=2, ensure_ascii=False))

# invert: video -> playlist names
vid2pl = {}
for name, vids in members.items():
    for v in vids:
        vid2pl.setdefault(v, []).append(name)


def clean(name: str) -> str:
    return name.replace(" @ AI Engineer", "").strip()


# Playlists that describe the venue rather than the subject.
STRUCTURAL = {"AIE World's Fair 2026 Complete Playlist",
              "AI Engineer World's Fair Online Track 2026", "Building AIE"}

covered = 0
for r in idx:
    pls = vid2pl.get(r["video_id"], [])
    topical = [clean(p) for p in pls if p not in STRUCTURAL]
    r["playlists"] = [clean(p) for p in pls]
    r["topics"] = topical
    # Prefer schedule track; fall back to the first topical playlist.
    if not r.get("track") and topical:
        r["track"] = topical[0]
    if r.get("track"):
        covered += 1

(ROOT / "data" / "index.json").write_text(json.dumps(idx, indent=2, ensure_ascii=False))

print(f"\nvideos with >=1 playlist: {sum(1 for r in idx if r['playlists'])}/{len(idx)}")
print(f"videos with a track now:  {covered}/{len(idx)}")
counts = {}
for r in idx:
    for t in r["topics"]:
        counts[t] = counts.get(t, 0) + 1
print(f"\ntopical playlists ({len(counts)}):")
for t, c in sorted(counts.items(), key=lambda x: -x[1])[:30]:
    print(f"  {c:3d}  {t}")
