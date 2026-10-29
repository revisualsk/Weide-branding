import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from gl import glyph, kern
U = os.environ.get('UFONTS', os.path.join(os.path.dirname(__file__), '..', 'uf'))
GRAZE = f'{U}/graze/Graze.otf'
CHAMB = f'{U}/chambery/Chambery/OpenType-PS/Chambery-Regular.otf'
LUX = f'{U}/luxury/Luxury.otf'
QSERIF = f'{U}/quiet/QuietLuxury-Serif.otf'
QSCRIPT = f'{U}/quiet/QuietLuxury-Script.otf'

def leaf(cx, cy, L, Wd, ang):
    a = math.radians(ang); ca, sa = math.cos(a), math.sin(a)
    p = lambda u, v: f'{cx+u*ca-v*sa:.1f} {cy+u*sa+v*ca:.1f}'
    k = Wd * 1.33
    return f'M{p(-L/2,0)}C{p(-L/4,-k)} {p(L/4,-k*.9)} {p(L/2,0)}C{p(L/4,k*.9)} {p(-L/4,k)} {p(-L/2,0)}Z'

def setw(font, seq, sp=None, kern_on=True):
    """seq: list of glyph names/chars; sp: {index: extra after glyph i}"""
    sp = sp or {}; x = 0; out = []
    for i, n in enumerate(seq):
        d, adv, bb = glyph(font, n)
        out.append((n, x, d, adv, bb))
        x += adv + sp.get(i, 0)
        if kern_on and i + 1 < len(seq) and len(n) == 1 and len(seq[i+1]) == 1:
            x += kern(font, n, seq[i+1])
    return out, x - sp.get(len(seq) - 1, 0)

# A — Graze caps: native woven W, fused serifs EIDE, breathing E
def logo_GA(gap=None):
    gap = gap or {0: -10, 1: -38, 2: -38, 3: -38}
    gl, w = setw(GRAZE, list('WEIDE'), gap, kern_on=False)
    parts = []
    for n, x, d, adv, bb in gl:
        if n == 'E':
            parts.append(f'<g transform="translate({x:.1f},0)"><path d="{d}" clip-path="url(#gCutE)"/><rect x="142" y="-470" width="140" height="9"/></g>')
        else:
            parts.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>')
    defs = '<defs><clipPath id="gCutE"><path d="M-100 -800H500V-540H119V-390H500V100H-100Z"/></clipPath></defs>'
    return defs + ''.join(parts), (0, -700, w, 700)

def mono_GA():
    d, adv, bb = glyph(GRAZE, 'W')
    R = 520
    return (f'<circle r="{R}" fill="none" stroke="currentColor" stroke-width="6"/>'
            f'<line x1="{-R}" x2="{R}" y1="0" y2="0" stroke="currentColor" stroke-width="2" opacity=".0"/>'
            f'<g transform="translate({-adv/2*1.02:.1f},{350*1.02:.1f}) scale(1.02)"><path d="{d}"/></g>'), (-R-4, -R-4, 2*R+8, 2*R+8)

def wonly_GA():
    d, adv, bb = glyph(GRAZE, 'W')
    return f'<path d="{d}"/>', (0, -700, adv, 700)

# C — Graze title case "Weide" with willow-leaf tittle
def logo_GC(gap=None):
    gap = gap or {0: -46, 1: -14, 2: -10, 3: -14}
    gl, w = setw(GRAZE, list('Weide'), gap, kern_on=False)
    parts = []
    for n, x, d, adv, bb in gl:
        if n == 'i':
            stem = d[:d.index('Z') + 1]
            parts.append(f'<path transform="translate({x:.1f},0)" d="{stem}"/>')
            parts.append(f'<path class="accent" transform="translate({x:.1f},0)" d="{leaf(96, -600, 112, 22, -62)}"/>')
        else:
            parts.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>')
    return ''.join(parts), (0, -705, w, 712)

def sym_GC():
    d, adv, bb = glyph(GRAZE, 'i'); stem = d[:d.index('Z') + 1]
    return f'<path d="{stem}"/><path class="accent" d="{leaf(96, -600, 112, 22, -62)}"/>', (0, -665, 181, 670)

# B — Chambery caps, wide architectural tracking, cayenne I
def logo_CB(track=110):
    gl, w = setw(CHAMB, list('WEIDE'), {i: track for i in range(4)})
    parts = [f'<path {"class=\"accent\" " if n=="I" else ""}transform="translate({x:.1f},0)" d="{d}"/>' for n, x, d, adv, bb in gl]
    return ''.join(parts), (0, -700, w, 700)

# alternates
def simple(font, text, sp=None, box=(-760, 780)):
    gl, w = setw(font, list(text), sp)
    return ''.join(f'<path transform="translate({x:.1f},0)" d="{d}"/>' for n, x, d, adv, bb in gl), (0, box[0], w, box[1])

def text_path(font, s, track=0):
    """outlined English line for posters; returns (body, width) in font units"""
    x = 0; out = []
    for i, ch in enumerate(s):
        if ch == ' ':
            x += glyph(font, 'space')[1] if True else 250; continue
        d, adv, bb = glyph(font, ch); out.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>'); x += adv + track
        if i + 1 < len(s) and s[i+1] != ' ': x += kern(font, ch, s[i+1])
    return ''.join(out), x
