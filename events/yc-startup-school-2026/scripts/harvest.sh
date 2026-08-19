#!/usr/bin/env bash
# Harvest YC Startup School 2026 talk captions + metadata from YouTube.
# One extraction pass per video: writes .info.json and .en.json3 into raw/caps/.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
YTDLP=/tmp/ytdlp-env/bin/yt-dlp
OUT="$ROOT/raw/caps"
mkdir -p "$OUT"

total=$(wc -l < "$ROOT/raw/video_ids.txt")
i=0
while read -r vid; do
  [ -z "$vid" ] && continue
  i=$((i+1))
  if [ -f "$OUT/$vid.en.json3" ]; then
    echo "[$i/$total] $vid (cached)"
    continue
  fi
  echo "[$i/$total] $vid"
  timeout 120 "$YTDLP" \
    --skip-download \
    --write-auto-subs --sub-langs "en" --sub-format json3 \
    --write-info-json \
    --sleep-requests 1 \
    -o "$OUT/%(id)s.%(ext)s" \
    "https://www.youtube.com/watch?v=$vid" >>"$ROOT/raw/harvest.log" 2>&1 \
    || echo "FAILED: $vid" >> "$ROOT/raw/failures.txt"
done < "$ROOT/raw/video_ids.txt"

echo "DONE. captions=$(ls "$OUT"/*.en.json3 2>/dev/null | wc -l) info=$(ls "$OUT"/*.info.json 2>/dev/null | wc -l)"
