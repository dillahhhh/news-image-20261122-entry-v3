#!/usr/bin/env python3
"""Render entry.png — a 1024x1024 Indonesian world-news dashboard.

Layout (heights add up to exactly 1024, asserted below):
  header 58 + strip 42 + lead 118 + secondary 142 + grid 610 + gap 6 + footer 48

The 34 stories come from stories.py, which defines STORIES (a list of 34
dicts with 'tag', 'title' and 'text') and HIGHLIGHT (one short string for
the strip). Story 0 is the lead, stories 1-3 are the secondary row, and
stories 4-33 fill the two-column grid.

Run:  python3 build_image.py   (writes entry.png next to this file)
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONT_REG = HERE / "fonts" / "DejaVuSans.ttf"
FONT_BOLD = HERE / "fonts" / "DejaVuSans-Bold.ttf"

W = 1024
H = 1024

# --- section heights (must sum to H) ---
H_HEADER = 58
H_STRIP = 42
H_LEAD = 118
H_SEC = 142
H_GRID = 610
H_GAP = 6
H_FOOT = 48
assert H_HEADER + H_STRIP + H_LEAD + H_SEC + H_GRID + H_GAP + H_FOOT == H

# --- palette ---
NAVY = (13, 38, 64)
NAVY_SOFT = (24, 56, 88)
RED = (185, 38, 32)
GOLD = (212, 160, 23)
INK = (24, 24, 24)
MUTED = (98, 98, 98)
LINE = (214, 214, 214)
PAPER = (255, 255, 255)
LEAD_BG = (243, 245, 247)
TAG_COLORS = {
    "DUNIA": (13, 38, 64),
    "POLITIK": (124, 31, 31),
    "EKONOMI": (27, 94, 32),
    "TEKNOLOGI": (21, 76, 121),
    "OLAHRAGA": (146, 64, 14),
    "HIBURAN": (107, 33, 98),
    "SAINS": (0, 105, 92),
    "KESEHATAN": (136, 14, 79),
}


def load(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size)


def wrap(draw, text, font, max_w):
    """Split text into lines that fit max_w (word wrap)."""
    lines = []
    cur = ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def shorten(draw, text, font, max_w):
    """Cut one line to max_w, adding an ellipsis when shortened."""
    if draw.textlength(text, font=font) <= max_w:
        return text
    while text and draw.textlength(text + "…", font=font) > max_w:
        text = text[:-1]
    return text + "…"


def tag_color(tag):
    return TAG_COLORS.get(tag.upper(), NAVY_SOFT)


def draw_header(draw):
    draw.rectangle([0, 0, W, H_HEADER], fill=NAVY)
    title_font = load(30, bold=True)
    date_font = load(16, bold=True)
    draw.text((24, 12), "BERITA DUNIA", font=title_font, fill=PAPER)
    date = "22 November 2026"
    dw = draw.textlength(date, font=date_font)
    draw.text((W - 24 - dw, 19), date, font=date_font, fill=(255, 214, 90))


def draw_strip(draw, highlight):
    y0 = H_HEADER
    draw.rectangle([0, y0, W, y0 + H_STRIP], fill=RED)
    label_font = load(15, bold=True)
    text_font = load(16)
    draw.text((24, y0 + 11), "SOROTAN", font=label_font, fill=PAPER)
    label_w = draw.textlength("SOROTAN", font=label_font)
    max_w = W - 24 - (24 + label_w + 18)
    shown = shorten(draw, highlight, text_font, max_w)
    draw.text((24 + label_w + 18, y0 + 11), shown, font=text_font, fill=PAPER)


def draw_lead(draw, story):
    y0 = H_HEADER + H_STRIP
    draw.rectangle([0, y0, W, y0 + H_LEAD], fill=LEAD_BG)
    draw.line([0, y0 + H_LEAD - 1, W, y0 + H_LEAD - 1], fill=LINE)
    tag_f = load(13, bold=True)
    title_f = load(24, bold=True)
    body_f = load(15)
    x = 24
    y = y0 + 10
    draw.text((x, y), story["tag"].upper(), font=tag_f, fill=tag_color(story["tag"]))
    y += 20
    for line in wrap(draw, story["title"], title_f, W - 48)[:2]:
        draw.text((x, y), line, font=title_f, fill=INK)
        y += 29
    for line in wrap(draw, story["text"], body_f, W - 48)[:1]:
        draw.text((x, y), line, font=body_f, fill=MUTED)


def draw_secondary(draw, stories):
    y0 = H_HEADER + H_STRIP + H_LEAD
    margin = 24
    gutter = 16
    col_w = (W - 2 * margin - 2 * gutter) // 3
    tag_f = load(12, bold=True)
    title_f = load(16, bold=True)
    body_f = load(13)
    for i, story in enumerate(stories):
        x = margin + i * (col_w + gutter)
        y = y0 + 10
        draw.text((x, y), story["tag"].upper(), font=tag_f, fill=tag_color(story["tag"]))
        y += 18
        for line in wrap(draw, story["title"], title_f, col_w)[:3]:
            draw.text((x, y), line, font=title_f, fill=INK)
            y += 20
        for line in wrap(draw, story["text"], body_f, col_w)[:2]:
            draw.text((x, y), line, font=body_f, fill=MUTED)
            y += 17
        if i < 2:
            div_x = x + col_w + gutter // 2
            draw.line([div_x, y0 + 12, div_x, y0 + H_SEC - 12], fill=LINE)


def draw_grid(draw, stories):
    y0 = H_HEADER + H_STRIP + H_LEAD + H_SEC
    margin = 24
    gutter = 16
    col_w = (W - 2 * margin - gutter) // 2
    rows = 15
    tag_f = load(11, bold=True)
    title_f = load(14)
    for idx, story in enumerate(stories):
        row = idx // 2
        col = idx % 2
        x = margin + col * (col_w + gutter)
        y = y0 + int(row * H_GRID / rows) + 3
        draw.text((x, y), story["tag"].upper(), font=tag_f, fill=tag_color(story["tag"]))
        y += 15
        shown = shorten(draw, story["title"], title_f, col_w)
        draw.text((x, y), shown, font=title_f, fill=INK)
        if row < rows - 1:
            draw.line([x, y0 + int((row + 1) * H_GRID / rows) - 1,
                       x + col_w, y0 + int((row + 1) * H_GRID / rows) - 1],
                      fill=LINE)


def draw_footer(draw, count):
    y0 = H - H_FOOT
    draw.rectangle([0, y0, W, H], fill=NAVY)
    font = load(14)
    left = f"{count} cerita dari berbagai sumber berita dunia"
    right = "22 November 2026"
    draw.text((24, y0 + 15), left, font=font, fill=PAPER)
    rw = draw.textlength(right, font=font)
    draw.text((W - 24 - rw, y0 + 15), right, font=font, fill=(255, 214, 90))


def main():
    from stories import HIGHLIGHT, STORIES

    assert len(STORIES) == 34, f"expected 34 stories, got {len(STORIES)}"
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    draw_strip(draw, HIGHLIGHT)
    draw_lead(draw, STORIES[0])
    draw_secondary(draw, STORIES[1:4])
    draw_grid(draw, STORIES[4:34])
    draw_footer(draw, len(STORIES))
    out = HERE / "entry.png"
    img.save(out)
    print(f"wrote {out} ({out.stat().st_size} bytes, {W}x{H})")


if __name__ == "__main__":
    main()
