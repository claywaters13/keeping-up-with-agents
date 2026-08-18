#!/usr/bin/env python3
"""Generate the podcast cover art for "Keeping up with Agents".

Typographic cover with a subtle graph/constellation motif nodding to the
wiki's concept-graph explorer. Palette and typography follow the dataviz
skill's reference instance (dark surfaces, system-sans, fixed categorical
hue order) — see scripts/make_cover.py inline comments for the mapping.

Renders at 2x supersampling (6000px) then downsamples to the target size
for clean anti-aliased edges, per Apple's 3000x3000 RGB requirement.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---- dataviz skill palette (references/palette.md) ----------------------
PAGE_PLANE = (13, 13, 13)        # #0d0d0d dark page plane (outer bg)
SURFACE = (26, 26, 25)           # #1a1a19 dark chart surface (inner wash)
INK_PRIMARY = (255, 255, 255)    # #ffffff
INK_SECONDARY = (195, 194, 183)  # #c3c2b7
INK_MUTED = (137, 135, 129)      # #898781
HAIRLINE = (255, 255, 255)       # edges drawn at low alpha of this

# dark-mode categorical slots, in fixed order (slots 1,3,7,5 used sparingly)
SLOT_BLUE = (57, 135, 229)     # #3987e5
SLOT_AQUA = (25, 158, 112)     # #199e70
SLOT_VIOLET = (144, 133, 233)  # #9085e9
SLOT_MAGENTA = (213, 81, 129)  # #d55181
NODE_COLORS = [SLOT_BLUE, SLOT_AQUA, SLOT_VIOLET, SLOT_MAGENTA]

SS = 2                 # supersample factor
SIZE = 3000
S = SIZE * SS           # working canvas size

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def make_background():
    """Radial gradient page-plane -> surface, darkest at edges."""
    img = Image.new("RGB", (S, S), PAGE_PLANE)
    px = img.load()
    cx, cy = S / 2, S / 2
    maxr = math.hypot(cx, cy)
    # Precompute per-row for speed using numpy-free approach: sample coarse grid then resize
    small = 300
    small_img = Image.new("RGB", (small, small))
    spx = small_img.load()
    scx, scy = small / 2, small / 2
    smaxr = math.hypot(scx, scy)
    for y in range(small):
        for x in range(small):
            r = math.hypot(x - scx, y - scy) / smaxr
            t = min(1.0, r ** 1.4)
            spx[x, y] = lerp(SURFACE, PAGE_PLANE, t)
    img = small_img.resize((S, S), Image.LANCZOS)
    return img


def safe_zone(cx, cy, half_w, half_h, x, y, margin):
    return (cx - half_w - margin) <= x <= (cx + half_w + margin) and \
           (cy - half_h - margin) <= y <= (cy + half_h + margin)


def draw_constellation(draw, rng, avoid_rect):
    """Scatter nodes + thin connecting edges, avoiding the text safe zone."""
    cx, cy, hw, hh = avoid_rect
    n = 46
    pts = []
    attempts = 0
    while len(pts) < n and attempts < 4000:
        attempts += 1
        x = rng.uniform(S * 0.03, S * 0.97)
        y = rng.uniform(S * 0.03, S * 0.97)
        if safe_zone(cx, cy, hw, hh, x, y, S * 0.03):
            continue
        pts.append((x, y))

    # connect each point to its 1-2 nearest neighbours (constellation look)
    edges = set()
    for i, (x1, y1) in enumerate(pts):
        dists = sorted(
            ((math.hypot(x1 - x2, y1 - y2), j) for j, (x2, y2) in enumerate(pts) if j != i)
        )
        for _, j in dists[:2]:
            edges.add((min(i, j), max(i, j)))

    for i, j in edges:
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        length = math.hypot(x2 - x1, y2 - y1)
        if length > S * 0.22:
            continue
        alpha = max(10, 46 - int(length / (S * 0.22) * 36))
        draw.line([(x1, y1), (x2, y2)], fill=(*HAIRLINE, alpha), width=int(2.2 * SS))

    for idx, (x, y) in enumerate(pts):
        color = NODE_COLORS[idx % len(NODE_COLORS)]
        r = rng.uniform(4.5, 9.5) * SS
        # soft glow
        glow_r = r * 3.2
        draw.ellipse(
            [x - glow_r, y - glow_r, x + glow_r, y + glow_r],
            fill=(*color, 18),
        )
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(*color, 210))
        draw.ellipse([x - r, y - r, x + r, y + r], outline=(*PAGE_PLANE, 255), width=max(1, int(1.2 * SS)))


def letter_spaced(draw, xy, text, font, fill, tracking, anchor_center_x=None):
    """Draw text with extra letter-spacing, centered horizontally if anchor_center_x given."""
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_center_x is not None:
        x = anchor_center_x - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking
    return total


def main():
    rng = random.Random(20260813)
    bg = make_background()
    overlay = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    title_font = ImageFont.truetype(FONT_BOLD, int(340 * SS))
    eyebrow_font = ImageFont.truetype(FONT_BOLD, int(58 * SS))
    sub_font = ImageFont.truetype(FONT_REG, int(56 * SS))

    cx = S / 2
    line1, line2 = "KEEPING UP", "WITH AGENTS"

    # measure block for safe-zone sizing
    bbox1 = odraw.textbbox((0, 0), line1, font=title_font)
    bbox2 = odraw.textbbox((0, 0), line2, font=title_font)
    line_h = (bbox1[3] - bbox1[1]) * 1.28
    # full safe-zone height: eyebrow row + title block + rule + subtitle row
    block_h = line_h * 2 + 620 * SS
    block_w = max(bbox1[2] - bbox1[0], bbox2[2] - bbox2[0]) * 1.3

    draw_constellation(odraw, rng, (cx, S / 2, block_w / 2, block_h / 2))

    overlay = overlay.filter(ImageFilter.GaussianBlur(0))  # no-op keep pipeline explicit
    bg = Image.alpha_composite(bg.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(bg)

    # eyebrow
    eyebrow_y = S / 2 - block_h / 2 - 150 * SS
    letter_spaced(draw, (0, eyebrow_y), "AI ENGINEER WORLD'S FAIR 2026",
                  eyebrow_font, (*INK_MUTED, 255), tracking=14 * SS, anchor_center_x=cx)

    # title, two lines, bold white, tight leading
    title_y1 = S / 2 - line_h * 0.62
    title_y2 = title_y1 + line_h
    letter_spaced(draw, (0, title_y1), line1, title_font, (*INK_PRIMARY, 255),
                  tracking=4 * SS, anchor_center_x=cx)
    letter_spaced(draw, (0, title_y2), line2, title_font, (*INK_PRIMARY, 255),
                  tracking=4 * SS, anchor_center_x=cx)

    # thin rule + subtitle
    rule_y = title_y2 + line_h * 1.22
    rule_w = block_w * 0.42
    draw.line([(cx - rule_w / 2, rule_y), (cx + rule_w / 2, rule_y)],
              fill=(*INK_MUTED, 140), width=int(2 * SS))

    sub_y = rule_y + 60 * SS
    letter_spaced(draw, (0, sub_y), "231 TALKS. ZERO SETTLED.",
                  sub_font, (*INK_SECONDARY, 255), tracking=10 * SS, anchor_center_x=cx)

    bg = bg.convert("RGB")
    bg = bg.resize((SIZE, SIZE), Image.LANCZOS)
    bg.save("/home/openclaw-host/aiewf-2026/podcast/cover.png", optimize=True)
    print("wrote cover.png", bg.size)


if __name__ == "__main__":
    main()
