"""Draw an edition's social card: the image a link to the site shows when it is shared.

1200 by 630 pixels, the size link previews use. It is the cover in small: the name and number over a heavy
rule, the plate on the left, and on the right the month, the editorial's subject and the lead selections.
The build draws one for every edition (site/build.py), with the fonts the site itself uses.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS = Path(__file__).resolve().parent / "static" / "fonts"
W, H, S = 1200, 630, 3          # the card, and the scale it is drawn at before being reduced (for smooth edges)
INK = (11, 11, 12)
M = 56                          # margin

# Characters the "latin" font files hold; anything else is drawn from the "latin-ext" files.
LATIN = {0x131, 0x152, 0x153, 0x2BB, 0x2BC, 0x2C6, 0x2DA, 0x2DC, 0x20AC, 0x2122, 0x2191, 0x2193, 0x2212, 0x2215}


def _font(family, size, axes):
    """The face at a size, as a pair: the latin file and the latin-ext file."""
    pair = []
    for part in ("latin", "latin-ext"):
        f = ImageFont.truetype(str(FONTS / f"{family}-normal-{part}.woff2"), round(size * S))
        f.set_variation_by_axes(axes)
        pair.append(f)
    return pair


def _slab(size, weight=900):
    return _font("besley", size, [weight])


def _sans(size, weight=900, width=66):
    return _font("archivo", size, [weight, width])


def _face(pair, ch):
    cp = ord(ch)
    return pair[0] if cp <= 0xFF or 0x2000 <= cp <= 0x206F or cp in LATIN else pair[1]


def _width(text, pair, tracking=0.0):
    size = pair[0].size
    return sum(_face(pair, c).getlength(c) for c in text) + tracking * size * max(len(text) - 1, 0)


def _text(draw, x, y, text, pair, tracking=0.0, anchor="ls", fill=INK):
    """Draw text letter by letter (so it can be tracked), from x at baseline y. Coordinates are card pixels."""
    x, y = x * S, y * S
    if anchor[0] == "r":
        x -= _width(text, pair, tracking)
    for c in text:
        f = _face(pair, c)
        draw.text((x, y), c, font=f, fill=fill, anchor="l" + anchor[1])
        x += f.getlength(c) + tracking * pair[0].size
    return x / S


def _fit(text, make, size, room, floor, tracking=0.0):
    """The largest size, from `size` down to `floor`, at which the text is no wider than `room` card pixels."""
    while size > floor and _width(text, make(size), tracking) > room * S:
        size -= 2
    return make(size)


def _well(draw, cx, cy, d, kind, cover):
    """One well, centered at (cx, cy) with diameter d: a ring, a ring with a dot, a filled disc, or a double ring."""
    def disc(r, **kw):
        draw.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], **kw)
    faint = tuple(round(c * 0.8 + i * 0.2) for c, i in zip(cover, INK))      # the ink at one fifth strength
    mid = tuple(round(c * 0.6 + i * 0.4) for c, i in zip(cover, INK))
    if kind == "empty":
        disc(d / 2, outline=faint, width=round(2.5 * S))
    elif kind == "shortlisted":
        disc(d / 2, outline=mid, width=round(2.5 * S))
        disc(d * 0.12, fill=INK)
    elif kind == "lead":
        disc(d * 0.5, fill=INK)
        disc(d * 0.5 - 2.6, fill=cover)
        disc(d * 0.5 - 5.2, fill=INK)
    else:
        disc(d * 0.39, fill=INK)


def draw_card(edition, site, out):
    cover = tuple(int(edition["cover"].lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    img = Image.new("RGB", (W * S, H * S), cover)
    draw = ImageDraw.Draw(img)

    # The masthead: the name, the tagline and the number on one baseline, over a heavy rule.
    base = 168
    end = _text(draw, M - 5, base, site["name"], _slab(150), tracking=-0.045)
    number, numbers = f"No. {edition['number']}", _sans(82, 900, 66)
    _text(draw, W - M, base, number, numbers, anchor="rs")
    tagline = site["tagline"].upper()
    room = W - M - _width(number, numbers) / S - 30 - (end + 26)      # what is left between the name and the number
    _text(draw, end + 26, base, tagline, _fit(tagline, lambda s: _sans(s, 700, 78), 21, room, 13, 0.06), tracking=0.06)
    draw.rectangle([M * S, 196 * S, (W - M) * S, 204 * S], fill=INK)

    # The plate.
    top, pitch, d, x0 = 240, 44, 34, M + 58
    letters = _sans(40, 900, 64)
    for r, row in enumerate(edition["plate"]):
        cy = top + pitch * r + pitch / 2
        _text(draw, M, cy, row["beat"]["row"], letters, anchor="lm")
        for c, cell in enumerate(row["cells"]):
            kind = cell["kind"]
            if kind == "selected":
                kind = "lead" if cell["work"]["tier"] == "lead" else "selected"
            _well(draw, x0 + pitch * c + d / 2, cy, d, kind, cover)
    plate_right = x0 + pitch * len(edition["plate"][0]["cells"]) - (pitch - d)
    bottom = top + pitch * len(edition["plate"])

    # The panel: the month, the editorial's subject, and the lead selections.
    px = plate_right + 44
    draw.rectangle([(px - 2) * S, (top - 8) * S, px * S, (bottom + 4) * S], fill=INK)
    px += 30
    room = W - M - px
    _text(draw, px, top + 14, edition["period_label"].upper(), _sans(22, 700, 78), tracking=0.06)
    subject = edition.get("subject") or "Editorial"
    _text(draw, px - 3, top + 96, subject, _fit(subject, _slab, 84, room, 50, -0.03), tracking=-0.03)

    leads = [cell["work"] for row in edition["plate"] for cell in row["cells"]
             if cell["kind"] == "selected" and cell["work"]["tier"] == "lead"][:5]
    code, y = _sans(17, 800, 78), top + 150
    # One size for the whole list: the largest at which the longest title fits.
    longest = max((w["short"] for w in leads), key=lambda s: _width(s, _slab(27, 800), -0.012), default="")
    titles = _fit(longest, lambda s: _slab(s, 800), 27, room - 44, 19, -0.012)
    for w in leads:
        draw.rectangle([px * S, (y - 28) * S, (W - M) * S, (y - 28) * S + S], fill=tuple(round(c * 0.75 + i * 0.25) for c, i in zip(cover, INK)))
        _text(draw, px, y, w["well"], code)
        _text(draw, px + 44, y, w["short"], titles, tracking=-0.012)
        y += 41

    out.parent.mkdir(parents=True, exist_ok=True)
    # Two flat colors and the blends between them: a small palette keeps the file light without visible loss.
    img.resize((W, H), Image.LANCZOS).quantize(colors=64, dither=Image.Dither.NONE).save(out, optimize=True)
