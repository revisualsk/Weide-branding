import math, random, os, sys
from logos import logo_A, logo_B, logo_C, symbol_A, symbol_B, symbol_C

CAY, GLA, COC, LIM, TRA = '#9D3F0D', '#9AB0AA', '#391B17', '#F2EDE5', '#DED6CA'
OUT = sys.argv[1]

LA, LB, LC = logo_A(), logo_B(), logo_C()
SA, SB, SC = symbol_A(), symbol_B(), symbol_C()

def strip_defs(body):
    return body.split('</defs>', 1)[1] if body.startswith('<defs>') else body

def mark(lg, fill, accent=None, h=None, w=None, pad=0, cls='mark', style=''):
    body, (x, y, bw, bh) = lg
    accent = accent or fill
    size = (f' height="{h}"' if h else '') + (f' width="{w}"' if w else '')
    return (f'<svg class="{cls}" style="--acc:{accent};{style}" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{x-pad} {y-pad} {bw+2*pad} {bh+2*pad}"{size} fill="{fill}" role="img" aria-label="WEIDE">'
            f'{strip_defs(body)}</svg>')

def nest(lg, fill, accent, x, y, w):
    """place a logo inside a parent 1920x1080 svg, by width"""
    body, (bx, by, bw, bh) = lg
    s = w / bw
    return (f'<g transform="translate({x},{y}) scale({s:.5f}) translate({-bx},{-by})" fill="{fill}" style="--acc:{accent}">'
            f'{strip_defs(body)}</g>')

def standalone(lg, fill, accent=None, pad=40):
    body, (x, y, bw, bh) = lg
    accent = accent or fill
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-pad} {y-pad} {bw+2*pad} {bh+2*pad}" fill="{fill}">'
            f'<style>.accent{{fill:{accent}}}</style>{body}</svg>')

GLOBAL_DEFS = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<clipPath id="aCut"><path d="M0 -700H600V-428H213V-212H600V100H0Z"/></clipPath>
<clipPath id="cCut"><path d="M-50 100V-505L372 -505L372 -604L512 -690V100Z"/></clipPath>
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

def grain(w=1920, h=1080, op=.22):
    return f'<rect width="{w}" height="{h}" fill="#fff" filter="url(#grain)" opacity="{op}" style="mix-blend-mode:overlay"/>'

# ---------------------------------------------------------------- HERO A
def hero_A():
    s = f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="hAbg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#47231d"/><stop offset=".55" stop-color="#391B17"/><stop offset="1" stop-color="#2b130f"/></linearGradient>
<radialGradient id="hAglow" cx=".5" cy="1" r=".8"><stop offset="0" stop-color="{CAY}" stop-opacity=".95"/><stop offset=".55" stop-color="#6a2a10" stop-opacity=".55"/><stop offset="1" stop-color="#2a120e" stop-opacity="0"/></radialGradient>
<linearGradient id="hAniche" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f0d0a"/><stop offset="1" stop-color="#2c140f"/></linearGradient>
<radialGradient id="hAsphere" cx=".34" cy=".3" r=".75"><stop offset="0" stop-color="#d6e0dc"/><stop offset=".35" stop-color="{GLA}"/><stop offset=".75" stop-color="#4c5a56"/><stop offset="1" stop-color="#1e1512"/></radialGradient>
<linearGradient id="hAbeam" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3e3" stop-opacity=".22"/><stop offset="1" stop-color="#fff3e3" stop-opacity="0"/></linearGradient>
<linearGradient id="hAplinth" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6b3a2c"/><stop offset=".5" stop-color="#4a241c"/><stop offset="1" stop-color="#2a130f"/></linearGradient>
</defs>
<rect width="1920" height="1080" fill="url(#hAbg)"/>
<rect width="1920" height="1080" fill="#000" filter="url(#plaster)" opacity=".5"/>
<path d="M250 1080V430A270 270 0 0 1 790 430V1080Z" fill="url(#hAniche)"/>
<path d="M250 1080V430A270 270 0 0 1 790 430V1080Z" fill="url(#hAglow)"/>
<path d="M250 430A270 270 0 0 1 790 430" fill="none" stroke="#5a2e24" stroke-width="2"/>
<rect x="395" y="780" width="250" height="300" fill="url(#hAplinth)"/>
<rect x="395" y="780" width="250" height="6" fill="#8a5a46" opacity=".7"/>
<ellipse cx="520" cy="782" rx="120" ry="14" fill="#140806" opacity=".55" filter="url(#soft)"/>
<circle cx="520" cy="660" r="120" fill="url(#hAsphere)"/>
<polygon points="1240,0 1560,0 700,1080 250,1080" fill="url(#hAbeam)" style="mix-blend-mode:screen"/>
<line x1="960" y1="140" x2="960" y2="940" stroke="{GLA}" stroke-width="1.2" opacity=".55"/>
{nest(LA, LIM, LIM, 1060, 420, 700)}
<text x="1062" y="600" class="t-sans" font-size="17" letter-spacing="7.5" fill="{GLA}">LONGEVITY &amp; REGENERATIVE HEALTH</text>
<text x="1060" y="860" class="t-cormorant-i" font-size="64" fill="{LIM}">Time, well kept.</text>
<text x="1062" y="910" class="t-sans" font-size="15" letter-spacing="4" fill="{LIM}" opacity=".6">AUSTRIA</text>
{grain()}
</svg>'''
    return s

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
<text x="1180" y="96" class="t-manrope-m" font-size="16" letter-spacing="6" fill="{COC}">LONGEVITY &amp; REGENERATIVE HEALTH</text>
<text x="1180" y="146" class="t-garamond-i" font-size="40" fill="{COC}">Built for the next fifty years.</text>
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
{nest(LC, LIM, COC, 130, 610, 780)}
<text x="140" y="900" class="t-dmsans" font-size="18" letter-spacing="7" fill="{LIM}">LONGEVITY &amp; REGENERATIVE HEALTH</text>
<text x="140" y="250" class="t-dmserif-i" font-size="58" fill="{LIM}">Regeneration is</text>
<text x="140" y="318" class="t-dmserif-i" font-size="58" fill="{LIM}">a daily practice.</text>
{grain(op=.2)}
</svg>'''
    return s

# ---------------------------------------------------------------- APPLICATIONS
def app_A():
    def card(x, y, rot, bg, fg, back=False):
        inner = (nest(LA, fg, fg, 170, 260, 510) if back else
                 f'''{nest(SA, fg, fg, 70, 70, 80)}
<text x="70" y="330" class="t-cormorant" font-size="44" fill="{fg}">Dr. Name Surname</text>
<text x="70" y="370" class="t-sans" font-size="15" letter-spacing="4" fill="{fg}" opacity=".75">LONGEVITY MEDICINE</text>
<text x="70" y="440" class="t-sans" font-size="16" letter-spacing="1" fill="{fg}" opacity=".75">+43 000 000 000 · name@weide.at</text>
<text x="780" y="440" text-anchor="end" class="t-sans" font-size="14" letter-spacing="4" fill="{fg}" opacity=".6">WEIDE</text>''')
        return f'''<g transform="translate({x},{y}) rotate({rot})" filter="url(#lift)"><rect width="850" height="550" rx="6" fill="{bg}"/>
<rect width="850" height="550" rx="6" fill="#fff" filter="url(#plaster)" opacity=".25"/>{inner}</g>'''
    return f'''<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="aStone" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a9bcb7"/><stop offset="1" stop-color="#7f958f"/></linearGradient>
<linearGradient id="aLight" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<rect width="1920" height="1080" fill="url(#aStone)"/>
<rect width="1920" height="1080" fill="#fff" filter="url(#stone)" opacity=".45"/>
{card(130, 300, -8, COC, 'url(#foil)', back=True)}
{card(1000, 400, 5, LIM, COC)}
<polygon points="0,0 900,0 300,1080 0,1080" fill="url(#aLight)"/>
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
<defs><linearGradient id="cBottle" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7f9790"/><stop offset=".22" stop-color="#c3d2ce"/><stop offset=".4" stop-color="{GLA}"/><stop offset="1" stop-color="#6e857f"/></linearGradient>
<linearGradient id="cCap" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2a120f"/><stop offset=".3" stop-color="#5a2e26"/><stop offset="1" stop-color="#24100d"/></linearGradient>
<linearGradient id="cWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a8460f"/><stop offset="1" stop-color="{CAY}"/></linearGradient></defs>
<rect width="1920" height="720" fill="url(#cWall)"/>
<rect y="720" width="1920" height="360" fill="{LIM}"/>
<rect y="720" width="1920" height="360" fill="#000" filter="url(#plaster)" opacity=".25"/>
<g opacity=".35">{willow(seed=21, x0=1250, x1=1960, n=14, scale=.8)}</g>
<ellipse cx="760" cy="905" rx="250" ry="34" fill="#391B17" opacity=".35" filter="url(#soft)"/>
<path d="M560 420Q560 380 600 380H920Q960 380 960 420V880Q960 910 930 910H590Q560 910 560 880Z" fill="url(#cBottle)"/>
<rect x="680" y="250" width="160" height="140" rx="10" fill="url(#cCap)"/>
<rect x="600" y="500" width="320" height="300" fill="{LIM}"/>
{nest(LC, COC, CAY, 640, 610, 240)}
<line x1="640" x2="880" y1="660" y2="660" stroke="{COC}" stroke-width="1" opacity=".4"/>
<text x="640" y="700" class="t-dmsans" font-size="15" letter-spacing="4" fill="{COC}">DAILY PROTOCOL</text>
<text x="640" y="730" class="t-dmserif-i" font-size="22" fill="{COC}">Magnesium · Glycine</text>
<text x="640" y="775" class="t-dmsans" font-size="13" letter-spacing="2" fill="{COC}" opacity=".6">60 CAPSULES · Nº 03</text>
<rect x="585" y="420" width="22" height="460" fill="#fff" opacity=".28" rx="10"/>
<g transform="translate(1150,600) rotate(-6)" filter="url(#lift)"><rect width="420" height="560" fill="{COC}"/>
{nest(SC, LIM, CAY, 60, 70, 46)}
<text x="60" y="300" class="t-dmserif-i" font-size="44" fill="{LIM}">Welcome</text><text x="60" y="350" class="t-dmserif-i" font-size="44" fill="{LIM}">to your first day.</text>
<text x="60" y="480" class="t-dmsans" font-size="14" letter-spacing="4" fill="{GLA}">YOUR PROGRAMME · WEEK 01</text></g>
{grain(op=.16)}
</svg>'''

# ---------------------------------------------------------------- MOOD TILES
def tile_svg(inner, bg):
    return f'<svg class="tile-art" viewBox="0 0 600 600" preserveAspectRatio="xMidYMid slice"><rect width="600" height="600" fill="{bg}"/>{inner}{grain(600,600,.18)}</svg>'

def tiles_A():
    return [
        ('Raking light on plaster', tile_svg(f'<rect width="600" height="600" fill="#000" filter="url(#plaster)" opacity=".6"/><polygon points="380,0 520,0 160,600 -60,600" fill="#fff3e3" opacity=".16"/><polygon points="430,0 470,0 60,600 10,600" fill="#fff3e3" opacity=".12"/>', COC)),
        ('Stone sphere, glass skin', tile_svg(f'<defs><radialGradient id="tAs" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#e3ebe8"/><stop offset=".4" stop-color="{GLA}"/><stop offset="1" stop-color="#1e1512"/></radialGradient></defs><ellipse cx="300" cy="470" rx="170" ry="18" fill="#000" opacity=".5" filter="url(#soft)"/><circle cx="300" cy="320" r="160" fill="url(#tAs)"/>', '#2b130f')),
        ('Bronze, hand-patinated', tile_svg('<rect width="600" height="600" fill="url(#bronze)"/><rect width="600" height="600" fill="#000" filter="url(#stone)" opacity=".35"/>', '#5a2f22')),
        ('Cayenne velvet', tile_svg(f'<defs><radialGradient id="tAv" cx=".3" cy=".2" r="1"><stop offset="0" stop-color="#c25a22"/><stop offset=".6" stop-color="{CAY}"/><stop offset="1" stop-color="#5a2007"/></radialGradient></defs><rect width="600" height="600" fill="url(#tAv)"/><path d="M0 380Q200 300 330 420T600 360V600H0Z" fill="#000" opacity=".22" filter="url(#soft)"/>', CAY)),
        ('Arched niche', tile_svg(f'<path d="M190 600V300A110 110 0 0 1 410 300V600Z" fill="#1d0c09"/><path d="M190 600V300A110 110 0 0 1 410 300V600Z" fill="{CAY}" opacity=".25"/>', '#47231d')),
        ('Cotton paper, blind deboss', tile_svg(f'<rect width="600" height="600" fill="#000" filter="url(#plaster)" opacity=".18"/>{nest(SA, "#e2d9cc", LIM, 170, 230, 260)}', LIM)),
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
        ('Seed & leaf', tile_svg(f'{nest(SC, COC, CAY, 245, 150, 110)}', TRA)),
        ('Cocoa ceramic', tile_svg(f'<defs><radialGradient id="tCk" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#6b3b31"/><stop offset="1" stop-color="#22100c"/></radialGradient></defs><ellipse cx="300" cy="300" rx="210" ry="210" fill="url(#tCk)"/><ellipse cx="300" cy="300" rx="150" ry="150" fill="#2a130f"/>', '#4a241c')),
        ('Water, slow', tile_svg(''.join(f'<path d="M0 {y}Q150 {y-14} 300 {y}T600 {y}" fill="none" stroke="#fff" stroke-opacity="{.12+.02*(i%5)}" stroke-width="2"/>' for i, y in enumerate(range(40, 600, 26))), '#86a09a')),
    ]

def moodgrid(tiles):
    return '<div class="mood">' + ''.join(f'<figure class="mt">{svg}<figcaption>{cap}</figcaption></figure>' for cap, svg in tiles) + '</div>'

def ratio(parts):
    return '<div class="ratio">' + ''.join(
        f'<div style="flex:{p};background:{c};color:{t}"><span>{n}</span><b>{p}%</b></div>' for n, c, p, t in parts) + '</div>'

# ---------------------------------------------------------------- SLIDES
DIR = {
 'A': dict(name='Editorial Luxury', code='Nocturne', logo=LA, sym=SA, acc_light=None, acc_dark=None,
   bg=COC, fg=LIM, sub=GLA,
   thesis='Dlhovekosť ako kultúra, nie ako služba. WEIDE vystupuje s pokojom súkromnej galérie: tmavé priestory, svetlo, ktoré modeluje formu, a typografia s kontrastom klasickej knihy.',
   logo_text=[('Prepletené W', 'Dve prekrývajúce sa V z Cormorant Garamond tvoria slučku. Odkazuje na vŕbové prútie (Weide = vŕba) a na kontinuitu.'),
              ('Dýchajúce E', 'Stredné rameno oboch E je odpojené od kmeňa a zúžené na vlasovú linku. Malá medzera dáva písmu vzduch a je to podpisový detail značky.'),
              ('Rytmus', 'Pre display veľkosti široký tracking +120 jednotiek s optickými korekciami W–E a D–E. Monogram W slúži ako pečať, favicon a slepotlač.')],
   type_pair=('Cormorant Garamond', 'DM Sans'),
   ratio=[('Bitter Cocoa', COC, 58, LIM), ('Limestone', LIM, 18, COC), ('Weathered Glass', GLA, 14, COC), ('Cayenne', CAY, 10, LIM)],
   words='Šero · Socha · Bronz · Ticho · Rituál',
   photo='Fotografia: šerosvit, telo ako socha v bočnom svetle, kameň a zamat. Teplé svetlo z jedného zdroja, hlboké tiene, 85 mm, veľa negatívneho priestoru.'),
 'B': dict(name='Architectural Modernism', code='Monolith', logo=LB, sym=SB, acc_light=CAY, acc_dark=CAY,
   bg=GLA, fg=COC, sub=COC,
   thesis='Dlhovekosť ako presná disciplína. WEIDE je postavená ako budova: modulárne litery na mriežke, travertín, denné svetlo a jediný kayenský stĺp, ktorý je ľudskou osou v systéme.',
   logo_text=[('Konštruované písmo', 'Vlastné litery na mriežke 700 jednotiek. Kmene 96, horizontály 80, rezy na vrcholoch W sú vodorovné ako kamenné bloky.'),
              ('Portál D', 'Oblúk D je rovnaký ako oblúk vstupu do budovy. Ten istý tvar sa vracia v symbole, signáži a fotografii.'),
              ('Stĺp I', 'I je jediný farebný prvok: kayenský stĺp, vitalita uprostred systému. V monochrome zostáva tvarom rovnaké.')],
   type_pair=('Manrope', 'EB Garamond Italic'),
   ratio=[('Weathered Glass', GLA, 44, COC), ('Travertine', TRA, 26, COC), ('Bitter Cocoa', COC, 22, LIM), ('Cayenne', CAY, 8, LIM)],
   words='Os · Travertín · Denné svetlo · Proporcia · Presnosť',
   photo='Fotografia: architektúra za denného svetla, dlhé tiene, symetria a ľudská postava v mierke budovy. Tilt-shift objektív, rovné perspektívy, chladné ráno.'),
 'C': dict(name='Contemporary Longevity', code='Living Willow', logo=LC, sym=SC, acc_light=CAY, acc_dark=CAY, acc_bg=COC,
   bg=CAY, fg=LIM, sub=LIM,
   thesis='Dlhovekosť ako každodenná vitalita. Malé písmená, teplá kayenská farba a živý list robia z WEIDE značku, ktorú ľudia nosia so sebou: v aplikácii, v rituáloch aj doma.',
   logo_text=[('List namiesto bodky', 'Bodka nad i je nahradená vŕbovým listom. Je to nový výhonok, regenerácia v najmenšej mierke.'),
              ('Šikmý rez d', 'Driek písmena d je zrezaný pod uhlom, ako vŕbový odrezok pripravený zakoreniť. Odkazuje na to, že vŕba vyrastie z jedného prútika.'),
              ('Mäkký kontrast', 'DM Serif Display s užším kerningom. Bohatý kontrast ťahov drží značku čitateľnú aj v 16 px a vo farbe pôsobí priateľsky a sebavedomo.')],
   type_pair=('DM Serif Display', 'DM Sans'),
   ratio=[('Cayenne', CAY, 52, LIM), ('Bitter Cocoa', COC, 22, LIM), ('Weathered Glass', GLA, 16, COC), ('Limestone', LIM, 10, COC)],
   words='Výhonok · Teplo · Pohyb · Koža · Ráno',
   photo='Fotografia: telo v pohybe, ranné slnko, vŕby pri vode, koža a ľan. Zrnitý film, teplé tóny posunuté do kayenskej, prirodzené momenty, žiadne pózovanie.'),
}

def slide(content, cls='', bg=None, fg=None, label='', num=None):
    st = f'background:{bg};color:{fg};' if bg else ''
    lab = f'<div class="folio"><span>WEIDE · Phase 1</span><span>{label}</span><span>{num:02d}</span></div>' if num else ''
    return f'<section class="sw"><div class="slide {cls}" style="{st}">{content}{lab}</div></section>'

slides = []
def add(content, cls='', bg=None, fg=None, label=''):
    slides.append((content, cls, bg, fg, label))

# 1 cover
add(f'''<div class="cover">
<div class="cover-top"><span>ReVisual — Brand Identity</span><span>Fáza 1 · Kreatívne smery</span></div>
<div class="cover-mid">
 <div class="cover-l"><p class="eyebrow">WEIDE — Longevity &amp; Regenerative Health</p><h1>Tri podoby<br/>jedného mena.<br/><em>WEIDE.</em></h1></div>
 <div class="cover-r">
  <div class="cv"><span>A</span>{mark(LA, LIM, h=None, w="100%")}</div>
  <div class="cv"><span>B</span>{mark(LB, LIM, CAY, w="78%")}</div>
  <div class="cv"><span>C</span>{mark(LC, LIM, CAY, w="62%")}</div>
 </div>
</div>
<div class="cover-bot"><span>Editorial Luxury</span><span>Architectural Modernism</span><span>Contemporary Longevity</span><span>Október 2026</span></div>
</div>''', bg=COC, fg=LIM)

# 2 strategy
add(f'''<div class="pad grid-2">
<div class="col"><p class="eyebrow">Kreatívna stratégia</p><h2>Názov už nesie celú myšlienku.</h2>
<p class="lead"><em>Weide</em> je po nemecky vŕba. Strom, ktorý stelesňuje všetko, čo má značka sľubovať, a pritom zostáva tichý a nenápadný.</p>
<div class="facts">
<div><b>Regenerácia</b><p>Z odrezaného vŕbového prútika zasadeného do zeme vyrastie nový strom.</p></div>
<div><b>Veda</b><p>Z vŕbovej kôry pochádza salicín, východisko pre vývoj aspirínu. Príroda a laboratórium v jednom príbehu.</p></div>
<div><b>Odolnosť</b><p>Vŕba sa vo víchrici ohne, ale nezlomí. Pružnosť je forma sily.</p></div>
<div><b>Pokoj</b><p>Rastie pri vode. Druhý význam slova Weide je pastvina, miesto oddychu.</p></div>
</div></div>
<div class="col pos">
<div class="pos-block"><p class="eyebrow">Brand idea</p><p class="big">Regenerácia,<br/>s precíznosťou.</p></div>
<div class="pos-rows">
<div><span>Positioning</span><p>WEIDE — Longevity &amp; Regenerative Health. Prémiové centrum preventívneho a regeneratívneho zdravia v Rakúsku.</p></div>
<div><span>Pre koho</span><p>Medzinárodne orientovaní ľudia, ktorí berú zdravie ako dlhodobú investíciu a cenia si diskrétnosť, odbornosť a krásu prostredia.</p></div>
<div><span>Tón</span><p>Pokojný, presný, kultivovaný, sebavedomý. Hovoríme menej, ale s istotou.</p></div>
<div><span>Napätie</span><p>Veda × príroda · presnosť × teplo · architektúra × ľudské telo. Každý smer rieši toto napätie inak.</p></div>
</div></div>
</div>''', bg=LIM, fg=COC, label='Stratégia')

# 3 palette
def sw(name, hexv, rgb, cmyk, role, txt, big=True):
    return f'''<div class="sw-card {'sw-big' if big else ''}" style="background:{hexv};color:{txt}">
<div><p class="sw-name">{name}</p><p class="sw-role">{role}</p></div>
<div class="sw-spec"><span>HEX {hexv}</span><span>RGB {rgb}</span><span>CMYK ≈ {cmyk}</span></div></div>'''
add(f'''<div class="pad pal">
<div class="pal-head"><p class="eyebrow">Povinná paleta</p><h2>Tri farby, tri úlohy.</h2></div>
<div class="pal-grid">
{sw('Cayenne Dust', CAY, '157 63 13', '0 60 92 38', 'Energia a vitalita. Akcent, ktorý sa pamätá.', LIM)}
{sw('Weathered Glass', GLA, '154 176 170', '13 0 3 31', 'Pokoj, regenerácia, čistota. Svetlo a vzduch.', COC)}
{sw('Bitter Cocoa', COC, '57 27 23', '0 53 60 78', 'Hĺbka, kontrast, prémiový charakter. Nosná farba písma.', LIM)}
<div class="neutrals">
{sw('Limestone', LIM, '242 237 229', '0 2 5 5', 'Teplá biela, papier a svetlo.', COC, False)}
{sw('Travertine', TRA, '222 214 202', '0 4 9 13', 'Minerálny neutrál, kameň.', COC, False)}
</div></div>
<div class="pal-notes"><span>Kontrast Cocoa na Limestone 13.4 : 1</span><span>Glass na Cocoa 6.8 : 1</span><span>Cayenne na Limestone 5.7 : 1</span><span>Cayenne na Glass 2.9 : 1, len pre veľké plochy, nie text</span><span>CMYK hodnoty sú orientačné, finálne sa overia nátlačkom</span></div>
</div>''', bg=LIM, fg=COC, label='Farby')

# 4 typography
fonts = [
 ('Cormorant Garamond', 'tf-cormorant', 'Najvyšší kontrast ťahov, dlhé serify, úzke proporcie. Najviac luxusu, ale pod 14 pt krehne.', 'Smer A · display'),
 ('EB Garamond', 'tf-ebgaramond', 'Robustnejší Garamond s pokojnou textúrou. Ideálny pre dlhý editoriálny text a citáty.', 'Smer B · akcent, kurzíva'),
 ('DM Serif Display', 'tf-dmserif', 'Silný kontrast, mäkké kvapkové koncovky, veľká x-výška. Najteplejší a najčitateľnejší v malom.', 'Smer C · display'),
 ('Manrope', 'tf-manrope', 'Široký, technický grotesk s otvorenými tvarmi. Pôsobí architektonicky a presne.', 'Smer B · text a UI'),
 ('DM Sans', 'tf-dmsans', 'Nízky kontrast, geometrický, neutrálny. Najlepší partner pre výrazný serif.', 'Smery A a C · text a UI'),
]
add('<div class="pad typo"><div class="typo-head"><p class="eyebrow">Typografické porovnanie</p><h2>Päť písiem, tri osobnosti.</h2></div><div class="typo-rows">' + ''.join(
 f'''<div class="trow"><div class="tname"><b>{n}</b><span>{use}</span></div><div class="tspec {c}"><span class="tbig">WEIDE weide</span><span class="tmid">Regeneration, made precise.</span></div><p class="tnote">{note}</p></div>'''
 for n, c, note, use in fonts) + '</div></div>', bg=LIM, fg=COC, label='Typografia')

# direction slides
heroes = {'A': hero_A(), 'B': hero_B(), 'C': hero_C()}
apps = {'A': app_A(), 'B': app_B(), 'C': app_C()}
tiles = {'A': tiles_A(), 'B': tiles_B(), 'C': tiles_C()}
small = {'A': ('cormorant', 'Time, well kept.'), 'B': ('manrope', 'Built for the next fifty years.'), 'C': ('dmserif', 'Regeneration is a daily practice.')}

for k in 'ABC':
    d = DIR[k]
    accL = d['acc_light'] or COC
    accD = d['acc_dark'] or LIM
    # intro
    add(f'''<div class="pad intro">
<div class="intro-l"><p class="dir-letter">{k}</p><p class="eyebrow">Smer {k} · {d["code"]}</p><h2>{d["name"]}</h2><p class="lead">{d["thesis"]}</p>
<p class="words">{d["words"]}</p>
<div class="pair"><span>Display — {d["type_pair"][0]}</span><span>Text — {d["type_pair"][1]}</span></div></div>
<div class="intro-r"><div class="intro-logo">{mark(d["logo"], d["fg"], d.get("acc_bg") or (d["acc_dark"] if d["bg"]!=GLA else d["acc_light"]), w="100%")}</div>
<p class="intro-tag {"tl-"+small[k][0]}">{small[k][1]}</p></div>
</div>''', bg=d['bg'], fg=d['fg'], label=f'Smer {k} · {d["name"]}')
    # logo system
    add(f'''<div class="logo-sys">
<div class="ls-light" style="background:{LIM}"><span class="cap">Svetlé pozadie</span>{mark(d["logo"], COC, accL, w="78%")}</div>
<div class="ls-dark" style="background:{COC}"><span class="cap" style="color:{GLA}">Tmavé pozadie</span>{mark(d["logo"], LIM, accD, w="78%")}</div>
<div class="ls-info" style="background:{LIM};color:{COC}">
 <div class="ls-notes">{''.join(f'<div><b>{t}</b><p>{p}</p></div>' for t, p in d["logo_text"])}</div>
 <div class="ls-tests">
  <div class="mono"><span class="cap">Monochróm</span><div class="mono-row"><div style="background:#fff">{mark(d["logo"], "#000", "#000", w="86%")}</div><div style="background:#000">{mark(d["logo"], "#fff", "#fff", w="86%")}</div></div></div>
  <div class="sizes"><span class="cap">Malé veľkosti · 14 / 20 / 28 px</span><div class="size-row">{mark(d["logo"], COC, accL, h="14")}{mark(d["logo"], COC, accL, h="20")}{mark(d["logo"], COC, accL, h="28")}</div></div>
  <div class="symb"><span class="cap">Symbol</span><div class="sym-row"><div style="background:{d["bg"] if d["bg"]!=GLA else GLA}">{mark(d["sym"], LIM if d["bg"]!=GLA else COC, (COC if k=="C" else CAY) if k!="A" else None, h="64%")}</div><div style="background:{LIM}">{mark(d["sym"], COC, accL, h="64%")}</div><div class="fav" style="background:{COC}">{mark(d["sym"], LIM, accD, h="16")}</div></div></div>
 </div>
</div></div>''', label=f'Smer {k} · Logo')
    # moodboard
    add(f'''<div class="pad moodslide">
<div class="mood-l"><p class="eyebrow">Smer {k} · Moodboard</p><h3>{d["code"]}</h3><p class="body">{d["photo"]}</p>
<p class="eyebrow ratio-lab">Pomer farieb</p>{ratio(d["ratio"])}</div>
{moodgrid(tiles[k])}
</div>''', bg=LIM, fg=COC, label=f'Smer {k} · Moodboard')
    # hero
    add(f'<div class="full">{heroes[k]}<span class="hero-cap">Hero vizuál · art-direction kompozícia</span></div>', label=f'Smer {k} · Hero', bg=COC, fg=LIM)
    # application
    add(f'<div class="full">{apps[k]}<span class="hero-cap">Aplikácia · {["Vizitky, slepotlač a fólia","Signáž, kovové litery na travertíne","Welcome kit, obal a karta"]["ABC".index(k)]}</span></div>', label=f'Smer {k} · Aplikácia', bg=COC, fg=LIM)

# comparison
cmp_rows = [
 ('Charakter', 'Galéria, ticho, šerosvit', 'Architektúra, systém, presnosť', 'Vitalita, teplo, každodennosť'),
 ('Najsilnejšie v', 'Tlač, interiér, premium print', 'Signáž, wayfinding, digitál', 'Sociálne siete, produkty, app'),
 ('Dominantná farba', 'Bitter Cocoa', 'Weathered Glass', 'Cayenne Dust'),
 ('Riziko', 'Môže pôsobiť ako hotel alebo móda', 'Môže pôsobiť chladne bez fotografie ľudí', 'Bližšie k wellness než k medicíne'),
]
add(f'''<div class="pad cmp">
<div class="cmp-head"><p class="eyebrow">Porovnanie a odporúčanie</p><h2>Vyberte smer.</h2></div>
<div class="cmp-grid">
<div class="cmp-logos"><div></div>
<div style="background:{COC}">{mark(LA, LIM, w="80%")}</div><div style="background:{GLA}">{mark(LB, COC, CAY, w="72%")}</div><div style="background:{CAY}">{mark(LC, LIM, COC, w="56%")}</div></div>
{''.join(f'<div class="cmp-row"><span>{r[0]}</span><p>{r[1]}</p><p>{r[2]}</p><p>{r[3]}</p></div>' for r in cmp_rows)}
</div>
<div class="reco"><b>Odporúčanie ReVisual</b><p>Smer A ako hlavná identita. Prepletené W je najoriginálnejší a najviac vlastniteľný detail, priamo spätý s významom mena, a serif zodpovedá preferencii elegantného typografického wordmarku. Do Fázy 2 odporúčame prevziať architektonický systém zo smeru B (oblúk, mriežka, signáž) ako sekundárny jazyk pre priestor.</p></div>
</div>''', bg=LIM, fg=COC, label='Rozhodnutie')

# prompts
P = {
 'A': ['Editorial campaign photograph for a premium longevity clinic, a monumental arched plaster niche in deep cocoa brown (#391B17), a single polished stone sphere on a bronze plinth, warm raking light from upper right, deep chiaroscuro shadows, a faint ember-orange glow (#9D3F0D) at the base, generous negative space on the right for a logo, shot on Phase One, 80mm, f/8, film grain, quiet luxury --ar 16:9 --style raw --v 7',
       'Sculptural black-and-cocoa portrait of a woman in her fifties, bare shoulders turned from camera, skin lit by a single warm window light like a classical marble statue, background soft weathered sage glass (#9AB0AA) out of focus, calm, dignified, editorial, 85mm --ar 4:5 --style raw --v 7'],
 'B': ['Architectural photograph of the entrance of a contemporary longevity centre in the Austrian Alps, travertine facade with a single tall arched portal, a slim cayenne-red (#9D3F0D) monolith column beside it casting a long morning shadow, soft weathered-glass sage sky (#9AB0AA), perfect symmetry, tilt-shift lens, large blank travertine wall for signage, minimal, quiet --ar 16:9 --style raw --v 7',
       'Interior of a premium diagnostic suite, travertine walls, blackened steel details, fluted sage glass partition, one person in a white robe standing small in the frame, daylight falling from a skylight, Scandinavian-Austrian minimalism, architectural digest style --ar 4:5 --style raw --v 7'],
 'C': ['Warm editorial photograph, a man and a woman in their forties walking barefoot through tall grass beside weeping willows at sunrise, golden cayenne-tinted light (#9D3F0D), soft sage mist (#9AB0AA), natural motion, linen clothing, 35mm film grain, candid, vital, hopeful --ar 16:9 --style raw --v 7',
       'Close-up still life on warm limestone surface, frosted sage-glass apothecary bottle with deep cocoa cap, a single fresh willow cutting with two leaves, morning sun shadows, terracotta wall behind, premium supplement brand photography, blank label for logo --ar 4:5 --style raw --v 7'],
}
add('<div class="pad prompts"><div class="pr-head"><p class="eyebrow">Fotografické podklady pre Fázu 2</p><h2>Prompty pre Midjourney / ChatGPT Images</h2><p class="body">Vizuály vo Fáze 1 sú vektorové art-direction kompozície postavené len z palety a presných log. Po výbere smeru vygenerujeme fotografické scény z týchto promptov a presné logo do nich vložíme ako vektor, nikdy ho negenerujeme.</p></div><div class="pr-grid">' + ''.join(
 f'<div class="pr-col"><p class="pr-k">Smer {k} · {DIR[k]["name"]}</p>' + ''.join(f'<p class="pr">{p}</p>' for p in P[k]) + '</div>' for k in 'ABC') + '</div></div>', bg=LIM, fg=COC, label='Prompty')

# next
add(f'''<div class="pad next">
<div><p class="eyebrow">Ďalší krok</p><h2>Čakáme na vaše rozhodnutie.</h2>
<p class="lead">Vyberte smer A, B alebo C, prípadne kombináciu, napríklad logo z A a priestorový systém z B. Až potom pokračujeme.</p></div>
<div class="next-cols">
<div><b>Fáza 2 po schválení</b><p>Finálne doladenie loga a kerningu · kompletná identita · brand manuál · 10 mockupov · fotografie z promptov s vloženým presným logom · Instagram carousel 10 × 1080 × 1350 px</p></div>
<div><b>Potrebujeme od vás</b><p>Screenshoty dvoch Instagram referencií. Odkazy sa z nášho prostredia nedajú otvoriť, preto boli smery postavené len na brief. Screenshoty použijeme na kalibráciu art direction pred Fázou 2.</p></div>
</div></div>''', bg=COC, fg=LIM, label='Ďalší krok')

# ---------------------------------------------------------------- PAGE
FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@300;400;500&family=DM+Serif+Display:ital@0;1&family=EB+Garamond:ital,wght@0,400;1,400&family=Manrope:wght@300;400;500;600&display=swap">'

CSS = open(os.path.join(os.path.dirname(__file__), 'deck.css')).read()

def page(local_fonts=None):
    head = f'<title>WEIDE Creative Directions</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
    head += (f'<style>{local_fonts}</style>' if local_fonts else FONT_LINK)
    head += f'<style>{CSS}</style>'
    body = GLOBAL_DEFS + '<main class="deck">' + ''.join(
        slide(c, cls, bg, fg, label, i + 1) for i, (c, cls, bg, fg, label) in enumerate(slides)) + '</main>'
    return head + body

open(os.path.join(OUT, 'index.html'), 'w').write(page())
# local-render variant
fd = os.environ.get('FONTDIR')
if fd:
    faces = []
    for fn, fam, w, st in [('CormorantGaramond-400', 'Cormorant Garamond', 400, 'normal'), ('CormorantGaramond-500', 'Cormorant Garamond', 500, 'normal'), ('CormorantGaramond-600', 'Cormorant Garamond', 600, 'normal'), ('CormorantGaramond-400i', 'Cormorant Garamond', 400, 'italic'), ('CormorantGaramond-500i', 'Cormorant Garamond', 500, 'italic'),
                           ('DMSans-300', 'DM Sans', 300, 'normal'), ('DMSans-400', 'DM Sans', 400, 'normal'), ('DMSans-500', 'DM Sans', 500, 'normal'),
                           ('DMSerifDisplay-400', 'DM Serif Display', 400, 'normal'), ('DMSerifDisplay-400i', 'DM Serif Display', 400, 'italic'),
                           ('EBGaramond-400', 'EB Garamond', 400, 'normal'), ('EBGaramond-400i', 'EB Garamond', 400, 'italic'),
                           ('Manrope-300', 'Manrope', 300, 'normal'), ('Manrope-400', 'Manrope', 400, 'normal'), ('Manrope-500', 'Manrope', 500, 'normal'), ('Manrope-600', 'Manrope', 600, 'normal')]:
        faces.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{fd}/{fn}.ttf')}}")
    open(os.path.join(OUT, 'render.html'), 'w').write('<!doctype html><meta charset="utf-8">' + page('\n'.join(faces)))

# standalone logo files
LD = os.path.join(OUT, 'logos'); os.makedirs(LD, exist_ok=True)
for k, lg, sy, acc in (('A', LA, SA, None), ('B', LB, SB, CAY), ('C', LC, SC, CAY)):
    for nm, f, a in (('cocoa', COC, acc), ('limestone', LIM, acc or LIM), ('black', '#000000', '#000000')):
        open(f'{LD}/WEIDE_{k}_wordmark_{nm}.svg', 'w').write(standalone(lg, f, a))
        open(f'{LD}/WEIDE_{k}_symbol_{nm}.svg', 'w').write(standalone(sy, f, a))
print(len(slides), 'slides')
