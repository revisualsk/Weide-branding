"""WEIDE identity v2 (willow-leaf W): presentation, brand guidelines, Instagram carousel and logo pack."""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import GLOBAL_DEFS, grain, ratio, CAY, GLA, COC, LIM, wax_blob  # noqa
from logos5 import MONO, WORD, DESC, LOCK, LOCK_SHORT, LOCKH, SEAL, MONO_W, MONO_H, _mono_d, MX0, MY0
from gl import glyph

OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'deck.css')).read() + open(os.path.join(HERE, 'p2.css')).read() + open(os.path.join(HERE, 'p3.css')).read()
FD = os.environ.get('FONTDIR', '')
FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500&display=swap">'
LOCAL = '\n'.join(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{FD}/{fn}.ttf')}}" for fn, fam, w, st in
                  [('CormorantGaramond-400', 'Cormorant Garamond', 400, 'normal'), ('CormorantGaramond-500', 'Cormorant Garamond', 500, 'normal'),
                   ('CormorantGaramond-400i', 'Cormorant Garamond', 400, 'italic'), ('DMSans-400', 'DM Sans', 400, 'normal'), ('DMSans-500', 'DM Sans', 500, 'normal')])

PH = {  # file, label
    'hero': ('WEIDE_01_hero.jpg', 'Kampaň'), 'entrance': ('WEIDE_02_entrance.jpg', 'Vstup'), 'reception': ('WEIDE_03_reception.jpg', 'Recepcia'),
    'lounge': ('WEIDE_04_lounge.jpg', 'Relaxačná zóna'), 'glass': ('WEIDE_05_glass.jpg', 'Sklenená priečka'), 'towel': ('WEIDE_06_towel.jpg', 'Ošetrovňa'),
    'velvet': ('WEIDE_07_velvet.jpg', 'Detail materiálu'), 'cards': ('WEIDE_08_cards.jpg', 'Vizitky'), 'stationery': ('WEIDE_09_stationery.jpg', 'Tlačoviny'),
    'seal': ('WEIDE_10_seal.jpg', 'Pečať'), 'jar': ('WEIDE_11_jar.jpg', 'Produkt'), 'tote': ('WEIDE_12_tote.jpg', 'Taška'),
    'tablet': ('WEIDE_13_tablet.jpg', 'Web'), 'phone': ('WEIDE_14_phone.jpg', 'Aplikácia'), 'moodboard': ('WEIDE_15_moodboard.jpg', 'Moodboard'),
}
def src(k): return f'mockups/{PH[k][0]}'

def strip(body): return body.split('</defs>', 1)[1] if body.startswith('<defs>') else body

def mk(lg, fill, w=None, h=None, cls='mark'):
    body, (x, y, bw, bh) = lg
    size = (f' width="{w}"' if w else '') + (f' height="{h}"' if h else '')
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {bw} {bh}"{size} fill="{fill}" color="{fill}" role="img" aria-label="WEIDE">{strip(body)}</svg>'

def place(lg, fill, x, y, w=None, h=None, op=1):
    body, (bx, by, bw, bh) = lg
    s = w / bw if w else h / bh
    return f'<g transform="translate({x:.1f},{y:.1f}) scale({s:.5f}) translate({-bx},{-by})" fill="{fill}" color="{fill}" opacity="{op}">{strip(body)}</g>', bw * s, bh * s

def fig(k, cls='ph', cap=True):
    f, t = PH[k]
    c = f'<figcaption>{t}</figcaption>' if cap else ''
    return f'<figure class="{cls}"><img src="mockups/{f}" alt="WEIDE · {t}" loading="lazy">{c}</figure>'

# ===================================================================== PRESENTATION
P = []
def add(c, bg=None, fg=None, lab=''): P.append((c, bg, fg, lab))

add(f'''<div class="cover2"><div class="cover-top"><span>ReVisual · Brand Identity</span><span>WEIDE · 2026</span></div>
<div class="c2-mid">{mk(LOCK, LIM, w="34%")}</div><div class="cover-bot"><span>Longevity &amp; Regenerative Health</span><span>Rakúsko</span></div></div>''', COC, LIM)

add(f'''<div class="pad grid-2"><div class="col"><p class="eyebrow">Príbeh značky</p><h2>Weide je vŕba.</h2>
<p class="lead">Strom, ktorý z jedného prútika vyrastie znova, z ktorého kôry vzišiel salicín a ktorý sa vo víchrici ohne, ale nezlomí. Monogram WEIDE nesie tento príbeh priamo v písmene.</p>
<div class="facts"><div><b>Regenerácia</b><p>List v strede W je nový výhonok.</p></div><div><b>Veda</b><p>Klasický kontrastný serif pôsobí presne a dôveryhodne.</p></div><div><b>Pokoj</b><p>Veľa vzduchu, tlmená paleta, prírodné materiály.</p></div><div><b>Podpis</b><p>Time, well kept.</p></div></div></div>
<div class="col pos" style="justify-content:center;align-items:center">{mk(MONO, COC, w="86%")}</div></div>''', LIM, COC, 'Príbeh')

# anatomy slide
mono_svg = place(MONO, COC, 0, 0, w=1000)[0]
mh = 1000 * MONO_H / MONO_W
def call(x1, y1, x2, y2, t, a='start'):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CAY}" stroke-width="2.5"/><circle cx="{x1}" cy="{y1}" r="9" fill="{CAY}"/>'
            f'<text x="{x2 + (14 if a == "start" else -14)}" y="{y2 + 9}" text-anchor="{a}" class="t-sans" font-size="26" letter-spacing="4" fill="{COC}">{t}</text>')
anat = (f'<svg class="anat" viewBox="-620 -80 2580 {mh + 160:.0f}" fill="{COC}">{mono_svg}'
        + call(560, 300, 1180, 120, 'LIST VŔBY · NOVÝ VÝHONOK')
        + call(520, 420, 1180, 420, 'RYHA LISTU · PRESNOSŤ')
        + call(180, 220, -60, 120, 'KONTRASTNÝ SERIF', 'end')
        + call(760, 560, 1180, 640, 'ZÁKLADNÉ W · STABILITA') + '</svg>')
add(f'''<div class="pad cons"><div class="cons-l"><p class="eyebrow">Monogram</p><h2>W, ktoré rastie.</h2>
<p class="body">Klasické W s kontrastom ťahov. Jeho stredný ťah sa mení na vŕbový list s ryhou uprostred, ktorý vyrastá zo spodku písmena a otvára sa doprava hore.</p>
<p class="body">Monogram funguje samostatne ako pečať, výšivka, razba či ikona aplikácie. S nápisom WEIDE tvorí primárny lockup.</p></div>
<div class="cons-r">{anat}</div></div>''', LIM, COC, 'Monogram')

add(f'''<div class="pad sys"><div class="sys-head"><p class="eyebrow">Logo systém</p><h2>Jeden znak, päť podôb.</h2></div>
<div class="sys-grid">
<div class="sg sg-big" style="background:{LIM}">{mk(LOCK, COC, w="58%")}<p>Primárny lockup</p></div>
<div class="sg" style="background:{COC}">{mk(LOCK_SHORT, LIM, w="44%")}<p style="color:{GLA}">Lockup bez podnadpisu</p></div>
<div class="sg" style="background:{GLA}">{mk(MONO, COC, w="36%")}<p>Monogram</p></div>
<div class="sg" style="background:{CAY}">{mk(SEAL, LIM, h="66%")}<p style="color:{LIM}">Pečať</p></div>
<div class="sg" style="background:#fff">{mk(LOCKH, COC, w="80%")}<p>Horizontálna verzia</p></div>
</div></div>''', LIM, COC, 'Logo systém')

def band(img, name, hexv, rgb, cmyk, txt, bg):
    return (f'<div class="band"><div class="bmat"><img src="{img}" alt="" loading="lazy"></div>'
            f'<div class="bsw" style="background:{bg};color:{txt}"><p class="bname">{name}</p><p class="bspec">HEX {hexv}<br/>RGB {rgb}<br/>CMYK {cmyk}</p></div></div>')
add(f'''<div class="pad pal2"><div class="pal2-l"><p class="eyebrow">Farby</p><h2>Štyri tóny, štyri materiály.</h2>
<div class="roles"><div><b style="color:{CAY}">Cayenne Dust</b><p>Energia a vitalita. Hlina, terakota, vosk.</p></div>
<div><b>Weathered Glass</b><p>Pokoj a regenerácia. Sklo, voda, ranné svetlo.</p></div>
<div><b>Bitter Cocoa</b><p>Hĺbka a prémiový charakter. Zamat, koža, písmo.</p></div>
<div><b>Sand Limestone</b><p>Vzduch a svetlo. Kameň, ľan, papier.</p></div></div></div>
<div class="bands">
{band(src('lounge'), 'Cayenne Dust', '#9D3F0D', '157 63 13', '24 74 100 13', LIM, CAY)}
{band(src('glass'), 'Weathered Glass', '#9AB0AA', '154 176 170', '42 18 29 5', COC, GLA)}
{band(src('velvet'), 'Bitter Cocoa', '#391B17', '57 27 23', '46 78 72 70', LIM, COC)}
{band(src('seal'), 'Sand Limestone', '#D8C9B7', '216 201 183', '15 18 26 0', COC, LIM)}
</div></div>''', LIM, COC, 'Farby')

def tspec(font, s):
    return f'<span class="t3 {font}">{s}</span>'
add(f'''<div class="pad typo2"><div><p class="eyebrow">Typografia</p><h2>Klasika a presnosť.</h2></div>
<div class="t2-rows">
<div class="t2"><div class="t2-meta"><b>Cormorant Garamond</b><span>Wordmark, titulky, citáty · 400 a 500 · kurzíva na podpis</span></div><div class="t2-spec tf-cormorant" style="font-size:4.6em;line-height:1">Time, well kept.</div></div>
<div class="t2"><div class="t2-meta"><b>Cormorant Garamond · verzálky</b><span>Nápisy a signáž · prestrkanie +0.15 em</span></div><div class="t2-spec tf-cormorant" style="font-size:3em;letter-spacing:.15em">WEIDE · REGENERÁCIA</div></div>
<div class="t2"><div class="t2-meta"><b>DM Sans</b><span>Text, UI, popisky · 400 / 500 · 16 / 1.6</span></div><div class="t2-spec tf-dmsans" style="font-size:1.3em;line-height:1.6;max-width:36em">Presná diagnostika, regeneratívne terapie a osobný plán na ďalšie desaťročia. V pokoji rakúskeho domu.</div></div>
<div class="t2"><div class="t2-meta"><b>Podnadpis</b><span>DM Sans 400 · verzálky · prestrkanie +0.26 em</span></div><div class="t2-spec tf-dmsans" style="font-size:1em;letter-spacing:.26em">LONGEVITY &amp; REGENERATIVE HEALTH</div></div>
</div></div>''', LIM, COC, 'Typografia')

add(f'<div class="full"><figure class="ph ph-full"><img src="mockups/{PH["moodboard"][0]}" alt="WEIDE moodboard" style="object-fit:contain"><figcaption>Moodboard identity</figcaption></figure></div>', COC, LIM)
add(f'<div class="full"><figure class="ph ph-full"><img src="mockups/WEIDE_cover_composite.jpg" alt="WEIDE kampaň" style="object-position:center 40%"><figcaption>Kampaň</figcaption></figure></div>', COC, LIM)
for grp in (('entrance', 'reception', 'lounge'), ('glass', 'towel', 'velvet'), ('cards', 'stationery', 'seal'), ('jar', 'tote', 'phone'), ('tablet',)):
    add(f'<div class="phrow n{len(grp)}">{"".join(fig(k) for k in grp)}</div>', COC, LIM)

ig_thumbs = ''.join(f'<div class="igt"><img src="instagram/WEIDE_carousel_{i+1:02d}.jpg" alt="Carousel {i+1}" loading="lazy"></div>' for i in range(10))
add(f'<div class="pad igslide"><div class="ig-head"><p class="eyebrow">Instagram</p><h2>Carousel 10 × 1080 × 1350.</h2><p class="body">Kampaňová obálka, príbeh mena, monogram, vstup, paleta, vizitky, relaxačná zóna, produkt, web a záverečný lockup.</p></div><div class="ig-grid">{ig_thumbs}</div></div>', LIM, COC, 'Instagram')

add(f'''<div class="cover2"><div class="cover-top"><span>Brand identity by ReVisual</span><span>2026</span></div>
<div class="c2-mid">{mk(SEAL, LIM, w="22%")}</div><div class="cover-bot"><span>Time, well kept.</span><span>revisual.sk</span></div></div>''', COC, LIM)

# ===================================================================== MANUAL
M = []
def madd(c, bg=LIM, fg=COC, lab=''): M.append((c, bg, fg, lab))

madd(f'''<div class="cover2"><div class="cover-top"><span>Brand Guidelines</span><span>Verzia 2.0 · 2026</span></div>
<div class="c2-mid">{mk(LOCK, LIM, w="32%")}</div><div class="cover-bot"><span>Longevity &amp; Regenerative Health</span><span>ReVisual</span></div></div>''', COC, LIM)
toc = ['Príbeh značky', 'Logo', 'Monogram', 'Ochranná zóna', 'Varianty', 'Minimálne veľkosti', 'Nesprávne použitie', 'Farby', 'Typografia', 'Grafické prvky', 'Fotografia', 'Tón komunikácie', 'Aplikácie']
madd('<div class="pad toc"><div><p class="eyebrow">Obsah</p><h2>Ako používať WEIDE.</h2></div><ol class="toc-list">' + ''.join(f'<li><span>{i+3:02d}</span>{t}</li>' for i, t in enumerate(toc)) + '</ol></div>', lab='Obsah')
madd(P[1][0], lab='Príbeh značky')
madd(f'''<div class="logo-sys"><div class="ls-light" style="background:{LIM}"><span class="cap">Primárne · svetlé</span>{mk(LOCK, COC, w="52%")}</div>
<div class="ls-dark" style="background:{COC}"><span class="cap" style="color:{GLA}">Primárne · tmavé</span>{mk(LOCK, LIM, w="52%")}</div>
<div class="ls-info" style="background:{LIM};color:{COC}"><div class="ls-notes">
<div><b>Monogram</b><p>W s vŕbovým listom je nositeľ príbehu a stojí nad nápisom.</p></div>
<div><b>Wordmark</b><p>WEIDE v Cormorant Garamond 500, prestrkanie +0.15 em. Medzery v logu sa nemenia.</p></div>
<div><b>Podnadpis</b><p>LONGEVITY &amp; REGENERATIVE HEALTH v DM Sans, rovnako široký ako celý lockup.</p></div></div>
<div class="ls-notes"><div><b>Kedy lockup</b><p>Prvé stretnutie so značkou: vstup, web, tlačoviny, prezentácie.</p></div><div><b>Kedy monogram</b><p>Keď je značka zrejmá z kontextu: textil, pečať, obaly, ikona aplikácie, sociálne siete.</p></div></div></div></div>''', lab='Logo')
madd(P[2][0], lab='Monogram')

body, (bx, by, bw, bh) = LOCK
x = 230
guide = (f'<svg class="constr" viewBox="{-x-80} {-x-80} {bw+2*x+160} {bh+2*x+160}" fill="{COC}">'
         f'<rect x="{-x}" y="{-x}" width="{bw+2*x}" height="{bh+2*x}" fill="none" stroke="{CAY}" stroke-width="5" stroke-dasharray="24 16"/>'
         f'<rect x="0" y="0" width="{bw}" height="{bh}" fill="none" stroke="{GLA}" stroke-width="3"/>' + strip(body)
         + f'<rect x="{-x}" y="0" width="{x}" height="{x}" fill="{CAY}" opacity=".18"/><text x="{-x/2}" y="{x/2+25}" text-anchor="middle" font-size="80" fill="{CAY}" class="t-sans">x</text>'
         + f'<rect x="{bw}" y="{bh-x}" width="{x}" height="{x}" fill="{CAY}" opacity=".18"/><text x="{bw+x/2}" y="{bh-x/2+25}" text-anchor="middle" font-size="80" fill="{CAY}" class="t-sans">x</text></svg>')
madd(f'''<div class="pad cons"><div class="cons-l"><p class="eyebrow">Ochranná zóna</p><h2>Priestor okolo znaku.</h2>
<p class="body">Ochranná zóna x sa rovná výške písmen WEIDE. Do zóny nesmie zasahovať text, okraj formátu ani iný grafický prvok.</p>
<p class="body">Pri monograme platí rovnaké pravidlo: x je štvrtina jeho výšky.</p></div><div class="cons-r">{guide}</div></div>''', lab='Ochranná zóna')

madd(f'''<div class="pad vars"><div><p class="eyebrow">Varianty</p><h2>Správna podoba pre každú situáciu.</h2></div><div class="var-grid">
<div class="vg" style="background:{LIM}">{mk(LOCK, COC, w="40%")}<p>Lockup</p></div>
<div class="vg" style="background:{COC}">{mk(LOCK_SHORT, LIM, w="36%")}<p style="color:{GLA}">Bez podnadpisu</p></div>
<div class="vg" style="background:{GLA}">{mk(MONO, COC, w="34%")}<p>Monogram</p></div>
<div class="vg" style="background:{CAY}">{mk(SEAL, LIM, h="66%")}<p style="color:{LIM}">Pečať</p></div>
<div class="vg" style="background:#fff">{mk(LOCKH, "#000", w="78%")}<p>Horizontálna · čierna</p></div>
<div class="vg" style="background:#000">{mk(LOCK, "#fff", w="40%")}<p style="color:#fff">Biela</p></div></div></div>''', lab='Varianty')

madd(f'''<div class="pad sizes2"><div><p class="eyebrow">Minimálne veľkosti</p><h2>Vlasové ťahy potrebujú priestor.</h2>
<p class="body">List v monograme má veľmi tenké ťahy. Pod uvedenými veľkosťami sa zlieva, preto použite menší variant.</p></div>
<div class="size-table">
<div><span class="cap2">Lockup</span><div class="srow">{mk(LOCK, COC, h="96")}{mk(LOCK, COC, h="64")}</div><p>od 120 px šírky · od 30 mm</p></div>
<div><span class="cap2">Lockup bez podnadpisu</span><div class="srow">{mk(LOCK_SHORT, COC, h="64")}{mk(LOCK_SHORT, COC, h="44")}</div><p>od 80 px šírky · od 20 mm</p></div>
<div><span class="cap2">Monogram</span><div class="srow">{mk(MONO, COC, h="48")}{mk(MONO, COC, h="32")}</div><p>od 32 px výšky · od 8 mm · favicon 32 px</p></div>
<div><span class="cap2">Pečať</span><div class="srow">{mk(SEAL, COC, h="96")}{mk(SEAL, COC, h="64")}</div><p>od 64 px · od 20 mm</p></div>
</div></div>''', lab='Minimálne veľkosti')

def bad(inner, bg, t):
    return f'<div class="bad"><div class="bad-art" style="background:{bg}">{inner}<svg class="x" viewBox="0 0 100 100" preserveAspectRatio="none"><line x1="0" y1="100" x2="100" y2="0" stroke="{CAY}" stroke-width=".8"/></svg></div><p>{t}</p></div>'
busy = f'<svg class="busy" viewBox="0 0 600 340" preserveAspectRatio="xMidYMid slice"><image href="{src("velvet")}" width="600" height="340" preserveAspectRatio="xMidYMid slice"/></svg>'
madd(f'''<div class="pad misuse"><div><p class="eyebrow">Nesprávne použitie</p><h2>Čo s logom nerobiť.</h2></div><div class="bad-grid">
{bad(mk(LOCK, COC, w="34%").replace('<svg class="mark"', '<svg class="mark" style="transform:scaleX(1.5)"', 1), LIM, 'Nedeformovať')}
{bad(mk(LOCK, GLA, w="34%"), LIM, 'Nepoužívať farby s nízkym kontrastom')}
{bad(mk(LOCK, COC, w="34%").replace('<svg class="mark"', '<svg class="mark" style="filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))"', 1), LIM, 'Nepridávať tiene ani efekty')}
{bad('<div style="display:flex;gap:2em;align-items:center">' + mk(MONO, COC, h="90") + mk(WORD, COC, h="40") + '</div>', LIM, 'Nemeniť skladbu lockupu')}
{bad(mk(LOCK, COC, w="30%").replace('<svg class="mark"', '<svg class="mark" style="transform:rotate(-14deg)"', 1), LIM, 'Neotáčať')}
{bad(busy + mk(LOCK, COC, w="34%").replace('<svg class="mark"', '<svg class="mark over"', 1), COC, 'Neumiestňovať tmavé logo na tmavú fotografiu')}
</div></div>''', lab='Nesprávne použitie')

combos = [(LIM, COC, 'Sand Limestone na Cocoa', '9.6 : 1'), (COC, LIM, 'Cocoa na Sand Limestone', '9.6 : 1'), (COC, GLA, 'Cocoa na Glass', '6.8 : 1'),
          (LIM, CAY, 'Sand Limestone na Cayenne', '4.1 : 1 · veľký text'), (GLA, COC, 'Glass na Cocoa', '6.8 : 1'), (CAY, LIM, 'Cayenne na Sand Limestone', '4.1 : 1 · veľký text')]
madd(f'''<div class="pad colors"><div class="col-l"><p class="eyebrow">Farby</p><h2>Paleta a pomer.</h2>
{ratio([('Bitter Cocoa', COC, 48, LIM), ('Sand Limestone', LIM, 26, COC), ('Weathered Glass', GLA, 16, COC), ('Cayenne', CAY, 10, LIM)])}
<div class="specs">{''.join(f'<div><i style="background:{h}"></i><b>{n}</b><span>HEX {h} · RGB {rgb} · CMYK {cmyk}</span></div>' for n, h, rgb, cmyk in (('Cayenne Dust', CAY, '157 63 13', '24 74 100 13'), ('Weathered Glass', GLA, '154 176 170', '42 18 29 5'), ('Bitter Cocoa', COC, '57 27 23', '46 78 72 70'), ('Sand Limestone', LIM, '216 201 183', '15 18 26 0')))}</div>
<p class="body">Cocoa nesie značku, Sand Limestone dáva vzduch, Glass upokojuje a Cayenne je akcent: pečať, tlačidlo, jeden prvok na formát.</p></div>
<div class="combo-grid">{''.join(f'<div class="combo" style="background:{b};color:{f}"><span class="cmb-big">Aa</span><span>{n}</span><b>{c}</b></div>' for f, b, n, c in combos)}</div></div>''', lab='Farby')
madd(P[5][0], lab='Typografia')

# graphic elements: leaf-line pattern, monogram crop, seal, oval photo window
lines = ''.join(f'<path d="M{-60 + i*55} 320 C {60 + i*55} 200, {120 + i*50} 120, {260 + i*48} -20" fill="none" stroke="{LIM}" stroke-opacity=".7" stroke-width="1.6"/>' for i in range(10))
pattern = f'<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice"><rect width="400" height="300" fill="{GLA}"/>{lines}</svg>'
crop = f'<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice"><rect width="400" height="300" fill="{COC}"/>{place(MONO, LIM, -120, -60, w=760, op=.95)[0]}</svg>'
seal_el = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{LIM}"/>{place(SEAL, COC, 120, 70, w=160)[0]}</svg>'
oval = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{COC}"/><clipPath id="ovx"><ellipse cx="200" cy="150" rx="78" ry="118"/></clipPath><image href="{src("hero")}" x="80" y="20" width="240" height="300" preserveAspectRatio="xMidYMid slice" clip-path="url(#ovx)"/><ellipse cx="200" cy="150" rx="78" ry="118" fill="none" stroke="{GLA}"/></svg>'
frame = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{LIM}"/>' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="{COC}" opacity=".5"/>' for x, y, w in ((16, 16, 120), (300, 16, 84), (16, 280, 90), (170, 280, 60), (310, 280, 74))) + f'{place(LOCK_SHORT, COC, 150, 90, w=100)[0]}</svg>'
def el(svg, t, d): return f'<div class="el"><div class="el-art">{svg}</div><b>{t}</b><p>{d}</p></div>'
madd(f'''<div class="pad els"><div><p class="eyebrow">Grafické prvky</p><h2>Jazyk okolo loga.</h2></div><div class="el-grid">
{el(pattern, 'Línie listu', 'Tenké krivky odvodené z listu v monograme. Pozadie pre obaly a sekcie webu.')}
{el(crop, 'Orezaný monogram', 'Veľký výrez monogramu cez okraj formátu. Iba jeden na plochu.')}
{el(oval, 'Oválne okno', 'Výrez pre fotografiu, pomer 2 : 3, tenký obrys v Glass.')}
{el(frame, 'Editoriálny rám', 'Drobné popisky v rohoch formátu: značka, rok, miesto, číslovanie.')}
{el(seal_el, 'Pečať', 'Vosk v Cayenne alebo slepotlač. Pre osobné a slávnostné momenty.')}
</div></div>''', lab='Grafické prvky')
madd(f'''<div class="pad photo"><div class="ph-l"><p class="eyebrow">Fotografia</p><h2>Teplé svetlo, pokojný priestor.</h2>
<div class="facts"><div><b>Svetlo</b><p>Nízke slnko, tiene listov, jeden teplý zdroj.</p></div><div><b>Človek</b><p>Telo a pokoj, nie výkon. Žiadne pózovanie.</p></div>
<div><b>Materiál</b><p>Travertín, zamat, ľan, sklo, papier s vláknom.</p></div><div><b>Farebnosť</b><p>Cocoa a Cayenne v tieňoch, Sand v svetlách, Glass ako chladný kontrapunkt.</p></div></div></div>
<div class="ph-r"><img src="{src('hero')}" alt="WEIDE fotografia" style="object-position:center 35%"></div></div>''', lab='Fotografia')
madd('''<div class="pad grid-2"><div class="col"><p class="eyebrow">Tón komunikácie</p><h2>Hovoríme menej, s istotou.</h2>
<p class="lead">Pokojne, presne a kultivovane. Bez superlatívov a bez sľubov, ktoré nevieme overiť. Vedu vysvetľujeme ľudsky.</p></div>
<div class="col tone"><div class="tn"><span>Áno</span><p>Precízna diagnostika a osobný plán na ďalšie desaťročia.</p></div><div class="tn no"><span>Nie</span><p>Revolučná terapia, ktorá vás omladí o 20 rokov!</p></div>
<div class="tn"><span>Áno</span><p>Time, well kept.</p></div><div class="tn no"><span>Nie</span><p>Najlepšie longevity centrum v Európe.</p></div></div></div>''', lab='Tón komunikácie')
thumbs = ''.join(f'<div class="ap"><div class="ap-art"><img src="{src(k)}" alt="{PH[k][1]}" loading="lazy"></div><p>{PH[k][1]}</p></div>' for k in ('entrance', 'reception', 'lounge', 'towel', 'cards', 'stationery', 'jar', 'tablet'))
madd(f'<div class="pad apps"><div><p class="eyebrow">Aplikácie</p><h2>WEIDE v priestore, papieri a obrazovke.</h2></div><div class="ap-grid">{thumbs}</div></div>', lab='Aplikácie')
madd(f'''<div class="cover2"><div class="cover-top"><span>Brand Guidelines</span><span>ReVisual</span></div>
<div class="c2-mid">{mk(SEAL, LIM, w="22%")}</div><div class="cover-bot"><span>Time, well kept.</span><span>© 2026 ReVisual</span></div></div>''', COC, LIM)

# ===================================================================== CAROUSEL 1080x1350
def num(n, fg): return f'<text x="1024" y="1300" text-anchor="end" class="t-sans" font-size="15" letter-spacing="3" fill="{fg}" opacity=".8">{n:02d} / 10</text>'
def ig(inner): return f'<svg class="igs" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
def photo(k, n, fg=LIM, pos='xMidYMid'):
    return ig(f'<image href="{src(k)}" width="1080" height="1350" preserveAspectRatio="{pos} slice"/>{num(n, fg)}')

def ig_story():
    m, w, h = place(MONO, GLA, 560, 860, w=820, op=.4)
    return ig(f'''<rect width="1080" height="1350" fill="{LIM}"/>{m}
<text x="80" y="300" class="t-sans" font-size="17" letter-spacing="4" fill="{CAY}">THE NAME</text>
<text x="76" y="420" class="t-cormorant" font-size="130" fill="{COC}">Weide</text>
<text x="80" y="490" class="t-cormorant-i" font-size="48" fill="{COC}">German for willow.</text>
{''.join(f'<text x="80" y="{y}" class="t-sans" font-size="16" letter-spacing="3.5" fill="{CAY}">{k}</text><text x="80" y="{y+44}" class="t-cormorant" font-size="36" fill="{COC}">{v}</text>' for y, k, v in ((680, 'REGENERATION', 'A single cutting takes root again.'), (820, 'SCIENCE', 'Willow bark gave medicine salicin.'), (960, 'RESILIENCE', 'It bends in the storm, never breaks.')))}
{num(2, COC)}''')

def ig_mono():
    m, w, h = place(MONO, LIM, 90, 330, w=900)
    def c(x1, y1, x2, y2, t, a='start'):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GLA}" stroke-width="1.4"/><circle cx="{x1}" cy="{y1}" r="5" fill="{GLA}"/>'
                f'<text x="{x2 + (12 if a == "start" else -12)}" y="{y2 + 6}" text-anchor="{a}" class="t-sans" font-size="17" letter-spacing="3.5" fill="{LIM}">{t}</text>')
    return ig(f'''<rect width="1080" height="1350" fill="{COC}"/>{m}
{c(655, 560, 600, 230, 'WILLOW LEAF · NEW GROWTH')}{c(250, 560, 110, 1040, 'CLASSIC SERIF W')}{c(410, 900, 640, 1040, 'ROOTED BASE')}
<text x="540" y="1180" text-anchor="middle" class="t-cormorant-i" font-size="44" fill="{LIM}">A W that grows.</text>{num(3, LIM)}''')

def ig_palette():
    rows = [(src('lounge'), 'Cayenne Dust', '#9D3F0D', CAY, LIM), (src('glass'), 'Weathered Glass', '#9AB0AA', GLA, COC), (src('velvet'), 'Bitter Cocoa', '#391B17', COC, LIM), (src('seal'), 'Sand Limestone', '#D8C9B7', LIM, COC)]
    out = ''
    for i, (im, n, hx, c, t) in enumerate(rows):
        y = 150 + i * 270
        out += (f'<clipPath id="pc{i}"><rect x="60" y="{y}" width="480" height="250"/></clipPath><image href="{im}" x="60" y="{y-100}" width="480" height="450" preserveAspectRatio="xMidYMid slice" clip-path="url(#pc{i})"/>'
                f'<rect x="540" y="{y}" width="480" height="250" fill="{c}"/><text x="1000" y="{y+56}" text-anchor="end" class="t-cormorant" font-size="40" fill="{t}">{n}</text>'
                f'<text x="1000" y="{y+222}" text-anchor="end" class="t-sans" font-size="15" letter-spacing="3" fill="{t}" opacity=".85">HEX {hx}</text>')
    return ig(f'<rect width="1080" height="1350" fill="{LIM}"/>{out}<text x="60" y="100" class="t-sans" font-size="16" letter-spacing="4" fill="{COC}">COLOUR PALETTE</text>{num(5, COC)}')

def ig_cover():
    return ig(f'<image href="mockups/WEIDE_cover_composite.jpg" width="1080" height="1350" preserveAspectRatio="xMidYMid slice"/>{num(1, LIM)}')

def ig_end():
    l, w, h = place(LOCK, LIM, 540 - 260, 380, w=520)
    return ig(f'''<rect width="1080" height="1350" fill="{COC}"/>{l}
<text x="540" y="900" text-anchor="middle" class="t-cormorant-i" font-size="52" fill="{LIM}">Time, well kept.</text>
<text x="540" y="1180" text-anchor="middle" class="t-sans" font-size="16" letter-spacing="4" fill="{GLA}">BRAND IDENTITY BY REVISUAL</text>{num(10, LIM)}''')

IG = [ig_cover, ig_story, ig_mono, lambda: photo('entrance', 4), ig_palette, lambda: photo('cards', 6), lambda: photo('lounge', 7), lambda: photo('jar', 8), lambda: photo('tablet', 9), ig_end]

# ===================================================================== WRITE
def page(title, slides, folio, local=False):
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + (f'<style>{LOCAL}</style>' if local else FONT_LINK) + f'<style>{CSS}</style>'
    body = GLOBAL_DEFS + '<main class="deck">' + ''.join(
        f'<section class="sw"><div class="slide" style="{f"background:{bg};color:{fg};" if bg else ""}">{c}'
        + (f'<div class="folio"><span>{folio}</span><span>{lab}</span><span>{i+1:02d}</span></div>' if lab else '') + '</div></section>'
        for i, (c, bg, fg, lab) in enumerate(slides)) + '</main>'
    return ('<!doctype html><meta charset="utf-8">' if local else '') + head + body

os.makedirs(OUT, exist_ok=True)
for name, title, slides, folio in (('index', 'WEIDE Brand Identity', P, 'WEIDE · Brand Identity'), ('manual', 'WEIDE Brand Guidelines', M, 'WEIDE · Brand Guidelines')):
    open(f'{OUT}/{name}.html', 'w').write(page(title, slides, folio))
    open(f'{OUT}/{name}.render.html', 'w').write(page(title, slides, folio, True))
open(f'{OUT}/ig.render.html', 'w').write('<!doctype html><meta charset="utf-8"><style>' + LOCAL + CSS + 'body{margin:0}.g{width:1080px;height:1350px}.g>svg{display:block;width:1080px;height:1350px}</style>' + GLOBAL_DEFS + ''.join(f'<div class="g">{f()}</div>' for f in IG))

# cover composite helper page (hero photo + exact cream lockup on the wall)
l, w, h = place(LOCK, '#EFE4D6', 135, 760, w=700)
open(f'{OUT}/cover.render.html', 'w').write(f'<!doctype html><meta charset="utf-8"><body style="margin:0"><div class="g" style="width:1856px;height:2304px"><svg width="1856" height="2304" viewBox="0 0 1856 2304"><image href="mockups/{PH["hero"][0]}" width="1856" height="2304"/>{l}</svg></div>')

# logo pack
LD = f'{OUT}/logos'; os.makedirs(LD, exist_ok=True)
items = {'lockup': LOCK, 'lockup-short': LOCK_SHORT, 'lockup-horizontal': LOCKH, 'monogram': MONO, 'wordmark': WORD, 'seal': SEAL}
cols = {'cocoa': COC, 'sand-limestone': LIM, 'cayenne': CAY, 'black': '#000000', 'white': '#FFFFFF'}
html = '<!doctype html><body style="margin:0">'
for n, lg in items.items():
    b, (x, y, bw, bh) = lg; pad = max(bw, bh) * .08
    for cn, c in cols.items():
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-pad:.1f} {y-pad:.1f} {bw+2*pad:.1f} {bh+2*pad:.1f}" fill="{c}" color="{c}">{strip(b)}</svg>'
        open(f'{LD}/WEIDE_{n}_{cn}.svg', 'w').write(svg)
        W = 2400 if bw >= bh else int(2400 * bw / bh); H = int(W * (bh + 2 * pad) / (bw + 2 * pad))
        html += f'<div class="l" data-n="WEIDE_{n}_{cn}" style="width:{W}px;height:{H}px">' + svg.replace('<svg ', f'<svg width="{W}" height="{H}" ', 1) + '</div>'
open(f'{OUT}/logos.render.html', 'w').write(html)
print(len(P), len(M), len(IG))
