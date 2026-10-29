from mock2 import *

def ig(inner, defs=''):
    return f'<svg class="igs" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg"><defs>{SCENE_DEFS}{defs}</defs>{inner}</svg>'

def chrome_v(fg, n, op=.75):
    t = lambda x, y, s, a='start': f'<text x="{x}" y="{y}" text-anchor="{a}" class="t-sans" font-size="15" letter-spacing="3" fill="{fg}" opacity="{op}">{s}</text>'
    return t(56, 72, 'WEIDE® — BRAND IDENTITY') + t(1024, 72, 'REVISUAL', 'end') + t(56, 1300, 'LONGEVITY &amp; REGENERATIVE HEALTH') + t(1024, 1300, f'{n:02d} / 10', 'end')

def from_mock(fn, n, fg=LIM, cx=960):
    """crop a 1920x1080 mock into 4:5 around cx"""
    w = 1080 * 1080 / 1350
    old = 'class="art" viewBox="0 0 1920 1080"'
    new = f'class="art" width="1080" height="1350" viewBox="{cx - w/2:.0f} 0 {w:.0f} 1080"'
    inner = fn().replace(old, new, 1)
    return f'<svg class="igs" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{inner}{chrome_v(fg, n)}</svg>'

def s1():
    body, (bx, by, bw, bh) = LA
    s = 960 / bw
    pin = ''.join(f'<line x1="{x}" x2="{x}" y1="0" y2="1350" stroke="#4d271f" stroke-width="1"/>' for x in range(30, 1080, 40))
    return ig(f'''<rect width="1080" height="1350" fill="{COC}"/><rect width="1080" height="1350" fill="{COC}" filter="url(#leather)" opacity=".55"/>{pin}
<clipPath id="i1"><ellipse cx="540" cy="560" rx="250" ry="370"/></clipPath>
<g clip-path="url(#i1)"><rect x="290" y="190" width="500" height="740" fill="#1d0c09"/><rect x="290" y="190" width="500" height="740" fill="url(#hAglow)"/>
<rect x="450" y="760" width="180" height="200" fill="url(#hAplinth)"/><ellipse cx="540" cy="762" rx="92" ry="10" fill="#0d0504" opacity=".6"/><circle cx="540" cy="668" r="92" fill="url(#hAsphere)"/>
<polygon points="660,190 800,190 420,930 290,930" fill="#fff3e3" opacity=".14"/></g>
<ellipse cx="540" cy="560" rx="250" ry="370" fill="none" stroke="{GLA}" stroke-opacity=".5"/>
{nest(LA, LIM, LIM, 60, 880, 960)}
{chrome_v(LIM, 1)}{grain(1080, 1350, .18)}''')

def s2():
    wd, wadv, _ = glyph(GRAZE, 'W')
    return ig(f'''<rect width="1080" height="1350" fill="{LIM}"/><rect width="1080" height="1350" fill="{LIM}" filter="url(#paper)"/>
<g transform="translate(560,1350) scale(1.75)" fill="{GLA}" opacity=".55"><path d="{wd}"/></g>
<text x="80" y="300" class="t-sans" font-size="16" letter-spacing="4" fill="{CAY}">THE NAME</text>
<text x="76" y="420" class="t-cormorant" font-size="128" fill="{COC}">Weide</text>
<text x="80" y="490" class="t-cormorant-i" font-size="46" fill="{COC}">German for willow.</text>
{''.join(f'<text x="80" y="{y}" class="t-sans" font-size="15" letter-spacing="3.5" fill="{CAY}">{k}</text><text x="80" y="{y+40}" class="t-cormorant" font-size="34" fill="{COC}">{v}</text>' for y, k, v in ((640, 'REGENERATION', 'A cut branch takes root and grows again.'), (780, 'SCIENCE', 'Willow bark gave medicine salicin.'), (920, 'RESILIENCE', 'It bends in the storm and does not break.')))}
{chrome_v(COC, 2)}{grain(1080, 1350, .1)}''')

def s3():
    body, (bx, by, bw, bh) = LA
    s = 2600 / bw
    lab = lambda x1, y1, x2, y2, t, a='start': (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GLA}" stroke-width="1.2"/><circle cx="{x1}" cy="{y1}" r="5" fill="{GLA}"/>'
                                               f'<rect x="{x2 + (8 if a=="start" else -18 - len(t)*13.2):.0f}" y="{y2-16}" width="{len(t)*13.2+10:.0f}" height="30" fill="{COC}"/><text x="{x2 + (14 if a=="start" else -14)}" y="{y2+5}" text-anchor="{a}" class="t-sans" font-size="16" letter-spacing="3.5" fill="{LIM}">{t}</text>')
    return ig(f'''<rect width="1080" height="1350" fill="{COC}"/>
<g transform="translate(-180,1080) scale({s:.4f}) translate({-bx},0)" fill="{LIM}">{strip_defs(body)}</g>
<rect y="0" width="1080" height="200" fill="{COC}" opacity=".0"/>
{lab(360, 560, 520, 300, 'WOVEN W — WILLOW RODS')}
{lab(905, 1060, 760, 1160, 'FUSED SERIFS — CONTINUITY', 'end')}
{lab(1010, 640, 960, 420, 'BREATHING E', 'end')}
{chrome_v(LIM, 3)}{grain(1080, 1350, .14)}''')

def s4():
    body, (bx, by, bw, bh) = LA
    s = 760 / bw; h = bh * s
    rows = ''
    for i in range(4):
        y = 130 + i * (h + 22)
        fill = f'fill="{CAY}"' if i == 2 else f'fill="none" stroke="{COC}" stroke-width="{1.4/s:.2f}"'
        rows += f'<g transform="translate(160,{y:.0f}) scale({s:.5f}) translate({-bx},{-by})" {fill}>{strip_defs(body)}</g>'
    return ig(f'''<rect width="1080" height="1350" fill="{GLA}"/>{rows}{chrome_v(COC, 4)}{grain(1080, 1350, .12)}''')

def s5():
    bands = [(CAY, 'Cayenne Dust', '#9D3F0D', LIM, f'<rect width="540" height="290" fill="{CAY}" filter="url(#clay)"/>'),
             (GLA, 'Weathered Glass', '#9AB0AA', COC, ''.join(f'<rect x="{x}" width="14" height="290" fill="#fff" opacity="{.05 + .14 * ((x // 14) % 2)}"/>' for x in range(0, 540, 14))),
             (COC, 'Bitter Cocoa', '#391B17', LIM, f'<rect width="540" height="290" fill="{COC}" filter="url(#leather)"/>'),
             (LIM, 'Limestone', '#F2EDE5', COC, f'<rect width="540" height="290" fill="{LIM}" filter="url(#paper)"/>')]
    out = ''
    for i, (c, n, hx, t, mat) in enumerate(bands):
        y = 130 + i * 280
        out += f'''<g transform="translate(60,{y})"><svg width="480" height="260" viewBox="0 0 540 290" preserveAspectRatio="xMidYMid slice"><rect width="540" height="290" fill="{c}"/>{mat}</svg>
<rect x="480" width="480" height="260" fill="{c}"/><text x="940" y="56" text-anchor="end" class="t-cormorant" font-size="40" fill="{t}">{n}</text>
<text x="940" y="232" text-anchor="end" class="t-sans" font-size="14" letter-spacing="3" fill="{t}" opacity=".8">HEX {hx}</text></g>'''
    return ig(f'''<rect width="1080" height="1350" fill="{TRA}"/><rect width="1080" height="1350" fill="#fff" filter="url(#stone)" opacity=".5"/>{out}{chrome_v(COC, 5)}''')

def s7():
    return ig(f'''<rect width="1080" height="1350" fill="{COC}"/><rect width="1080" height="1350" fill="{COC}" filter="url(#leather)"/>
<g filter="url(#debossLeather)">{nest(LA, COC, COC, 120, 380, 840)}</g>
<g filter="url(#debossLeather)">{nest((descriptor()[0], (0, -720, descriptor()[1], 720)), COC, COC, 220, 720, 640)}</g>
<g filter="url(#liftS)"><g filter="url(#raise)"><path d="{wax_blob(540, 1010, 150, seed=6)}" fill="url(#wax)"/></g></g>
<g filter="url(#debossWax)">{nest(SEAL2, CAY, CAY, 425, 895, 230)}</g>
{chrome_v(LIM, 7)}{grain(1080, 1350, .12)}''')

def s9():
    return ig(f'''<rect width="1080" height="1350" fill="{CAY}"/><rect width="1080" height="1350" fill="{CAY}" filter="url(#clay)"/>
{phone(app_welcome(), 120, 260, 400, -5)}{phone(app_today(), 560, 220, 400, 4)}
{chrome_v(LIM, 9)}{grain(1080, 1350, .1)}''')

def s10():
    return ig(f'''<rect width="1080" height="1350" fill="{LIM}"/><rect width="1080" height="1350" fill="{LIM}" filter="url(#paper)"/>
<g filter="url(#deboss)" color="{LIM}">{nest(SEAL2, LIM, LIM, 290, 230, 500)}</g>
{nest(LOCK, COC, COC, 240, 840, 600)}
<text x="540" y="1225" text-anchor="middle" class="t-cormorant-i" font-size="40" fill="{COC}">Brand identity by ReVisual</text>
{chrome_v(COC, 10)}{grain(1080, 1350, .1)}''')

SLIDES = [s1, s2, s3, s4, s5, lambda: from_mock(m_entrance, 6), s7, lambda: from_mock(m_interior, 8, COC), s9, s10]
