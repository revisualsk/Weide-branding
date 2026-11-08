"""WEIDE identity v2: willow-leaf W monogram (traced from the approved artwork),
Cormorant Garamond wordmark and DM Sans descriptor. Boxes are (x, y, w, h)."""
import json, math, os, re
from gl import glyph

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, '..', 'fonts')
DMS = os.path.join(FONTS, 'DMSans-400.ttf')
CG = os.path.join(FONTS, 'CormorantGaramond-500.ttf')

# --- monogram -------------------------------------------------------------
_mono_d = re.search(r' d="([^"]+)"', open(os.path.join(HERE, '..', 'newlogo', 'mono.svg')).read()).group(1)
MX0, MY0, MX1, MY1 = 18.0, 20.0, 577.0, 397.0          # traced bounds
MONO_W, MONO_H = MX1 - MX0, MY1 - MY0

def monogram():
    return (f'<path fill-rule="evenodd" transform="translate({-MX0},{-MY0})" d="{_mono_d}"/>',
            (0, 0, MONO_W, MONO_H))

# --- type helpers ---------------------------------------------------------
def setline(font, text, track=0.0):
    """outlined text on a baseline at y=0, returns (body, width, cap)"""
    x = 0.0; out = []
    for i, ch in enumerate(text):
        if ch == ' ':
            x += glyph(font, 'space')[1] + track; continue
        d, adv, _ = glyph(font, ch)
        out.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>')
        x += adv + (track if i < len(text) - 1 else 0)
    return ''.join(out), x

def wordmark(track=150):
    body, w = setline(CG, 'WEIDE', track)
    return body, (0, -625, w, 625)

def descriptor(track=260):
    body, w = setline(DMS, 'LONGEVITY & REGENERATIVE HEALTH', track)
    return body, (0, -700, w, 700)

def _place(lg, x, y, w):
    """place a (body, box) so its box starts at x,y with width w; returns (svg, height)"""
    body, (bx, by, bw, bh) = lg
    s = w / bw
    return f'<g transform="translate({x:.2f},{y:.2f}) scale({s:.5f}) translate({-bx},{-by})">{body}</g>', bh * s

# --- lockups (unit: monogram width = 1000) --------------------------------
def lockup(with_descriptor=True):
    MW = 1000.0
    word_w, desc_w = 1340.0, 1670.0
    total_w = desc_w if with_descriptor else word_w
    cx = total_w / 2
    parts = []
    m, mh = _place(monogram(), cx - MW / 2, 0, MW); parts.append(m)
    y = mh + 125
    wsvg, wh = _place(wordmark(), cx - word_w / 2, y, word_w); parts.append(wsvg)
    y += wh
    if with_descriptor:
        y += 112
        dsvg, dh = _place(descriptor(), cx - desc_w / 2, y, desc_w); parts.append(dsvg)
        y += dh
    return ''.join(parts), (0, 0, total_w, y)

def lockup_h():
    """monogram left, wordmark + descriptor right"""
    mh = 1000.0; mw = mh * MONO_W / MONO_H
    m, _ = _place(monogram(), 0, 0, mw)
    x = mw + 230
    word_w = 2000.0
    wsvg, wh = _place(wordmark(), x, 300, word_w)
    dsvg, dh = _place(descriptor(), x, 300 + wh + 110, word_w)
    return m + f'<rect x="{mw + 115 - 4}" y="80" width="8" height="840"/>' + wsvg + dsvg, (0, 0, x + word_w, mh)

def seal(text='LONGEVITY & REGENERATIVE HEALTH · AUSTRIA · ', R=470, size=74):
    sc = size / 1000; widths = []
    for ch in text:
        widths.append(260 * sc if ch == ' ' else glyph(DMS, ch)[1] * sc + 32 * sc)
    k = 2 * math.pi * R / sum(widths); a = -90.0; parts = []
    for ch, w in zip(text, widths):
        span = w * k / R * 180 / math.pi
        if ch != ' ':
            d, adv, _ = glyph(DMS, ch)
            parts.append(f'<g transform="rotate({a + span / 2:.2f}) translate(0,{-R}) scale({sc}) translate({-adv/2:.1f},0)"><path d="{d}"/></g>')
        a += span
    mw = 560.0; s = mw / MONO_W; mh = MONO_H * s
    inner = f'<g transform="translate({-mw/2:.1f},{-mh/2 - 8:.1f}) scale({s:.5f}) translate({-MX0},{-MY0})"><path fill-rule="evenodd" d="{_mono_d}"/></g>'
    rings = (f'<circle r="{R + 110}" fill="none" stroke="currentColor" stroke-width="5"/>'
             f'<circle r="{R - 120}" fill="none" stroke="currentColor" stroke-width="3"/>')
    return rings + ''.join(parts) + inner, (-R - 125, -R - 125, 2 * R + 250, 2 * R + 250)

MONO = monogram()
WORD = wordmark()
DESC = descriptor()
LOCK = lockup()
LOCK_SHORT = lockup(False)
LOCKH = lockup_h()
SEAL = seal()
