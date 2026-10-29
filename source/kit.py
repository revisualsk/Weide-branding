import math, random, os, sys
from logos import symbol_A
from logos2 import symbol_B2
from logos3 import logo_GA, logo_GC, logo_CB, mono_GA, wonly_GA, sym_GC, simple, text_path, GRAZE, CHAMB, LUX, QSERIF, QSCRIPT
from mat import MAT_DEFS, wax_blob

CAY, GLA, COC, LIM, TRA = '#9D3F0D', '#9AB0AA', '#391B17', '#D8C9B7', '#D8C9B7'

LA, LB, LC = logo_GA(), logo_CB(), logo_GC()
SA, SB, SC = wonly_GA(), symbol_B2(), sym_GC()
SEAL = mono_GA()

def strip_defs(body):
    return body.split('</defs>', 1)[1] if body.startswith('<defs>') else body

def mark(lg, fill, accent=None, h=None, w=None, pad=0, cls='mark', style=''):
    body, (x, y, bw, bh) = lg
    accent = accent or fill
    size = (f' height="{h}"' if h else '') + (f' width="{w}"' if w else '')
    return (f'<svg class="{cls}" style="--acc:{accent};{style}" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{x-pad} {y-pad} {bw+2*pad} {bh+2*pad}"{size} fill="{fill}" color="{fill}" role="img" aria-label="WEIDE">'
            f'{strip_defs(body)}</svg>')

def nest(lg, fill, accent, x, y, w):
    """place a logo inside a parent 1920x1080 svg, by width"""
    body, (bx, by, bw, bh) = lg
    s = w / bw
    col = f' color="{fill}"' if fill.startswith('#') else ''
    return (f'<g transform="translate({x},{y}) scale({s:.5f}) translate({-bx},{-by})" fill="{fill}"{col} style="--acc:{accent}">'
            f'{strip_defs(body)}</g>')

def standalone(lg, fill, accent=None, pad=40):
    body, (x, y, bw, bh) = lg
    accent = accent or fill
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-pad} {y-pad} {bw+2*pad} {bh+2*pad}" fill="{fill}">'
            f'<style>.accent{{fill:{accent}}}</style>{body}</svg>')

GLOBAL_DEFS = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<clipPath id="aCut"><path d="M0 -700H600V-428H213V-212H600V100H0Z"/></clipPath>
<clipPath id="gCutE"><path d="M-100 -800H500V-540H119V-390H500V100H-100Z"/></clipPath>
<clipPath id="cCut2"><path d="M-50 100V-560H300L460 -700V100Z"/></clipPath>
{MAT_DEFS}
<radialGradient id="wax" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#b8541d"/><stop offset=".7" stop-color="#9D3F0D"/><stop offset="1" stop-color="#6e2706"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="stone" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".0035 .045" numOctaves="4" seed="7"/><feColorMatrix values="0 0 0 0 .55  0 0 0 0 .47  0 0 0 0 .38  0 0 0 .9 -.32"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="plaster" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="5" seed="3"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 -.12"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="18"/></filter>
<filter id="softer" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
<filter id="lift" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="26" stdDeviation="22" flood-color="#1a0b08" flood-opacity=".45"/></filter>
<filter id="liftS" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="8" flood-color="#1a0b08" flood-opacity=".35"/></filter>
<filter id="relief" x="-5%" y="-5%" width="110%" height="120%"><feDropShadow dx="6" dy="9" stdDeviation="5" flood-color="#3a2a1c" flood-opacity=".42"/></filter>
<linearGradient id="bronze" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5a2f22"/><stop offset=".35" stop-color="#8a5a3f"/><stop offset=".5" stop-color="#c79a73"/><stop offset=".62" stop-color="#7a4a33"/><stop offset="1" stop-color="#3d1f17"/></linearGradient>
<linearGradient id="brushed" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4b2620"/><stop offset=".45" stop-color="#391B17"/><stop offset=".55" stop-color="#2a1210"/><stop offset="1" stop-color="#3f1e19"/></linearGradient>
<linearGradient id="foil" x1="0" y1="0" x2="1" y2=".4"><stop offset="0" stop-color="#c9b9a2"/><stop offset=".45" stop-color="#f6efe3"/><stop offset=".6" stop-color="#b9a68c"/><stop offset="1" stop-color="#e9dfcf"/></linearGradient>
<linearGradient id="copperfoil" x1="0" y1="0" x2="1" y2=".5"><stop offset="0" stop-color="#7d2f08"/><stop offset=".45" stop-color="#d27a45"/><stop offset=".6" stop-color="#9D3F0D"/><stop offset="1" stop-color="#c0612b"/></linearGradient>
</defs></svg>'''

def chrome(fg, op=.8, left='WEIDE® — LONGEVITY &amp; REGENERATIVE HEALTH', right='BRAND IDENTITY · PHASE 1', bl='DESIGNED BY REVISUAL', bm='2026 · AUSTRIA', br='© 2026 REVISUAL'):
    t = lambda x, y, s, a='start': f'<text x="{x}" y="{y}" text-anchor="{a}" class="t-dmsans" font-size="13" letter-spacing="2.6" fill="{fg}" opacity="{op}">{s}</text>'
    return t(60, 62, left) + t(1860, 62, right, 'end') + t(60, 1030, bl) + t(960, 1030, bm, 'middle') + t(1860, 1030, br, 'end')

def tags(x, y, words, fg, size=13):
    out = []; cx = x
    for w_ in words:
        w = len(w_) * size * .78 + 28
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.0f}" height="{size+15}" fill="none" stroke="{fg}" stroke-width="1"/><text x="{cx+w/2:.0f}" y="{y+size+5}" text-anchor="middle" class="t-dmsans" font-size="{size}" letter-spacing="2.4" fill="{fg}">{w_}</text>')
        cx += w
    return ''.join(out)

def outline(font, s, x, y, size, fill, anchor='start', track=0):
    body, w = text_path(font, s, track)
    sc = size / 1000; dx = {'start': 0, 'middle': -w * sc / 2, 'end': -w * sc}[anchor]
    return f'<g transform="translate({x + dx:.1f},{y}) scale({sc:.4f})" fill="{fill}">{body}</g>'

def grain(w=1920, h=1080, op=.22):
    return f'<rect width="{w}" height="{h}" fill="#fff" filter="url(#grain)" opacity="{op}" style="mix-blend-mode:overlay"/>'

# ---------------------------------------------------------------- HERO A
def hero_A():
    body, (bx, by, bw, bh) = LA
    W = 1640; s_ = W / bw; h = bh * s_
    rows = ''.join(f'<g transform="translate(140,{y:.0f}) scale({s_:.5f}) translate({-bx},{-by})" fill="none" stroke="#6a3a2e" stroke-width="{1.6/s_:.2f}">{strip_defs(body)}</g>'
                   for y in (150, 150 + h + 40, 150 + 2 * (h + 40)))
    return f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs>
<radialGradient id="hAbg" cx=".5" cy=".45" r=".75"><stop offset="0" stop-color="#4a241d"/><stop offset="1" stop-color="#2a130f"/></radialGradient>
<radialGradient id="hAglow" cx=".5" cy="1" r=".9"><stop offset="0" stop-color="{CAY}" stop-opacity=".95"/><stop offset=".6" stop-color="#5a230c" stop-opacity=".5"/><stop offset="1" stop-color="#1c0b08" stop-opacity="0"/></radialGradient>
<radialGradient id="hAsphere" cx=".34" cy=".3" r=".75"><stop offset="0" stop-color="#dfe8e4"/><stop offset=".35" stop-color="{GLA}"/><stop offset=".78" stop-color="#46524f"/><stop offset="1" stop-color="#1a1210"/></radialGradient>
<linearGradient id="hAplinth" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a4535"/><stop offset=".45" stop-color="#4a241c"/><stop offset="1" stop-color="#22100c"/></linearGradient>
<linearGradient id="hAbeam" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3e3" stop-opacity=".28"/><stop offset="1" stop-color="#fff3e3" stop-opacity="0"/></linearGradient>
<clipPath id="hAoval"><ellipse cx="960" cy="520" rx="240" ry="350"/></clipPath>
</defs>
<rect width="1920" height="1080" fill="url(#hAbg)"/>
<rect width="1920" height="1080" fill="#391B17" filter="url(#leather)" opacity=".55"/>
{''.join(f'<line x1="{x}" x2="{x}" y1="0" y2="1080" stroke="#4d271f" stroke-width="1"/>' for x in range(24, 1920, 48))}
{rows}
<g clip-path="url(#hAoval)">
<rect x="700" y="160" width="520" height="760" fill="#1d0c09"/>
<rect x="700" y="160" width="520" height="760" fill="url(#hAglow)"/>
<rect x="870" y="690" width="180" height="240" fill="url(#hAplinth)"/>
<ellipse cx="960" cy="692" rx="92" ry="10" fill="#0d0504" opacity=".6" filter="url(#soft)"/>
<circle cx="960" cy="600" r="92" fill="url(#hAsphere)"/>
<polygon points="1080,160 1230,160 830,920 700,920" fill="url(#hAbeam)" style="mix-blend-mode:screen"/>
</g>
<ellipse cx="960" cy="520" rx="240" ry="350" fill="none" stroke="{GLA}" stroke-width="1" opacity=".5"/>
{nest(LA, LIM, LIM, 845, 900, 230)}
{chrome(LIM, .7, bm='')}
{grain(op=.2)}
</svg>'''

# ---------------------------------------------------------------- HERO B
def hero_B():
    body, (bx, by, bw, bh) = LB
    W = 1000; s_ = W / bw
    joints = ''.join(f'<line x1="0" x2="1100" y1="{y}" y2="{y}" stroke="#b9ad9c" stroke-width="2"/>' for y in (180, 380, 580, 780))
    vj = ''.join(f'<line x1="{x}" x2="{x}" y1="{y0}" y2="{y0+200}" stroke="#b9ad9c" stroke-width="2"/>'
                 for x, y0 in ((240, 180), (860, 180), (520, 380), (140, 580), (980, 580), (420, 780)))
    s = f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="hBsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b2c4bf"/><stop offset="1" stop-color="{GLA}"/></linearGradient>
<linearGradient id="hBground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a9f99"/><stop offset="1" stop-color="#7d928c"/></linearGradient>
<linearGradient id="hBwall" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e6dfd4"/><stop offset="1" stop-color="#d6cdbf"/></linearGradient>
<linearGradient id="hBportal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c8d5d1"/><stop offset="1" stop-color="#8ea49e"/></linearGradient>
<linearGradient id="hBmono" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b0521c"/><stop offset=".55" stop-color="{CAY}"/><stop offset="1" stop-color="#7e300a"/></linearGradient>
<linearGradient id="hBshadow" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4f625d" stop-opacity=".75"/><stop offset="1" stop-color="#4f625d" stop-opacity=".1"/></linearGradient>
</defs>
<rect width="1920" height="1080" fill="url(#hBsky)"/>
<rect y="760" width="1920" height="320" fill="url(#hBground)"/>
<rect width="1100" height="760" fill="url(#hBwall)"/>
<rect width="1100" height="760" fill="#fff" filter="url(#stone)" opacity=".9"/>
<g clip-path="inset(0)">{joints}{vj}</g>
<path d="M600 760V420A150 150 0 0 1 900 420V760Z" fill="url(#hBportal)"/>
<path d="M600 760V420A150 150 0 0 1 900 420V760Z" fill="none" stroke="#9c8f7c" stroke-width="3"/>
<polygon points="900,760 1100,760 1100,700" fill="#b4a895" opacity=".6"/>
<polygon points="1460,760 1560,760 1920,940 1920,1010" fill="url(#hBshadow)"/>
<rect x="1460" y="250" width="100" height="510" fill="url(#hBmono)"/>
<rect x="1460" y="250" width="100" height="510" fill="#fff" filter="url(#plaster)" opacity=".35"/>
<g stroke="{COC}" stroke-width="1.4" fill="none" opacity=".75">
<line x1="1620" y1="250" x2="1620" y2="760"/><line x1="1608" y1="250" x2="1632" y2="250"/><line x1="1608" y1="760" x2="1632" y2="760"/>
<line x1="1460" y1="210" x2="1560" y2="210"/><line x1="1460" y1="200" x2="1460" y2="220"/><line x1="1560" y1="200" x2="1560" y2="220"/>
</g>
<text x="1642" y="512" class="t-manrope" font-size="15" letter-spacing="2" fill="{COC}">5 100</text>
<text x="1478" y="194" class="t-manrope" font-size="15" letter-spacing="2" fill="{COC}">1 000</text>
<text x="1180" y="788" class="t-manrope" font-size="14" letter-spacing="3" fill="{COC}" opacity=".8">± 0.00</text>
<g transform="translate(130,1010) scale({s_:.5f}) translate({-bx},0)" fill="{COC}" style="--acc:{CAY}">{body}</g>
<text x="1180" y="118" class="t-garamond-i" font-size="40" fill="{COC}">Built for the next fifty years.</text>
{tags(1182, 138, ["PRECISION", "REGENERATION", "VITALITY"], COC, 12)}
{chrome(COC, .75)}
{grain(op=.16)}
</svg>'''
    return s

# ---------------------------------------------------------------- HERO C
def willow(seed=4, x0=820, x1=1960, n=30, scale=1.0, leafcol=(COC, '#5a2a1e', GLA)):
    rnd = random.Random(seed); out = []
    for i in range(n):
        sx = x0 + (x1 - x0) * (i + rnd.random() * .8) / n
        L = rnd.uniform(380, 980) * scale
        sway = rnd.uniform(-90, 50) * scale
        pts = []
        for k in range(0, 41):
            t = k / 40
            x = sx + sway * t * t + 14 * math.sin(t * 3 + i)
            y = -30 + L * t
            pts.append((x, y))
        d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
        col = rnd.choice(leafcol[:2])
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{rnd.uniform(1.4,2.6):.1f}" opacity=".85"/>')
        side = 1
        for k in range(3, 41, 2):
            x, y = pts[k]; px, py = pts[k - 1]
            a = math.degrees(math.atan2(y - py, x - px))
            side = -side
            ll = rnd.uniform(34, 58) * scale * (0.6 + 0.4 * (k / 40))
            ang = a + side * rnd.uniform(14, 30)
            ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            w = ll * .16
            ex, ey = x + ll * ca, y + ll * sa
            nx, ny = -sa * w, ca * w
            mx, my = x + ll * .5 * ca, y + ll * .5 * sa
            fill = leafcol[2] if rnd.random() < .12 else rnd.choice(leafcol[:2])
            out.append(f'<path d="M{x:.1f} {y:.1f}Q{mx+nx:.1f} {my+ny:.1f} {ex:.1f} {ey:.1f}Q{mx-nx:.1f} {my-ny:.1f} {x:.1f} {y:.1f}Z" fill="{fill}" opacity="{rnd.uniform(.7,1):.2f}"/>')
    return ''.join(out)

def hero_C():
    s = f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs>
<radialGradient id="hCbg" cx=".25" cy=".8" r="1"><stop offset="0" stop-color="#b24a12"/><stop offset=".6" stop-color="{CAY}"/><stop offset="1" stop-color="#7d300a"/></radialGradient>
<radialGradient id="hCsun" cx=".42" cy=".38" r=".7"><stop offset="0" stop-color="#c5d4d0"/><stop offset=".7" stop-color="{GLA}"/><stop offset="1" stop-color="#86a09a"/></radialGradient>
</defs>
<rect width="1920" height="1080" fill="url(#hCbg)"/>
<rect width="1920" height="1080" fill="#000" filter="url(#plaster)" opacity=".35"/>
<circle cx="1390" cy="430" r="330" fill="url(#hCsun)"/>
<g opacity=".18" transform="translate(40,60)" filter="url(#soft)">{willow(seed=9, n=16, leafcol=("#2a0f08","#2a0f08","#2a0f08"))}</g>
<g>{willow()}</g>
{nest(LC, LIM, COC, 130, 590, 620)}
<text x="140" y="880" class="t-dmsans" font-size="18" letter-spacing="7" fill="{LIM}">LONGEVITY &amp; REGENERATIVE HEALTH</text>
{chrome(LIM, .75)}
{outline(QSCRIPT, 'Regeneration is', 140, 250, 96, LIM)}
{outline(QSCRIPT, 'a daily practice.', 190, 360, 96, LIM)}
{grain(op=.2)}
</svg>'''
    return s

# ---------------------------------------------------------------- APPLICATIONS
def app_A():
    return f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="aLight" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff2e2" stop-opacity=".14"/><stop offset=".55" stop-color="#fff2e2" stop-opacity="0"/></linearGradient>
<linearGradient id="aEdge" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3128"/><stop offset="1" stop-color="#2a130f"/></linearGradient></defs>
<rect width="1920" height="1080" fill="#2a130f"/>
<rect width="1920" height="1080" fill="#2a130f" filter="url(#leather)" opacity=".6"/>
<g transform="rotate(-7 960 540)">
 <rect x="330" y="120" width="1260" height="860" rx="14" fill="#140806" opacity=".55" filter="url(#softer)"/>
 <rect x="300" y="90" width="1260" height="860" rx="14" fill="url(#aEdge)"/>
 <rect x="300" y="84" width="1260" height="860" rx="14" fill="{COC}"/>
 <rect x="300" y="84" width="1260" height="860" rx="14" fill="{COC}" filter="url(#leather)"/>
 <rect x="330" y="114" width="1200" height="800" rx="8" fill="none" stroke="#2a120e" stroke-width="2" stroke-dasharray="9 7" opacity=".9"/>
 <g filter="url(#debossLeather)">{nest(LA, COC, COC, 560, 400, 740)}</g>
 <g filter="url(#debossLeather)"><text x="930" y="560" text-anchor="middle" class="t-dmsans" font-size="17" letter-spacing="9" fill="{COC}">LONGEVITY &amp; REGENERATIVE HEALTH</text></g>
</g>
<g filter="url(#liftS)"><g filter="url(#raise)"><path d="{wax_blob(1420, 770, 128, seed=5)}" fill="url(#wax)"/></g></g>
<g filter="url(#debossWax)">{nest(SEAL, CAY, CAY, 1320, 670, 200)}</g>
<g transform="translate(160,700) rotate(9)" filter="url(#lift)"><rect width="520" height="320" fill="{LIM}"/><rect width="520" height="320" fill="{LIM}" filter="url(#paper)"/>
<g filter="url(#deboss)">{nest(LA, LIM, LIM, 120, 135, 280)}</g>
<text x="260" y="250" text-anchor="middle" class="t-dmsans" font-size="10" letter-spacing="3.5" fill="{COC}" opacity=".7">DR. NAME SURNAME · LONGEVITY MEDICINE</text></g>
<rect width="1920" height="1080" fill="url(#aLight)"/>
{grain(op=.14)}
</svg>'''

def app_B():
    body, (bx, by, bw, bh) = LB
    W = 1180; s_ = W / bw
    return f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="bWall" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ebe5db"/><stop offset=".6" stop-color="#ddd4c6"/><stop offset="1" stop-color="#c9bfae"/></linearGradient>
<linearGradient id="bLight" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<rect width="1920" height="1080" fill="url(#bWall)"/>
<rect width="1920" height="1080" fill="#fff" filter="url(#stone)"/>
{''.join(f'<line x1="0" x2="1920" y1="{y}" y2="{y}" stroke="#bfb3a1" stroke-width="2"/>' for y in (150, 420, 690, 960))}
{''.join(f'<line x1="{x}" x2="{x}" y1="{y0}" y2="{y0+270}" stroke="#bfb3a1" stroke-width="2"/>' for x, y0 in ((380, 150), (1500, 150), (900, 420), (240, 690), (1660, 690)))}
<g filter="url(#relief)"><g transform="translate(370,640) scale({s_:.5f}) translate({-bx},0)" fill="url(#brushed)" style="--acc:url(#copperfoil)">{body}</g></g>
<g filter="url(#relief)"><rect x="1490" y="760" width="250" height="150" fill="{COC}"/></g>
<text x="1515" y="805" class="t-manrope-m" font-size="14" letter-spacing="4" fill="{LIM}">LEVEL 01</text>
<text x="1515" y="845" class="t-manrope" font-size="22" fill="{LIM}">Diagnostics</text>
<text x="1515" y="880" class="t-manrope" font-size="22" fill="{LIM}" opacity=".7">Recovery Suites →</text>
<polygon points="0,0 1920,0 1920,240 0,900" fill="url(#bLight)"/>
{grain(op=.12)}
</svg>'''

def app_C():
    return f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs><clipPath id="cPaper"><rect x="420" y="90" width="760" height="980"/></clipPath>
<linearGradient id="cLight" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<rect width="1920" height="1080" fill="{CAY}"/>
<rect width="1920" height="1080" fill="{CAY}" filter="url(#clay)"/>
<g filter="url(#lift)"><rect x="420" y="90" width="760" height="980" fill="{LIM}"/></g>
<rect x="420" y="90" width="760" height="980" fill="{LIM}" filter="url(#paper)"/>
<g clip-path="url(#cPaper)"><g filter="url(#deboss)" transform="translate(-260,40)">{willow(seed=11, x0=760, x1=1430, n=11, scale=1.05, leafcol=(LIM, LIM, LIM))}</g></g>
{nest(LC, COC, CAY, 560, 840, 300)}
<text x="562" y="1000" class="t-dmsans" font-size="12" letter-spacing="4" fill="{COC}" opacity=".75">LONGEVITY &amp; REGENERATIVE HEALTH</text>
<g transform="translate(1260,330) rotate(8)" filter="url(#lift)"><rect width="420" height="600" fill="{COC}"/><rect width="420" height="600" fill="{COC}" filter="url(#leather)" opacity=".6"/>
<g filter="url(#foilE)">{nest(LC, "url(#foil)", "url(#copperfoil)", 80, 300, 260)}</g>
{outline(QSCRIPT, 'Regeneration is a daily practice.', 210, 520, 34, GLA, 'middle')}</g>
<rect width="1920" height="1080" fill="url(#cLight)"/>
{grain(op=.14)}
</svg>'''

# ---------------------------------------------------------------- MOOD TILES
def tile_svg(inner, bg):
    return f'<svg class="tile-art" viewBox="0 0 600 600" preserveAspectRatio="xMidYMid slice"><rect width="600" height="600" fill="{bg}"/>{inner}{grain(600,600,.18)}</svg>'

def tiles_A():
    return [
        ('Raking light on plaster', tile_svg(f'<rect width="600" height="600" fill="#000" filter="url(#plaster)" opacity=".6"/><polygon points="380,0 520,0 160,600 -60,600" fill="#fff3e3" opacity=".16"/><polygon points="430,0 470,0 60,600 10,600" fill="#fff3e3" opacity=".12"/>', COC)),
        ('Stone sphere, glass skin', tile_svg(f'<defs><radialGradient id="tAs" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#e3ebe8"/><stop offset=".4" stop-color="{GLA}"/><stop offset="1" stop-color="#1e1512"/></radialGradient></defs><ellipse cx="300" cy="470" rx="170" ry="18" fill="#000" opacity=".5" filter="url(#soft)"/><circle cx="300" cy="320" r="160" fill="url(#tAs)"/>', '#2b130f')),
        ('Cocoa leather, deboss', tile_svg(f'<rect width="600" height="600" fill="{COC}" filter="url(#leather)"/><g filter="url(#debossLeather)">{nest(LA, COC, COC, 60, 270, 480)}</g>', COC)),
        ('Cayenne velvet', tile_svg(f'<defs><radialGradient id="tAv" cx=".3" cy=".2" r="1"><stop offset="0" stop-color="#c25a22"/><stop offset=".6" stop-color="{CAY}"/><stop offset="1" stop-color="#5a2007"/></radialGradient></defs><rect width="600" height="600" fill="url(#tAv)"/><path d="M0 380Q200 300 330 420T600 360V600H0Z" fill="#000" opacity=".22" filter="url(#soft)"/>', CAY)),
        ('Cayenne wax seal', tile_svg(f'<rect width="600" height="600" fill="{LIM}" filter="url(#paper)"/><g filter="url(#liftS)"><g filter="url(#raise)"><path d="{wax_blob(300, 300, 150, seed=8)}" fill="url(#wax)"/></g></g><g filter="url(#debossWax)">{nest(SEAL, CAY, CAY, 180, 180, 240)}</g>', LIM)),
        ('Cotton paper, blind deboss', tile_svg(f'<rect width="600" height="600" fill="{LIM}" filter="url(#paper)"/><g filter="url(#deboss)">{nest(SA, LIM, LIM, 150, 220, 300)}</g>', LIM)),
    ]

def tiles_B():
    return [
        ('Travertine, vein-cut', tile_svg('<rect width="600" height="600" fill="#fff" filter="url(#stone)"/>', '#e3dbcf')),
        ('Monolith & long shadow', tile_svg(f'<rect y="430" width="600" height="170" fill="#869b95"/><polygon points="330,430 380,430 600,520 600,560" fill="#4f625d" opacity=".55"/><rect x="330" y="120" width="50" height="310" fill="{CAY}"/>', GLA)),
        ('Weathered glass, fluted', tile_svg(''.join(f'<rect x="{x}" width="30" height="600" fill="#fff" opacity="{.05+.12*((x//30)%2)}"/>' for x in range(0, 600, 30)) + '<rect width="600" height="600" fill="#fff" opacity=".08"/>', GLA)),
        ('Section drawing', tile_svg(f'<g stroke="{COC}" fill="none" stroke-width="1.5"><path d="M120 520V260A180 180 0 0 1 480 260V520"/><path d="M200 520V280A100 100 0 0 1 400 280V520"/><line x1="60" x2="540" y1="520" y2="520"/><line x1="300" x2="300" y1="60" y2="560" stroke-dasharray="10 6"/></g><text x="70" y="560" class="t-manrope" font-size="18" letter-spacing="3" fill="{COC}">A — A  1:50</text>', LIM)),
        ('Blackened steel', tile_svg('<rect width="600" height="600" fill="url(#brushed)"/>' + ''.join(f'<line x1="0" x2="600" y1="{y}" y2="{y}" stroke="#fff" stroke-opacity=".035"/>' for y in range(0, 600, 4)), COC)),
        ('Daylight from above', tile_svg(f'<rect width="600" height="600" fill="#fff" filter="url(#stone)" opacity=".6"/><polygon points="200,0 400,0 470,600 130,600" fill="#fff" opacity=".35"/>', TRA)),
    ]

def tiles_C():
    return [
        ('Willow in motion', tile_svg(f'<g transform="translate(-700,-40) scale(1)">{willow(seed=5, x0=700, x1=1350, n=12, scale=.9)}</g>', GLA)),
        ('Sun-warmed clay', tile_svg(f'<defs><radialGradient id="tCc" cx=".3" cy=".25" r="1"><stop offset="0" stop-color="#c76a35"/><stop offset="1" stop-color="#7d300a"/></radialGradient></defs><rect width="600" height="600" fill="url(#tCc)"/><rect width="600" height="600" fill="#000" filter="url(#plaster)" opacity=".4"/>', CAY)),
        ('Skin, linen, morning light', tile_svg(f'<path d="M-20 420C120 300 240 480 380 380S560 300 640 340V620H-20Z" fill="#e7d7c6"/><path d="M-20 470C140 380 260 540 400 440S580 380 640 400V620H-20Z" fill="#d8c2ac"/><polygon points="420,0 600,0 600,200" fill="#fff" opacity=".35" filter="url(#soft)"/>', LIM)),
        ('Willow, blind deboss', tile_svg(f'<rect width="600" height="600" fill="{LIM}" filter="url(#paper)"/><g filter="url(#deboss)" transform="translate(-760,-60)">{willow(seed=13, x0=760, x1=1360, n=7, scale=.9, leafcol=(LIM, LIM, LIM))}</g>', LIM)),
        ('Cocoa ceramic', tile_svg(f'<defs><radialGradient id="tCk" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#6b3b31"/><stop offset="1" stop-color="#22100c"/></radialGradient></defs><ellipse cx="300" cy="300" rx="210" ry="210" fill="url(#tCk)"/><ellipse cx="300" cy="300" rx="150" ry="150" fill="#2a130f"/>', '#4a241c')),
        ('Water, slow', tile_svg(''.join(f'<path d="M0 {y}Q150 {y-14} 300 {y}T600 {y}" fill="none" stroke="#fff" stroke-opacity="{.12+.02*(i%5)}" stroke-width="2"/>' for i, y in enumerate(range(40, 600, 26))), '#86a09a')),
    ]

def moodgrid(tiles):
    return '<div class="mood">' + ''.join(f'<figure class="mt">{svg}<figcaption>{cap}</figcaption></figure>' for cap, svg in tiles) + '</div>'

def ratio(parts):
    return '<div class="ratio">' + ''.join(
        f'<div style="flex:{p};background:{c};color:{t}"><span>{n}</span><b>{p}%</b></div>' for n, c, p, t in parts) + '</div>'

