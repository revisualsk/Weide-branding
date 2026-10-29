import math, random
from sys2 import *

SCENE_DEFS = f'''<radialGradient id="hAglow" cx=".5" cy="1" r=".9"><stop offset="0" stop-color="{CAY}" stop-opacity=".95"/><stop offset=".6" stop-color="#5a230c" stop-opacity=".5"/><stop offset="1" stop-color="#1c0b08" stop-opacity="0"/></radialGradient>
<radialGradient id="hAsphere" cx=".34" cy=".3" r=".75"><stop offset="0" stop-color="#dfe8e4"/><stop offset=".35" stop-color="{GLA}"/><stop offset=".78" stop-color="#46524f"/><stop offset="1" stop-color="#1a1210"/></radialGradient>
<linearGradient id="hAplinth" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a4535"/><stop offset=".45" stop-color="#4a241c"/><stop offset="1" stop-color="#22100c"/></linearGradient>'''

def art(inner, defs='', vb='0 0 1920 1080', cls='art'):
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"><defs>{SCENE_DEFS}{defs}</defs>{inner}</svg>'

def bronze_word(lg, x, y, w, fill='url(#bronze)', flt='relief'):
    return f'<g filter="url(#{flt})">{nest(lg, fill, fill, x, y, w)}</g>'

# ------------------------------------------------------------ M1 entrance
def m_entrance():
    joints = ''.join(f'<line x1="250" x2="1670" y1="{y}" y2="{y}" stroke="#b7aa97" stroke-width="2" opacity=".7"/>' for y in range(260, 900, 90))
    wing = lambda x0, x1: (f'<rect x="{x0}" y="470" width="{x1-x0}" height="430" fill="#d2c8b8"/><rect x="{x0}" y="470" width="{x1-x0}" height="430" fill="#fff" filter="url(#stone)" opacity=".7"/>'
                           + ''.join(f'<rect x="{x}" y="560" width="22" height="300" fill="url(#mGlow)" opacity=".9"/>' for x in range(x0 + 60, x1 - 40, 90)))
    defs = f'''<linearGradient id="mSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6d8580"/><stop offset=".55" stop-color="{GLA}"/><stop offset="1" stop-color="#d8c6ae"/></linearGradient>
<linearGradient id="mGlow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a1a12"/><stop offset=".55" stop-color="#8a3a12"/><stop offset="1" stop-color="#e2955a"/></linearGradient>
<linearGradient id="mPortal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c0b08"/><stop offset=".6" stop-color="#6e2c0c"/><stop offset="1" stop-color="#d9874c"/></linearGradient>
<linearGradient id="mPool" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f4f4b"/><stop offset="1" stop-color="#22302d"/></linearGradient>
<linearGradient id="mSpill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2955a" stop-opacity=".55"/><stop offset="1" stop-color="#e2955a" stop-opacity="0"/></linearGradient>
<linearGradient id="mFacade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ddd4c6"/><stop offset=".5" stop-color="#e9e2d6"/><stop offset="1" stop-color="#cfc4b3"/></linearGradient>'''
    inner = f'''<rect width="1920" height="1080" fill="url(#mSky)"/>
{wing(0, 330)}{wing(1590, 1920)}
<rect x="250" y="170" width="1420" height="730" fill="url(#mFacade)"/>
<rect x="250" y="170" width="1420" height="730" fill="#fff" filter="url(#stone)" opacity=".85"/>
{joints}
<rect x="250" y="170" width="1420" height="14" fill="#a99b86" opacity=".6"/>
<rect x="806" y="446" width="308" height="454" fill="#7d705f"/>
<rect x="830" y="470" width="260" height="430" fill="url(#mPortal)"/>
<rect x="830" y="470" width="20" height="430" fill="#000" opacity=".35"/>
{bronze_word(LA, 700, 250, 520)}
<rect x="0" y="900" width="1920" height="22" fill="#cfc3b1"/><rect x="0" y="922" width="1920" height="18" fill="#b9ac98"/><rect x="0" y="940" width="1920" height="16" fill="#a39581"/>
<polygon points="830,900 1090,900 1240,956 680,956" fill="url(#mSpill)"/>
<rect y="956" width="1920" height="124" fill="url(#mPool)"/>
<rect x="830" y="960" width="260" height="120" fill="url(#mPortal)" opacity=".35" filter="url(#soft)" transform="scale(1,-1) translate(0,-2036)"/>
<g opacity=".25" transform="translate(0,1912) scale(1,-1)"><rect x="250" y="832" width="1420" height="70" fill="#e9e2d6"/></g>
{''.join(f'<line x1="{x}" x2="{x+260}" y1="{y}" y2="{y}" stroke="#fff" stroke-opacity=".12" stroke-width="2"/>' for x, y in ((120, 990), (1300, 1010), (600, 1040), (1500, 1060)))}
{grain(op=.12)}'''
    return art(inner, defs)

# ------------------------------------------------------------ M2 signage pylon
def m_pylon():
    body, (bx, by, bw, bh) = LA
    defs = f'''<linearGradient id="pSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9c8c4"/><stop offset="1" stop-color="{GLA}"/></linearGradient>
<linearGradient id="pFront" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4a2620"/><stop offset="1" stop-color="#2f1612"/></linearGradient>
<linearGradient id="pGround" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfc6b8"/><stop offset="1" stop-color="#e6dfd3"/></linearGradient>'''
    paving = ''.join(f'<line x1="960" y1="760" x2="{x}" y2="1080" stroke="#b9ae9d" stroke-width="1.5"/>' for x in range(-1600, 3600, 260))
    paving += ''.join(f'<line x1="0" x2="1920" y1="{y}" y2="{y}" stroke="#b9ae9d" stroke-width="1.5"/>' for y in (790, 830, 885, 960, 1060))
    s = 560 / bw
    inner = f'''<rect width="1920" height="1080" fill="url(#pSky)"/>
<rect y="760" width="1920" height="320" fill="url(#pGround)"/>
<rect y="760" width="1920" height="320" fill="#fff" filter="url(#stone)" opacity=".5"/>
{paving}
<polygon points="1060,900 1130,860 1840,1080 1500,1080" fill="#5d5247" opacity=".28" filter="url(#soft)"/>
<polygon points="1060,180 1130,140 1130,860 1060,900" fill="#22100c"/>
<rect x="840" y="180" width="220" height="720" fill="url(#pFront)"/>
<rect x="840" y="180" width="220" height="720" fill="#fff" filter="url(#plaster)" opacity=".18"/>
<polygon points="840,180 1060,180 1130,140 910,140" fill="#5a2f26"/>
<g filter="url(#embossS)"><g transform="translate(1048,250) rotate(90) scale({s:.4f}) translate({-bx},{-by})" fill="url(#foil)">{strip_defs(body)}</g></g>
<rect x="840" y="860" width="220" height="40" fill="{CAY}"/>
<g opacity=".95">{willow(seed=31, x0=-120, x1=560, n=14, scale=1.05)}</g>
<rect x="300" y="700" width="260" height="140" fill="{COC}" filter="url(#liftS)"/>
<text x="322" y="740" class="t-sans" font-size="12" letter-spacing="3.5" fill="{GLA}">ENTRANCE · LEVEL 00</text>
<text x="322" y="780" class="t-cormorant" font-size="28" fill="{LIM}">Reception</text>
<text x="322" y="815" class="t-sans" font-size="14" fill="{LIM}" opacity=".75">Diagnostics → Regeneration</text>
<line x1="430" x2="430" y1="840" y2="900" stroke="#3a2a22" stroke-width="5"/>
{grain(op=.12)}'''
    return art(inner, defs)

# ------------------------------------------------------------ M3 stationery
def m_stationery():
    lines = ''.join(f'<rect x="70" y="{y}" width="{w}" height="5" fill="{COC}" opacity=".18"/>' for y, w in zip(range(330, 600, 22), (420, 400, 410, 300, 0, 420, 415, 390, 405, 260, 0, 200)))
    inner = f'''<rect width="1920" height="1080" fill="{GLA}"/>
<rect width="1920" height="1080" fill="{GLA}" filter="url(#paper)"/>
<g transform="translate(200,80) rotate(-3)" filter="url(#lift)"><rect width="560" height="792" fill="{LIM}"/><rect width="560" height="792" fill="{LIM}" filter="url(#paper)"/>
{nest(LOCK, COC, COC, 190, 70, 180)}
<text x="70" y="270" class="t-sans" font-size="11" letter-spacing="2" fill="{COC}" opacity=".6">VIENNA, 29 OCTOBER 2026</text>
{lines}
<line x1="70" x2="490" y1="720" y2="720" stroke="{COC}" stroke-opacity=".25"/>
<text x="70" y="745" class="t-sans" font-size="9.5" letter-spacing="2" fill="{COC}" opacity=".7">WEIDE · LONGEVITY &amp; REGENERATIVE HEALTH · AUSTRIA · WEIDE.AT</text></g>
<g transform="translate(860,120) rotate(4)" filter="url(#lift)"><rect width="700" height="350" fill="{COC}"/><rect width="700" height="350" fill="{COC}" filter="url(#leather)" opacity=".5"/>
<path d="M0 0L350 210L700 0" fill="none" stroke="#1f0d0a" stroke-width="2"/>
<g filter="url(#liftS)"><g filter="url(#raise)"><path d="{wax_blob(350, 212, 62, seed=4)}" fill="url(#wax)"/></g></g>
<g filter="url(#debossWax)">{nest(SEAL2, CAY, CAY, 300, 162, 100)}</g>
<g filter="url(#foilE)">{nest(LA, "url(#foil)", "url(#foil)", 40, 300, 110)}</g></g>
<g transform="translate(890,610) rotate(-6)" filter="url(#lift)"><rect width="440" height="280" fill="{COC}"/><rect width="440" height="280" fill="{COC}" filter="url(#leather)" opacity=".5"/>
<g filter="url(#foilE)">{nest(LA, "url(#foil)", "url(#foil)", 120, 100, 200)}</g></g>
<g transform="translate(1340,600) rotate(7)" filter="url(#lift)"><rect width="440" height="280" fill="{LIM}"/><rect width="440" height="280" fill="{LIM}" filter="url(#paper)"/>
<g filter="url(#deboss)">{nest(SA, LIM, LIM, 34, 30, 34)}</g>
<text x="34" y="190" class="t-cormorant" font-size="27" fill="{COC}">Dr. Name Surname</text>
<text x="34" y="215" class="t-sans" font-size="9.5" letter-spacing="2.6" fill="{COC}" opacity=".7">LONGEVITY MEDICINE</text>
<text x="34" y="250" class="t-sans" font-size="10" letter-spacing="1" fill="{COC}" opacity=".7">+43 000 000 000 · name@weide.at</text></g>
{grain(op=.12)}'''
    return art(inner)

# ------------------------------------------------------------ M4 interior
def m_interior():
    VP = (960, 520)
    L, Rr, T, B = 560, 1360, 250, 790
    tiles = ''.join(f'<line x1="{VP[0] + (x - VP[0]) * (B - VP[1]) / (1080 - VP[1]):.1f}" y1="{B}" x2="{x}" y2="1080" stroke="#b9ae9d" stroke-width="1.4"/>' for x in range(-1400, 3400, 240))
    tiles += ''.join(f'<line x1="0" x2="1920" y1="{y}" y2="{y}" stroke="#b9ae9d" stroke-width="1.4"/>' for y in (812, 846, 900, 985))
    flutes = ''
    for i in range(0, 22):
        t = i / 22; x = L * t
        ytop = T * t; ybot = 1080 - (1080 - B) * t
        flutes += f'<line x1="{x:.1f}" y1="{ytop:.1f}" x2="{x:.1f}" y2="{ybot:.1f}" stroke="#fff" stroke-opacity=".28" stroke-width="{6 - 4 * t:.1f}"/>'
    panels = ''.join(f'<line x1="{1920 - (1920 - Rr) * t:.1f}" y1="{T * t:.1f}" x2="{1920 - (1920 - Rr) * t:.1f}" y2="{1080 - (1080 - B) * t:.1f}" stroke="#1d0c09" stroke-width="2"/>' for t in (.2, .45, .66, .85))
    defs = f'''<linearGradient id="iFloor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfc6b8"/><stop offset="1" stop-color="#e7e0d4"/></linearGradient>
<linearGradient id="iGlass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9fb5af"/><stop offset="1" stop-color="#b9cac5"/></linearGradient>
<linearGradient id="iWood" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#3a1b16"/><stop offset="1" stop-color="#55291f"/></linearGradient>
<linearGradient id="iBack" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8e1d5"/><stop offset="1" stop-color="#d9cfbf"/></linearGradient>'''
    inner = f'''<rect width="1920" height="1080" fill="{LIM}"/>
<polygon points="0,0 1920,0 {Rr},{T} {L},{T}" fill="#ece6dc"/>
<polygon points="{L+120},{T-60} {Rr-120},{T-60} {Rr-170},{T-30} {L+170},{T-30}" fill="#fff8ec"/>
<polygon points="0,1080 1920,1080 {Rr},{B} {L},{B}" fill="url(#iFloor)"/>{tiles}
<rect x="{L}" y="{T}" width="{Rr-L}" height="{B-T}" fill="url(#iBack)"/>
<rect x="{L}" y="{T}" width="{Rr-L}" height="{B-T}" fill="#fff" filter="url(#stone)" opacity=".8"/>
{bronze_word(LOCK, 780, 360, 360)}
<text x="{Rr-40}" y="{B-40}" text-anchor="end" class="t-sans" font-size="11" letter-spacing="3" fill="{COC}" opacity=".7">DIAGNOSTICS · ROOM 02</text>
<polygon points="0,0 {L},{T} {L},{B} 0,1080" fill="url(#iGlass)"/>{flutes}
<polygon points="1920,0 {Rr},{T} {Rr},{B} 1920,1080" fill="url(#iWood)"/>{panels}
<polygon points="760,860 1160,860 1110,800 810,800" fill="#efe9df"/>
<rect x="760" y="860" width="400" height="60" fill="#d8cfc1"/>
<rect x="800" y="920" width="320" height="40" fill="#8f8170"/>
<polygon points="790,812 1130,812 1110,800 810,800" fill="#fff" opacity=".6"/>
<ellipse cx="960" cy="985" rx="260" ry="20" fill="#3a2a22" opacity=".25" filter="url(#soft)"/>
<rect x="700" y="660" width="60" height="140" fill="{CAY}"/>
<polygon points="0,0 700,0 300,1080 0,1080" fill="#fff" opacity=".08"/>
{grain(op=.1)}'''
    return art(inner, defs)

# ------------------------------------------------------------ screen designs (web + app)
def web_screen():
    body, (bx, by, bw, bh) = LA
    s = 1100 / bw; h = bh * s
    rows = ''.join(f'<g transform="translate(170,{y:.0f}) scale({s:.5f}) translate({-bx},{-by})" fill="none" stroke="#5b2f25" stroke-width="{1.4/s:.2f}">{strip_defs(body)}</g>' for y in (90, 90 + h + 24))
    menu = ''.join(f'<text x="{x}" y="46" class="t-sans" font-size="11" letter-spacing="2.4" fill="{LIM}" opacity=".85">{t}</text>' for x, t in ((470, 'PROGRAMMES'), (600, 'DIAGNOSTICS'), (735, 'REGENERATION'), (880, 'THE HOUSE'), (990, 'JOURNAL')))
    cards = ''.join(f'''<g transform="translate({x},640)"><rect width="420" height="170" fill="{c}"/><text x="28" y="50" class="t-sans" font-size="10" letter-spacing="2.4" fill="{f}" opacity=".7">{e}</text><text x="28" y="96" class="t-cormorant" font-size="34" fill="{f}">{t}</text></g>'''
                    for x, c, f, e, t in ((40, LIM, COC, 'ASSESS', 'Diagnostics'), (510, GLA, COC, 'RESTORE', 'Regeneration'), (980, CAY, LIM, 'SUSTAIN', 'Longevity Programmes')))
    return f'''<svg viewBox="0 0 1440 810" width="1440" height="810">
<rect width="1440" height="810" fill="{COC}"/><rect width="1440" height="610" fill="{COC}" filter="url(#leather)" opacity=".55"/>
{rows}
{nest(LA, LIM, LIM, 40, 30, 92)}{menu}
<rect x="1220" y="26" width="180" height="32" fill="none" stroke="{LIM}" stroke-opacity=".7"/><text x="1310" y="47" text-anchor="middle" class="t-sans" font-size="11" letter-spacing="2" fill="{LIM}">BOOK A CONSULTATION</text>
<clipPath id="wOval"><ellipse cx="420" cy="340" rx="150" ry="215"/></clipPath>
<g clip-path="url(#wOval)"><rect x="270" y="120" width="300" height="440" fill="#1d0c09"/><rect x="270" y="120" width="300" height="440" fill="url(#hAglow)"/>
<rect x="370" y="430" width="100" height="140" fill="url(#hAplinth)"/><circle cx="420" cy="380" r="54" fill="url(#hAsphere)"/>
<polygon points="490,120 560,120 360,560 300,560" fill="#fff3e3" opacity=".12"/></g>
<ellipse cx="420" cy="340" rx="150" ry="215" fill="none" stroke="{GLA}" stroke-opacity=".5"/>
<text x="700" y="290" class="t-cormorant-i" font-size="84" fill="{LIM}">Time, well kept.</text>
<text x="704" y="340" class="t-sans" font-size="16" fill="{LIM}" opacity=".8">Precise diagnostics, regenerative therapies and a personal plan</text>
<text x="704" y="364" class="t-sans" font-size="16" fill="{LIM}" opacity=".8">for the decades ahead. In the calm of an Austrian house.</text>
<rect x="704" y="400" width="240" height="46" fill="{CAY}"/><text x="824" y="428" text-anchor="middle" class="t-sans" font-size="12" letter-spacing="2.4" fill="{LIM}">BEGIN YOUR ASSESSMENT</text>
<text x="968" y="428" class="t-sans" font-size="12" letter-spacing="2.4" fill="{LIM}" opacity=".8">EXPLORE THE HOUSE →</text>
<rect y="610" width="1440" height="200" fill="{LIM}"/>{cards}
</svg>'''

def phone(screen_svg, x, y, w=330, rot=0):
    h = w * 844 / 390
    return f'''<g transform="translate({x},{y}) rotate({rot})" filter="url(#lift)"><rect width="{w}" height="{h:.0f}" rx="{w*.14:.0f}" fill="#141010"/>
<svg x="{w*.035:.1f}" y="{w*.035:.1f}" width="{w*.93:.1f}" height="{h - w*.07:.1f}" viewBox="0 0 390 844" preserveAspectRatio="xMidYMid slice"><clipPath id="sc{x}"><rect width="390" height="844" rx="48"/></clipPath><g clip-path="url(#sc{x})">{screen_svg}</g></svg>
<rect x="{w/2 - w*.16:.1f}" y="{w*.06:.1f}" width="{w*.32:.1f}" height="{w*.085:.1f}" rx="{w*.04:.1f}" fill="#000"/></g>'''

def app_welcome():
    return f'''<rect width="390" height="844" fill="{COC}"/><rect width="390" height="844" fill="{COC}" filter="url(#leather)" opacity=".6"/>
{nest(SEAL2, LIM, LIM, 95, 250, 200)}
<text x="195" y="540" text-anchor="middle" class="t-cormorant-i" font-size="38" fill="{LIM}">Welcome back.</text>
<text x="195" y="575" text-anchor="middle" class="t-sans" font-size="13" fill="{LIM}" opacity=".7">Your day at WEIDE is ready.</text>
<rect x="60" y="700" width="270" height="52" fill="{CAY}"/><text x="195" y="731" text-anchor="middle" class="t-sans" font-size="12" letter-spacing="2.4" fill="{LIM}">TODAY'S RITUAL</text>'''

def app_today():
    items = [('07:00', 'Cold immersion', '3 min · Water house', True), ('08:30', 'Breakfast', 'Seasonal menu', True), ('11:00', 'Consultation', 'Dr. Name Surname', False), ('15:00', 'Infrared sauna', '25 min', False), ('18:30', 'Breathwork', 'Studio 2', False)]
    rows = ''
    for i, (t, a, b, done) in enumerate(items):
        y = 300 + i * 92
        rows += f'''<line x1="32" x2="358" y1="{y-30}" y2="{y-30}" stroke="{COC}" stroke-opacity=".12"/>
<text x="32" y="{y}" class="t-sans" font-size="13" fill="{COC}" opacity=".6">{t}</text>
<text x="100" y="{y}" class="t-cormorant" font-size="24" fill="{COC}">{a}</text>
<text x="100" y="{y+22}" class="t-sans" font-size="12" fill="{COC}" opacity=".6">{b}</text>
<circle cx="346" cy="{y-6}" r="11" fill="{CAY if done else 'none'}" stroke="{CAY}" stroke-width="1.5"/>'''
    return f'''<rect width="390" height="844" fill="{LIM}"/>
{nest(LA, COC, COC, 32, 70, 70)}
<text x="32" y="170" class="t-cormorant" font-size="46" fill="{COC}">Today</text>
<text x="32" y="200" class="t-sans" font-size="12" letter-spacing="2.4" fill="{COC}" opacity=".6">THURSDAY · 2 OF 5 COMPLETE</text>
<circle cx="330" cy="168" r="26" fill="none" stroke="{COC}" stroke-opacity=".12" stroke-width="4"/>
<circle cx="330" cy="168" r="26" fill="none" stroke="{CAY}" stroke-width="4" stroke-dasharray="65 200" transform="rotate(-90 330 168)"/>
{rows}
<rect y="770" width="390" height="74" fill="#fff" opacity=".5"/>
{''.join(f'<circle cx="{x}" cy="800" r="5" fill="{COC}" opacity="{o}"/>' for x, o in ((80, 1), (160, .3), (240, .3), (310, .3)))}'''

def app_programme():
    return f'''<rect width="390" height="844" fill="{GLA}"/>
<clipPath id="aOv"><ellipse cx="195" cy="280" rx="140" ry="190"/></clipPath>
<g clip-path="url(#aOv)"><rect x="55" y="90" width="280" height="380" fill="#1d0c09"/><rect x="55" y="90" width="280" height="380" fill="url(#hAglow)"/>
<rect x="150" y="360" width="90" height="120" fill="url(#hAplinth)"/><circle cx="195" cy="318" r="46" fill="url(#hAsphere)"/></g>
<text x="32" y="540" class="t-sans" font-size="12" letter-spacing="2.4" fill="{COC}" opacity=".7">PROGRAMME · 7 DAYS</text>
<text x="32" y="590" class="t-cormorant" font-size="40" fill="{COC}">Regeneration</text>
<text x="32" y="625" class="t-sans" font-size="13" fill="{COC}" opacity=".75">Diagnostics, recovery therapies and</text>
<text x="32" y="645" class="t-sans" font-size="13" fill="{COC}" opacity=".75">a personal plan to take home.</text>
<rect x="32" y="700" width="326" height="52" fill="{COC}"/><text x="195" y="731" text-anchor="middle" class="t-sans" font-size="12" letter-spacing="2.4" fill="{LIM}">REQUEST DATES</text>'''

def m_web():
    inner = f'''<rect width="1920" height="1080" fill="{TRA}"/><rect width="1920" height="1080" fill="#fff" filter="url(#stone)" opacity=".6"/>
<polygon points="0,0 900,0 400,1080 0,1080" fill="#fff" opacity=".12"/>
<ellipse cx="960" cy="1000" rx="520" ry="26" fill="#3a2a22" opacity=".3" filter="url(#soft)"/>
<rect x="890" y="880" width="140" height="110" fill="#b8b1a6"/><rect x="760" y="985" width="400" height="16" rx="6" fill="#a59d91"/>
<g filter="url(#lift)"><rect x="232" y="70" width="1456" height="836" rx="18" fill="#141010"/></g>
<svg x="252" y="90" width="1416" height="796" viewBox="0 0 1440 810" preserveAspectRatio="xMidYMid slice">{web_screen()}</svg>
{grain(op=.08)}'''
    return art(inner)

def m_mobile():
    inner = f'''<rect width="1920" height="1080" fill="{CAY}"/><rect width="1920" height="1080" fill="{CAY}" filter="url(#clay)"/>
{phone(app_welcome(), 420, 150, 320, -4)}{phone(app_today(), 800, 110, 340, 0)}{phone(app_programme(), 1190, 160, 320, 4)}
{grain(op=.1)}'''
    return art(inner)

# ------------------------------------------------------------ M7 bronze plate detail
def m_plate():
    brush = ''.join(f'<line x1="0" x2="1500" y1="{y}" y2="{y}" stroke="#fff" stroke-opacity="{.03 + .03 * (y % 7 == 0)}"/>' for y in range(0, 700, 3))
    defs = '''<linearGradient id="plateG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b4430"/><stop offset=".35" stop-color="#a87a55"/><stop offset=".5" stop-color="#d9b48c"/><stop offset=".65" stop-color="#9a6c4a"/><stop offset="1" stop-color="#4b2b1e"/></linearGradient>
<radialGradient id="screw" cx=".35" cy=".35" r=".7"><stop offset="0" stop-color="#e3c39e"/><stop offset="1" stop-color="#5b3826"/></radialGradient>'''
    inner = f'''<rect width="1920" height="1080" fill="#e3dbcf"/><rect width="1920" height="1080" fill="#fff" filter="url(#stone)"/>
<g transform="translate(210,190)"><g filter="url(#lift)"><rect width="1500" height="700" fill="url(#plateG)"/></g>{brush}
<g filter="url(#debossDeep)">{nest(LA, "#3a2116", "#3a2116", 330, 140, 840)}</g>
<g opacity=".8">{nest((descriptor()[0], (0, -720, descriptor()[1], 720)), "#3a2116", "#3a2116", 450, 520, 600)}</g>
{''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="url(#screw)"/><line x1="{x-9}" x2="{x+9}" y1="{y}" y2="{y}" stroke="#3a2116" stroke-width="3"/>' for x, y in ((60, 60), (1440, 60), (60, 640), (1440, 640)))}</g>
<polygon points="0,0 1100,0 500,1080 0,1080" fill="#fff" opacity=".1"/>
{grain(op=.1)}'''
    return art(inner, defs)

# ------------------------------------------------------------ M8 atmospheric arcade
def m_arcade():
    VPx, VPy = 960, 560
    n = 6
    scales = [0.6 ** i for i in range(n)][::-1]
    shades = ['#e8dccb', '#d9c6ad', '#b99c80', '#8d6a55', '#5e3d31', '#3a1f19']
    out = [f'<rect width="1920" height="1080" fill="#f3e4cc"/>', f'<polygon points="-400,1080 2320,1080 {VPx},{VPy}" fill="#c9b9a3"/>']
    end = scales[0] * .6
    eb = VPy + (1080 - VPy) * end
    out.append(f'<circle cx="{VPx}" cy="{eb - 260*end:.1f}" r="{260*end:.1f}" fill="url(#hAsphere)"/>')
    for i, sc in enumerate(scales):
        yb = VPy + (1080 - VPy) * sc
        w = 1180 * sc; hh = 1500 * sc; r = w / 2
        x0 = VPx - w / 2; x1 = VPx + w / 2; yt = yb - hh
        d = f'M-400 -400H2320V{yb:.1f}H-400Z M{x0:.1f} {yb:.1f}V{yt+r:.1f}A{r:.1f} {r:.1f} 0 0 1 {x1:.1f} {yt+r:.1f}V{yb:.1f}Z'
        out.append(f'<path fill-rule="evenodd" d="{d}" fill="{shades[i]}"/><path fill-rule="evenodd" d="{d}" fill="#fff" filter="url(#stone)" opacity=".25"/>')
        if i + 1 < n:
            nyb = VPy + (1080 - VPy) * scales[i + 1]
            out.append(f'<polygon points="{x0 + w*.15:.1f},{yb:.1f} {x0 + w*.5:.1f},{yb:.1f} {x0 + w*.3:.1f},{nyb:.1f} {x0 - w*.25:.1f},{nyb:.1f}" fill="#fff4e0" opacity=".5"/>')
    inner = "".join(out) + f'''
{nest(LA, LIM, LIM, 890, 985, 140)}
{grain(op=.14)}'''
    return art(inner)

# ------------------------------------------------------------ M9 welcome kit
def m_kit():
    inner = f'''<rect width="1920" height="1080" fill="{TRA}"/><rect width="1920" height="1080" fill="#fff" filter="url(#stone)" opacity=".8"/>
<g transform="translate(200,150) rotate(-4)" filter="url(#lift)"><rect width="980" height="720" fill="{COC}"/><rect width="980" height="720" fill="{COC}" filter="url(#leather)" opacity=".5"/>
<rect x="30" y="30" width="920" height="660" fill="{LIM}"/><rect x="30" y="30" width="920" height="660" fill="{LIM}" filter="url(#paper)"/>
<g transform="translate(70,70)" filter="url(#liftS)"><rect width="330" height="460" fill="{COC}"/><rect width="330" height="460" fill="{COC}" filter="url(#leather)"/>
<g filter="url(#debossLeather)">{nest(SA, COC, COC, 125, 160, 80)}</g><rect x="300" width="10" height="460" fill="#1e0c09" opacity=".5"/></g>
<g transform="translate(460,80)"><circle cx="110" cy="110" r="110" fill="{GLA}" filter="url(#liftS)"/><circle cx="110" cy="110" r="96" fill="#b8cac5"/><circle cx="110" cy="110" r="70" fill="url(#cCap)"/><circle cx="96" cy="96" r="22" fill="#fff" opacity=".15"/></g>
<g transform="translate(700,90) rotate(6)" filter="url(#liftS)"><rect width="210" height="290" fill="{LIM}"/><rect width="210" height="290" fill="{LIM}" filter="url(#paper)"/>
{nest(SEAL2, COC, COC, 45, 40, 120)}<text x="105" y="230" text-anchor="middle" class="t-cormorant-i" font-size="22" fill="{COC}">Welcome.</text></g>
<g transform="translate(450,360)" filter="url(#liftS)"><rect width="460" height="280" rx="20" fill="{GLA}"/><rect width="460" height="280" rx="20" fill="#fff" filter="url(#paper)" opacity=".5"/>
<path d="M40 40Q230 80 420 40" fill="none" stroke="#5f726d" stroke-width="3"/><g filter="url(#deboss)">{nest(LA, GLA, GLA, 150, 140, 160)}</g></g></g>
<g transform="translate(1260,180) rotate(5)" filter="url(#lift)"><rect width="540" height="720" fill="{COC}"/><rect width="540" height="720" fill="{COC}" filter="url(#leather)" opacity=".6"/>
<g filter="url(#foilE)">{nest(LOCK, "url(#foil)", "url(#foil)", 110, 300, 320)}</g></g>
{grain(op=.1)}'''
    defs = f'<radialGradient id="cCap" cx=".35" cy=".35" r=".7"><stop offset="0" stop-color="#6a3a30"/><stop offset="1" stop-color="#22100c"/></radialGradient>'
    return art(inner, defs)

MOCKS = [
 ('Monumentálny vstup', m_entrance),
 ('Architektonické označenie', m_pylon),
 ('Tlačoviny a vizitky', m_stationery),
 ('Diagnostické prostredie', m_interior),
 ('Web na veľkej obrazovke', m_web),
 ('Mobilný zážitok', m_mobile),
 ('Logo na prémiovom materiáli', m_plate),
 ('Atmosférická brand fotografia', m_arcade),
 ('Welcome kit', m_kit),
]
