import math, os
from kit import *
from gl import glyph
DMS = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'DMSans-500.ttf')

def descriptor(track=260):
    return text_path(DMS, 'LONGEVITY & REGENERATIVE HEALTH', track)

def lockup():
    """wordmark + descriptor, descriptor width = wordmark width"""
    body, (bx, by, bw, bh) = LA
    db, dw = descriptor()
    s = bw / dw
    gap = 150
    return (strip_defs(body) + f'<g transform="translate(0,{gap + 700 * s * .72:.1f}) scale({s:.4f})">{db}</g>',
            (0, -700, bw, 700 + gap + 700 * s * .72))

def lockup_h():
    """monogram | wordmark horizontal"""
    wb, (wx, wy, ww, wh) = SA; body, (bx, by, bw, bh) = LA
    x2 = ww + 260
    return (f'<path d="{glyph(GRAZE, "W")[0]}"/><rect x="{ww+120}" y="-700" width="8" height="700"/>'
            f'<g transform="translate({x2},0)">{strip_defs(body)}</g>', (0, -700, x2 + bw, 700))

def micro():
    """optical micro version for < 40 px: hairlines thickened"""
    body, box = LA
    return (strip_defs(body).replace('<path ', '<path stroke="currentColor" stroke-width="16" stroke-linejoin="round" ').replace('<rect x="142" y="-470" width="140" height="9"/>', '<rect x="142" y="-476" width="140" height="20"/>'), box)

def seal_ring(text='LONGEVITY & REGENERATIVE HEALTH · AUSTRIA · ', R=470, size=74):
    """monogram W in a ring of outlined DM Sans text"""
    sc = size / 1000; parts = []
    widths = []
    for ch in text:
        if ch == ' ': widths.append(260 * sc); continue
        d, adv, _ = glyph(DMS, ch); widths.append(adv * sc + 32 * sc)
    total = sum(widths); circ = 2 * math.pi * R
    k = circ / total  # spread evenly
    a = -90.0; 
    for ch, w in zip(text, widths):
        span = w * k / R * 180 / math.pi
        if ch != ' ':
            d, adv, _ = glyph(DMS, ch)
            mid = a + span / 2
            parts.append(f'<g transform="rotate({mid:.2f}) translate(0,{-R}) scale({sc}) translate({-adv/2:.1f},0)"><path d="{d}"/></g>')
        a += span
    wd, wadv, _ = glyph(GRAZE, 'W')
    s = .78
    inner = f'<g transform="translate({-wadv*s/2:.1f},{700*s/2:.1f}) scale({s})"><path d="{wd}"/></g>'
    rings = f'<circle r="{R+110}" fill="none" stroke="currentColor" stroke-width="5"/><circle r="{R-120}" fill="none" stroke="currentColor" stroke-width="3"/>'
    return rings + ''.join(parts) + inner, (-R-125, -R-125, 2*R+250, 2*R+250)

SEAL2 = seal_ring()
LOCK = lockup(); LOCKH = lockup_h(); MICRO = micro()
