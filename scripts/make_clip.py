#!/usr/bin/env python3
"""Cut a captioned square/vertical audiogram from an episode, for social feeds.

Usage:
  python3 scripts/make_clip.py episodes/episode-001.m4a \\
      --start 0:17 --end 1:14 \\
      --episode 1 \\
      --event "AI Engineer World's Fair 2026" \\
      --out clips/episode-001-1x1.mp4 \\
      [--aspect 1x1|4x5]           # default 1x1 \\
      [--snap-end 4]               # extend to the next sentence end, seconds \\
      [--whisper-model small.en]   # faster-whisper model for word timings \\
      [--no-captions]

What it does:
  1. Transcribes the excerpt locally with faster-whisper at word-level
     timestamps. Captions are the whole point on LinkedIn, which autoplays
     muted, so this is not optional polish.
  2. Snaps the out point to the end of the last complete sentence within
     --snap-end seconds of --end, so the clip doesn't stop mid-phrase.
  3. Cuts the audio with short fades and loudness-normalizes it to -16 LUFS.
  4. Draws the still frame with PIL in the show's cover-art style: near-black,
     constellations, wordmark, episode/event line, "AI MOVES FAST. KEEP UP."
  5. Burns in 3-4 word caption cards (libass). Words containing digits, and
     "zero"/"none", are drawn in the accent colour, which is what makes a
     stats-heavy excerpt read while scrolling.
  6. Renders H.264/AAC MP4 with +faststart, sized for the chosen aspect.

Requires: ffmpeg/ffprobe on PATH, Pillow, and faster-whisper. If faster-whisper
lives in another virtualenv, point --whisper-python (or $KUWA_WHISPER_PYTHON)
at that interpreter and this script re-execs itself there.
"""
import argparse
import json
import math
import os
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SHOW_TITLE = "KEEPING UP WITH AGENTS"
TAGLINE = "AI MOVES FAST. KEEP UP."
BG_RGB = (11, 11, 13)
PALETTE = [(59, 111, 212), (123, 92, 214), (209, 70, 110), (47, 158, 107), (70, 150, 230)]

# (canvas, title_y, rule_y, subtitle_y, wave_y, wave_h, caption_y, footer_y)
LAYOUTS = {
    "1x1": dict(size=(1080, 1080), title_y=208, rule_y=292, sub_y=312,
                wave_y=450, wave_h=160, cap_y=748, foot_y=890),
    "4x5": dict(size=(1080, 1350), title_y=300, rule_y=384, sub_y=404,
                wave_y=580, wave_h=180, cap_y=930, foot_y=1140),
}


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def parse_time(value):
    """Accept 73, 1:13, or 0:01:13.5."""
    parts = str(value).split(":")
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + float(part)
    return seconds


def font_file(query, fallback):
    try:
        out = subprocess.run(["fc-match", "-f", "%{file}", query],
                             capture_output=True, text=True, check=True).stdout.strip()
        if out and Path(out).exists():
            return out
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return fallback


def transcribe_words(audio, model_name):
    """[{s, e, w}] word timings for the whole file, via faster-whisper."""
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=8)
    segments, _ = model.transcribe(str(audio), beam_size=5, word_timestamps=True, vad_filter=False)
    words = []
    for seg in segments:
        for w in seg.words or []:
            text = w.word.strip()
            if text:
                words.append({"s": round(w.start, 3), "e": round(w.end, 3), "w": text})
    return words


def snap_out_point(words, target, window):
    """End of the last sentence-final word within `window` seconds of target."""
    best = None
    for w in words:
        if w["e"] <= target + window and re.search(r"[.?!]$", w["w"]):
            best = w["e"]
    if best is None or best < target - 2.0:
        return target
    return best


def draw_background(path, layout, episode_label, accent_seed=11):
    from PIL import Image, ImageDraw, ImageFont

    W, H = layout["size"]
    img = Image.new("RGB", (W, H), BG_RGB)
    d = ImageDraw.Draw(img)

    random.seed(accent_seed)

    def cluster(cx, cy, n, spread_x, spread_y):
        pts = [(int(random.gauss(cx, spread_x)), int(random.gauss(cy, spread_y)),
                random.choice(PALETTE)) for _ in range(n)]
        for i, (x, y, _) in enumerate(pts):
            near = sorted((math.hypot(x - x2, y - y2), j)
                          for j, (x2, y2, _) in enumerate(pts) if j != i)[:2]
            for _, j in near:
                d.line([(x, y), (pts[j][0], pts[j][1])], fill=(44, 44, 52), width=1)
        for x, y, c in pts:
            r = random.choice([3, 4, 5])
            d.ellipse([x - r * 3, y - r * 3, x + r * 3, y + r * 3],
                      fill=tuple(int(v * 0.20) for v in c))
            d.ellipse([x - r, y - r, x + r, y + r], fill=c)

    cluster(W * 0.17, H * 0.085, 6, 90, 32)
    cluster(W * 0.81, H * 0.078, 6, 100, 30)
    cluster(W * 0.19, H * 0.924, 6, 105, 32)
    cluster(W * 0.81, H * 0.926, 7, 110, 32)

    black = font_file("Lato:style=Black", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    medium = font_file("Lato:style=Medium", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    f_title = ImageFont.truetype(black, 54)
    f_sub = ImageFont.truetype(medium, 25)
    f_foot = ImageFont.truetype(medium, 23)

    def tracked(text, y, font, fill, tracking):
        widths = [d.textlength(ch, font=font) for ch in text]
        x = W / 2 - (sum(widths) + tracking * (len(text) - 1)) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill)
            x += w + tracking

    tracked(SHOW_TITLE, layout["title_y"], f_title, (255, 255, 255), 3)
    d.line([(W / 2 - 200, layout["rule_y"]), (W / 2 + 200, layout["rule_y"])],
           fill=(62, 62, 72), width=1)
    tracked(episode_label, layout["sub_y"], f_sub, (140, 140, 152), 3)
    tracked(TAGLINE, layout["foot_y"], f_foot, (104, 104, 116), 5)

    img.save(path)


def write_ass(path, words, end, layout, accent, max_words=4, max_chars=26):
    """3-4 word caption cards, numbers in the accent colour."""
    W, H = layout["size"]
    cards, cur = [], []
    for w in words:
        if w["s"] >= end - 0.6:
            break
        tentative = cur + [w]
        if len(tentative) > max_words or len(" ".join(x["w"] for x in tentative)) > max_chars:
            if cur:
                cards.append(cur)
            cur = [w]
        else:
            cur = tentative
        if re.search(r"[.?!]$", w["w"]):
            cards.append(cur)
            cur = []
    if cur:
        cards.append(cur)

    white = "&H00FFFFFF&"
    accent_ass = "&H00{}{}{}&".format(accent[4:6], accent[2:4], accent[0:2])  # RGB hex -> ASS BGR
    is_number = re.compile(r"\d|^(zero|none)[.,!?]?$", re.I)

    def ts(t):
        t = max(0.0, t)
        return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"

    lines = []
    for i, card in enumerate(cards):
        start = card[0]["s"] - 0.06
        stop = min(card[-1]["e"] + 0.10, end)
        if i + 1 < len(cards):
            nxt = cards[i + 1][0]["s"] - 0.06
            if 0 <= nxt - stop < 0.40:
                stop = nxt
        text = " ".join(
            "{{\\c{}}}{}".format(accent_ass if is_number.search(w["w"]) else white, w["w"])
            for w in card
        )
        lines.append(
            f"Dialogue: 0,{ts(start)},{ts(stop)},Cap,,0,0,0,,"
            f"{{\\an5\\pos({W // 2},{layout['cap_y']})\\fad(90,90)}}{text}"
        )

    path.write_text(
        "[Script Info]\n"
        "ScriptType: v4.00+\n"
        f"PlayResX: {W}\nPlayResY: {H}\n"
        "WrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
        "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Cap,Lato Black,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,"
        "0,0,0,0,100,100,1,0,1,4,0,5,60,60,60,1\n\n"
        "[Events]\n"
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
        + "\n".join(lines) + "\n"
    )
    return len(cards)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio", type=Path, help="episode audio (any container ffmpeg reads)")
    ap.add_argument("--start", required=True, help="excerpt in point, e.g. 0:17")
    ap.add_argument("--end", required=True, help="excerpt out point, e.g. 1:14")
    ap.add_argument("--episode", required=True, help="episode number, e.g. 1")
    ap.add_argument("--event", required=True, help='e.g. "AI Engineer World\'s Fair 2026"')
    ap.add_argument("--out", type=Path, default=None, help="output mp4 (default: clips/<stem>-<aspect>.mp4)")
    ap.add_argument("--aspect", default="1x1", choices=sorted(LAYOUTS))
    ap.add_argument("--snap-end", type=float, default=4.0,
                    help="seconds past --end to look for a sentence boundary (0 disables)")
    ap.add_argument("--accent", default="4DA3FF", help="caption accent colour, RRGGBB")
    ap.add_argument("--whisper-model", default="small.en")
    ap.add_argument("--whisper-python", default=os.environ.get("KUWA_WHISPER_PYTHON"),
                    help="interpreter that has faster-whisper, if not this one")
    ap.add_argument("--no-captions", action="store_true")
    args = ap.parse_args()

    try:
        import faster_whisper  # noqa: F401
        import PIL  # noqa: F401
    except ImportError:
        # A venv's bin/python often symlinks to the same real interpreter, so compare
        # the literal paths and use a sentinel to make the hand-off strictly once.
        if args.whisper_python and Path(args.whisper_python).exists() \
                and os.environ.get("KUWA_REEXEC") != "1":
            os.environ["KUWA_REEXEC"] = "1"
            os.execv(args.whisper_python, [args.whisper_python, __file__] + sys.argv[1:])
        raise SystemExit("needs Pillow + faster-whisper (see --whisper-python)")

    layout = LAYOUTS[args.aspect]
    start = parse_time(args.start)
    end = parse_time(args.end)
    if end <= start:
        raise SystemExit("--end must be after --start")

    out = args.out or REPO_ROOT / "clips" / f"{args.audio.stem}-{args.aspect}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        probe_len = (end - start) + max(args.snap_end, 0.0)

        words = []
        if not args.no_captions:
            probe_wav = tmp / "probe.wav"
            run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                 "-ss", f"{start}", "-t", f"{probe_len}", "-i", str(args.audio),
                 "-ar", "16000", "-ac", "1", str(probe_wav)])
            words = transcribe_words(probe_wav, args.whisper_model)
            if args.snap_end > 0:
                snapped = snap_out_point(words, end - start, args.snap_end)
                if snapped > end - start:
                    print(f"snapped out point +{snapped - (end - start):.2f}s to the sentence end")
                end = start + snapped

        dur = end - start
        fade_out = max(dur - 0.40, 0.0)
        clip_wav = tmp / "clip.wav"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-ss", f"{start}", "-t", f"{dur + 0.45}", "-i", str(args.audio),
             "-af", f"afade=t=in:st=0:d=0.35,afade=t=out:st={fade_out:.2f}:d=0.40,"
                    "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-ar", "48000", "-ac", "2", str(clip_wav)])

        bg = tmp / "bg.png"
        draw_background(bg, layout,
                        f"EPISODE {args.episode}  ·  {args.event.upper()}")

        vf = (f"[1:a]showwaves=s={layout['size'][0] - 180}x{layout['wave_h']}:mode=cline:"
              f"rate=30:scale=sqrt:colors=0x{args.accent}:draw=full,"
              "format=yuva420p,colorchannelmixer=aa=0.92[w];"
              f"[0:v][w]overlay=x=90:y={layout['wave_y']}[v0];")
        if words:
            caps = tmp / "caps.ass"
            n = write_ass(caps, words, dur + 0.45, layout, args.accent)
            print(f"{n} caption cards")
            vf += f"[v0]ass={caps},format=yuv420p[v]"
        else:
            vf += "[v0]format=yuv420p[v]"

        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-loop", "1", "-i", str(bg), "-i", str(clip_wav),
             "-filter_complex", vf, "-map", "[v]", "-map", "1:a", "-shortest", "-r", "30",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-profile:v", "high", "-level", "4.1", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
             "-movflags", "+faststart", str(out)])

    size_mb = out.stat().st_size / 1e6
    print(f"{out}  {dur + 0.45:.1f}s  {size_mb:.1f} MB  {layout['size'][0]}x{layout['size'][1]}")


if __name__ == "__main__":
    main()
