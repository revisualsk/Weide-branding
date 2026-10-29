import os, sys
from ig2 import *

OUT = sys.argv[1]
CSS = open(os.path.join(os.path.dirname(__file__), 'deck.css')).read() + open(os.path.join(os.path.dirname(__file__), 'p2.css')).read()
FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500&display=swap">'
LOCAL = '\n'.join(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{os.environ['FONTDIR']}/{fn}.ttf')}}" for fn, fam, w, st in
                  [('CormorantGaramond-400', 'Cormorant Garamond', 400, 'normal'), ('CormorantGaramond-500', 'Cormorant Garamond', 500, 'normal'), ('CormorantGaramond-400i', 'Cormorant Garamond', 400, 'italic'), ('DMSans-400', 'DM Sans', 400, 'normal'), ('DMSans-500', 'DM Sans', 500, 'normal')])

def page(title, slides, local=False):
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + (f'<style>{LOCAL}</style>' if local else FONT_LINK) + f'<style>{CSS}</style>'
    body = GLOBAL_DEFS + '<main class="deck">' + ''.join(
        f'<section class="sw"><div class="slide" style="{f"background:{bg};color:{fg};" if bg else ""}">{c}'
        + (f'<div class="folio"><span>{folio}</span><span>{lab}</span><span>{i+1:02d}</span></div>' if lab else '') + '</div></section>'
        for i, (c, bg, fg, lab) in enumerate(slides)) + '</main>'
    return ('<!doctype html><meta charset="utf-8">' if local else '') + head + body

def full(svg, cap=None, fg=LIM):
    c = f'<span class="hero-cap" style="color:{fg}">{cap}</span>' if cap else ''
    return f'<div class="full">{svg}{c}</div>'

def outline_svg(font, s):
    body, w = text_path(font, s)
    return f'<svg class="tsvg" viewBox="0 -760 {w:.0f} 900" preserveAspectRatio="xMinYMid meet" fill="{COC}">{body}</svg>'

def mk(lg, fill, acc=None, w='70%', h=None):
    return mark(lg, fill, acc or fill, w=w if not h else None, h=h)

# ====================================================================== PRESENTATION
P = []
folio = 'WEIDE · Phase 2'
P.append((f'''<div class="cover2">
<div class="cover-top"><span>ReVisual — Brand Identity</span><span>Fáza 2 · Identita, aplikácie, carousel</span></div>
<div class="c2-mid">{mk(LOCK, LIM, w="62%")}</div>
<div class="cover-bot"><span>Smer A · Editorial Luxury</span><span>Graze</span><span>Október 2026</span></div></div>''', COC, LIM, ''))

P.append((f'''<div class="pad sys">
<div class="sys-head"><p class="eyebrow">Logo systém</p><h2>Jeden znak, štyri podoby.</h2></div>
<div class="sys-grid">
<div class="sg sg-big" style="background:{LIM}">{mk(LOCK, COC, w="70%")}<p>Primárny lockup · wordmark a podnadpis</p></div>
<div class="sg" style="background:{COC}">{mk(LA, LIM, w="70%")}<p style="color:{GLA}">Wordmark</p></div>
<div class="sg" style="background:{GLA}">{mk(SA, COC, h="46%")}<p>Monogram W</p></div>
<div class="sg" style="background:{CAY}">{mk(SEAL2, LIM, h="62%")}<p style="color:{LIM}">Pečať</p></div>
<div class="sg" style="background:{LIM}"><div class="micro-row">{mk(MICRO, COC, h="22")}{mk(MICRO, COC, h="16")}</div><p>Mikro verzia pod 40 px</p></div>
</div></div>''', LIM, COC, 'Logo systém'))

PH = [('01','web-tablet','Web · tablet'),('02','web-desktop','Web · desktop'),('03','cover-shadow','Cover'),('04','details-grid','Detaily'),('05','palette-vertical','Paleta'),('06','palette-horizontal','Paleta · materiály'),('07','treatment-towel','Ošetrovňa · monogram'),('08','fluted-glass','Sklenená priečka'),('09','bottle','Produkt'),('10','lounge','Relaxačná zóna'),('11','treatment-room','Diagnostická miestnosť'),('12','business-cards','Vizitky'),('13','hero-body','Hero kampaň'),('14','collage','Prehľad identity'),('15','entrance','Vstup'),('16','stationery','Tlačoviny')]
def img(n): 
    nn, slug, t = PH[n-1]
    return f'<figure class="ph"><img src="mockups/WEIDE_{nn}_{slug}.jpg" alt="WEIDE {t}" loading="lazy"><figcaption>{nn} · {t}</figcaption></figure>'
P.append((f'<div class="full">{img(14).replace("class=\"ph\"", "class=\"ph ph-full\"")}</div>', COC, LIM, ''))
for grp in ((13, 15, 3), (11, 10, 7), (8, 9, 4), (12, 16, 5), (1, 2, 6)):
    P.append((f'<div class="phrow">{"".join(img(n) for n in grp)}</div>', COC, LIM, ''))

ig_thumbs = ''.join(f'<div class="igt"><img src="instagram/WEIDE_carousel_{i+1:02d}.jpg" alt="Carousel {i+1}" loading="lazy"></div>' for i in range(10))
P.append((f'<div class="pad igslide"><div class="ig-head"><p class="eyebrow">Instagram</p><h2>Carousel 10 × 1080 × 1350.</h2><p class="body">Cover s kampaňovou fotografiou, príbeh mena, detail loga, vstup, paleta, vizitky, sklenená priečka, diagnostická miestnosť, web a tlačoviny.</p></div><div class="ig-grid">{ig_thumbs}</div></div>', LIM, COC, 'Instagram carousel'))

PROMPTS = [
 ('Monumentálny vstup', 'Architectural photograph at dusk, monumental travertine facade of a contemporary longevity centre in the Austrian Alps, a single tall rectangular portal glowing warm amber from inside, bronze lettering above the portal left blank, reflecting pool in the foreground, sage-grey sky (#9AB0AA), perfect symmetry, tilt-shift lens, quiet luxury --ar 16:9 --style raw --v 7'),
 ('Diagnostické prostredie', 'Interior of a premium diagnostic suite, travertine back wall left blank for bronze lettering, fluted sage glass partition on the left, dark cocoa wood panels on the right (#391B17), a low limestone treatment bed, soft daylight from a ceiling slot, one-point perspective, architectural digest --ar 16:9 --style raw --v 7'),
 ('Atmosféra', 'Enfilade of travertine arches receding into warm light, raking sunlight on the floor, a single polished stone sphere at the end of the corridor, deep cocoa shadows, editorial, calm, film grain --ar 4:5 --style raw --v 7'),
 ('Ľudia', 'Sculptural portrait of a woman in her fifties in a cocoa-brown linen robe, turned away from camera, single warm window light like a marble statue, sage-grey background, dignified, editorial, 85mm --ar 4:5 --style raw --v 7'),
 ('Materiál', 'Macro still life, cocoa-brown leather folder with a blind-debossed area left blank, cayenne wax seal, limestone cotton paper card, raking light from upper left, premium stationery photography --ar 4:5 --style raw --v 7'),
]

P.append((f'''<div class="pad next">
<div><p class="eyebrow">Odovzdanie</p><h2>Identita je pripravená.</h2>
<p class="lead">Súčasťou je logo systém v SVG a PNG, 16 fotorealistických mockupov, Instagram carousel, brand manuál a texty k príspevku.</p></div>
<div class="next-cols">
<div><b>Ďalší krok</b><p>Pripomienky k výberu a poradiu fotografií alebo k carouselu zapracujeme v jednom kole.</p></div>
<div><b>Poznámka k fontom</b><p>Graze a ostatné dodané fonty nie sú súčasťou balíka. Logo je v krivkách. Pred použitím u klienta overte licenciu písma pre logo a web.</p></div>
</div></div>''', COC, LIM, 'Odovzdanie'))

# ====================================================================== MANUAL
M = []
folio = 'WEIDE · Brand Guidelines'
def mslide(c, bg=LIM, fg=COC, lab=''):
    M.append((c, bg, fg, lab))

mslide(f'''<div class="cover2"><div class="cover-top"><span>Brand Guidelines</span><span>Verzia 1.0 · 2026</span></div>
<div class="c2-mid">{mk(LOCK, LIM, w="56%")}</div><div class="cover-bot"><span>Longevity &amp; Regenerative Health</span><span>ReVisual</span></div></div>''', COC, LIM)

toc = ['Príbeh značky', 'Logo', 'Konštrukcia a ochranná zóna', 'Varianty', 'Minimálne veľkosti', 'Nesprávne použitie', 'Farby', 'Typografia', 'Grafické prvky', 'Fotografia', 'Tón komunikácie', 'Aplikácie']
mslide('<div class="pad toc"><div><p class="eyebrow">Obsah</p><h2>Ako používať WEIDE.</h2></div><ol class="toc-list">' + ''.join(f'<li><span>{i+3:02d}</span>{t}</li>' for i, t in enumerate(toc)) + '</ol></div>', lab='Obsah')

mslide(f'''<div class="pad grid-2"><div class="col"><p class="eyebrow">Príbeh značky</p><h2>Weide je vŕba.</h2>
<p class="lead">Strom, ktorý z jedného prútika vyrastie znova, z ktorého kôry vzišiel salicín a ktorý sa vo víchrici ohne, ale nezlomí. WEIDE spája vedu dlhovekosti s pokojom prírody a architektúry.</p>
<div class="facts"><div><b>Brand idea</b><p>Regenerácia, s precíznosťou.</p></div><div><b>Positioning</b><p>Longevity &amp; Regenerative Health, Rakúsko.</p></div><div><b>Hodnoty</b><p>Presnosť · Pokoj · Vitalita · Diskrétnosť</p></div><div><b>Podpis</b><p>Time, well kept.</p></div></div></div>
<div class="col pos" style="justify-content:center">{mk(SA, COC, h="70%")}</div></div>''', lab='Príbeh značky')

mslide(f'''<div class="logo-sys"><div class="ls-light" style="background:{LIM}"><span class="cap">Primárne · svetlé</span>{mk(LOCK, COC, w="70%")}</div>
<div class="ls-dark" style="background:{COC}"><span class="cap" style="color:{GLA}">Primárne · tmavé</span>{mk(LOCK, LIM, w="70%")}</div>
<div class="ls-info" style="background:{LIM};color:{COC}"><div class="ls-notes">
<div><b>Prekrížené W</b><p>Ťahy W sa prekrižujú ako vŕbové prútie. Je to nositeľ príbehu mena a samostatný monogram.</p></div>
<div><b>Spojené serify</b><p>Písmená EIDE sa dotýkajú serifmi a tvoria jednu líniu. Medzery v logu sa nikdy nemenia.</p></div>
<div><b>Dýchajúce E</b><p>Stredné rameno E je odpojené od kmeňa. Podpisový detail, ktorý sa zachováva v každej veľkosti.</p></div></div>
<div class="ls-notes"><div><b>Kedy použiť lockup</b><p>Prvé stretnutie so značkou: vstup, web, tlačoviny, prezentácie.</p></div><div><b>Kedy použiť wordmark</b><p>Keď je podnadpis zrejmý z kontextu: obaly, signáž v interiéri, sociálne siete.</p></div></div></div></div>''', lab='Logo')

body, (bx, by, bw, bh) = LA
cs = 350
guide = (f'<svg class="constr" viewBox="{-cs-120} {-700-cs-120} {bw+2*cs+240} {700+2*cs+240}" fill="{COC}">'
         f'<rect x="{-cs}" y="{-700-cs}" width="{bw+2*cs}" height="{700+2*cs}" fill="none" stroke="{CAY}" stroke-width="5" stroke-dasharray="24 16"/>'
         f'<rect x="0" y="-700" width="{bw}" height="700" fill="none" stroke="{GLA}" stroke-width="3"/>'
         + ''.join(f'<line x1="-60" x2="{bw+60}" y1="{y}" y2="{y}" stroke="{GLA}" stroke-width="2"/>' for y in (-700, -466, 0))
         + strip_defs(body)
         + f'<rect x="{-cs}" y="-700" width="{cs}" height="{cs}" fill="{CAY}" opacity=".18"/><text x="{-cs/2}" y="{-700+cs/2+25}" text-anchor="middle" font-size="80" fill="{CAY}" class="t-sans">x</text>'
         + f'<rect x="{bw}" y="{-cs}" width="{cs}" height="{cs}" fill="{CAY}" opacity=".18"/><text x="{bw+cs/2}" y="{-cs/2+25}" text-anchor="middle" font-size="80" fill="{CAY}" class="t-sans">x</text>'
         + '</svg>')
mslide(f'''<div class="pad cons"><div class="cons-l"><p class="eyebrow">Konštrukcia a ochranná zóna</p><h2>Priestor okolo znaku.</h2>
<p class="body">Ochranná zóna x sa rovná polovici výšky písmen. Do zóny nesmie zasahovať text, okraj formátu ani iný grafický prvok.</p>
<p class="body">Horizontálne vodidlá: výška verzálok, os odpojeného ramena E a účiaria. Rameno E leží na 2/3 výšky písmena.</p></div>
<div class="cons-r">{guide}</div></div>''', lab='Konštrukcia')

mslide(f'''<div class="pad vars"><div><p class="eyebrow">Varianty</p><h2>Správna podoba pre každú situáciu.</h2></div><div class="var-grid">
<div class="vg" style="background:{LIM}">{mk(LOCK, COC, w="74%")}<p>Lockup</p></div>
<div class="vg" style="background:{COC}">{mk(LA, LIM, w="74%")}<p style="color:{GLA}">Wordmark</p></div>
<div class="vg" style="background:{GLA}">{mk(SA, COC, h="48%")}<p>Monogram</p></div>
<div class="vg" style="background:{CAY}">{mk(SEAL2, LIM, h="62%")}<p style="color:{LIM}">Pečať · vosk, razba, nálepky</p></div>
<div class="vg" style="background:#fff">{mk(LA, "#000", w="74%")}<p>Čierna</p></div>
<div class="vg" style="background:#000">{mk(LA, "#fff", w="74%")}<p style="color:#fff">Biela</p></div>
</div></div>''', lab='Varianty')

mslide(f'''<div class="pad sizes2"><div><p class="eyebrow">Minimálne veľkosti</p><h2>Graze potrebuje priestor.</h2>
<p class="body">Graze má veľmi tenké vlasové ťahy. Pod 40 px používajte mikro verziu so zosilnenými ťahmi, pod 24 px už iba monogram.</p></div>
<div class="size-table">
<div><span class="cap2">Wordmark · štandard</span><div class="srow">{mk(LA, COC, h="80")}{mk(LA, COC, h="48")}</div><p>od 40 px · od 12 mm</p></div>
<div><span class="cap2">Wordmark · mikro</span><div class="srow">{mk(MICRO, COC, h="32")}{mk(MICRO, COC, h="24")}</div><p>24–40 px · 7–12 mm</p></div>
<div><span class="cap2">Monogram</span><div class="srow">{mk(SA, COC, h="40")}{mk(SA, COC, h="16")}</div><p>od 16 px · od 5 mm · favicon</p></div>
<div><span class="cap2">Pečať</span><div class="srow">{mk(SEAL2, COC, h="96")}{mk(SEAL2, COC, h="64")}</div><p>od 64 px · od 20 mm</p></div>
</div></div>''', lab='Minimálne veľkosti')

def bad(inner, bg, txt):
    return f'<div class="bad"><div class="bad-art" style="background:{bg}">{inner}<svg class="x" viewBox="0 0 100 100" preserveAspectRatio="none"><line x1="0" y1="100" x2="100" y2="0" stroke="{CAY}" stroke-width=".8"/></svg></div><p>{txt}</p></div>'
wide = logo_GA({0: 90, 1: 90, 2: 90, 3: 90})
mslide(f'''<div class="pad misuse"><div><p class="eyebrow">Nesprávne použitie</p><h2>Čo s logom nerobiť.</h2></div><div class="bad-grid">
{bad(mk(LA, COC, w="70%").replace('<svg class="mark"', '<svg class="mark" style="transform:scaleX(1.45)"', 1), LIM, 'Nedeformovať')}
{bad(mk(LA, GLA, w="70%"), LIM, 'Nepoužívať farby s nízkym kontrastom')}
{bad(mk(LA, COC, w="70%").replace('<svg class="mark"', '<svg class="mark" style="filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))"', 1), LIM, 'Nepridávať tiene ani efekty')}
{bad(mk(wide, COC, w="80%"), LIM, 'Nemeniť medzery medzi písmenami')}
{bad(mk(LA, COC, w="64%").replace('<svg class="mark"', '<svg class="mark" style="transform:rotate(-14deg)"', 1), LIM, 'Neotáčať')}
{bad('<svg class="busy" viewBox="0 0 600 340" preserveAspectRatio="xMidYMid slice"><rect width="600" height="340" fill="' + GLA + '"/><g transform="translate(-700,-40)">' + willow(seed=5, x0=700, x1=1300, n=16, scale=.8) + '</g></svg>' + mk(LA, COC, w="70%").replace('<svg class="mark"', '<svg class="mark over"', 1), GLA, 'Neumiestňovať na rušivé pozadie')}
</div></div>''', lab='Nesprávne použitie')

combos = [(LIM, COC, 'Sand Limestone na Cocoa', '9.6 : 1'), (COC, LIM, 'Cocoa na Sand Limestone', '9.6 : 1'), (COC, GLA, 'Cocoa na Glass', '6.8 : 1'), (LIM, CAY, 'Sand Limestone na Cayenne', '4.1 : 1 · veľký text'), (GLA, COC, 'Glass na Cocoa', '6.8 : 1'), (CAY, LIM, 'Cayenne na Sand Limestone', '4.1 : 1 · veľký text')]
mslide(f'''<div class="pad colors"><div class="col-l"><p class="eyebrow">Farby</p><h2>Paleta a pomer.</h2>
{ratio([('Bitter Cocoa', COC, 48, LIM), ('Sand Limestone', LIM, 26, COC), ('Weathered Glass', GLA, 16, COC), ('Cayenne', CAY, 10, LIM)])}
<div class="specs">{''.join(f'<div><i style="background:{h}"></i><b>{n}</b><span>HEX {h} · RGB {rgb} · CMYK {cmyk}</span></div>' for n, h, rgb, cmyk in (('Cayenne Dust', CAY, '157 63 13', '24 74 100 13'), ('Weathered Glass', GLA, '154 176 170', '42 18 29 5'), ('Bitter Cocoa', COC, '57 27 23', '46 78 72 70'), ('Sand Limestone', LIM, '216 201 183', '15 18 26 0')))}</div>
<p class="body">Cocoa nesie značku, Sand Limestone dáva vzduch, Glass upokojuje a Cayenne je akcent: tlačidlá, pečať, jeden prvok na formát.</p></div>
<div class="combo-grid">{''.join(f'<div class="combo" style="background:{b};color:{f}"><span class="cmb-big">Aa</span><span>{n}</span><b>{c}</b></div>' for f, b, n, c in combos)}</div></div>''', lab='Farby')

mslide(f'''<div class="pad typo2"><div><p class="eyebrow">Typografia</p><h2>Tri hlasy, jasné úlohy.</h2></div>
<div class="t2-rows">
<div class="t2"><div class="t2-meta"><b>Graze</b><span>Logo a anglické display titulky · iba v krivkách</span></div><div class="t2-spec">{outline_svg(GRAZE, "Time, well kept.")}</div></div>
<div class="t2"><div class="t2-meta"><b>Cormorant Garamond</b><span>Titulky v slovenčine a nemčine · 400 · riadkovanie 1.05</span></div><div class="t2-spec tf-cormorant" style="font-size:4.4em;line-height:1">Dlhovekosť, ľudsky.</div></div>
<div class="t2"><div class="t2-meta"><b>DM Sans</b><span>Text, UI, popisky · 400 / 500 · 16 / 1.6</span></div><div class="t2-spec tf-dmsans" style="font-size:1.3em;line-height:1.6;max-width:36em">Regeneratívna medicína, presná diagnostika a osobný plán na ďalšie desaťročia. V pokoji rakúskeho domu.</div></div>
<div class="t2"><div class="t2-meta"><b>Popisky</b><span>DM Sans 500 · verzálky · prestrkanie +0.24 em</span></div><div class="t2-spec tf-dmsans" style="font-size:1em;letter-spacing:.24em;text-transform:uppercase">Diagnostics · Regeneration · Longevity</div></div>
</div></div>''', lab='Typografia')

def el(svg, t, d):
    return f'<div class="el"><div class="el-art">{svg}</div><b>{t}</b><p>{d}</p></div>'
pin = f'<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice"><rect width="400" height="300" fill="{COC}"/>' + ''.join(f'<line x1="{x}" x2="{x}" y1="0" y2="300" stroke="#5a2e24" stroke-width="1.4"/>' for x in range(10, 400, 18)) + '</svg>'
oval = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{COC}"/><clipPath id="elo"><ellipse cx="200" cy="150" rx="80" ry="120"/></clipPath><g clip-path="url(#elo)"><rect x="100" y="20" width="200" height="270" fill="#1d0c09"/><rect x="100" y="20" width="200" height="270" fill="url(#hAglow)"/><circle cx="200" cy="190" r="34" fill="url(#hAsphere)"/></g><ellipse cx="200" cy="150" rx="80" ry="120" fill="none" stroke="{GLA}" stroke-opacity=".6"/><defs>{SCENE_DEFS}</defs></svg>'
rep_s = 300 / bw; rep_h = 700 * rep_s
rep = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{GLA}"/>' + ''.join(f'<g transform="translate(50,{30 + i*(rep_h+8):.0f}) scale({rep_s:.4f}) translate(0,700)" {"fill=" + chr(34) + CAY + chr(34) if i == 1 else "fill=" + chr(34) + "none" + chr(34) + " stroke=" + chr(34) + COC + chr(34) + " stroke-width=" + chr(34) + f"{1.2/rep_s:.1f}" + chr(34)}>{strip_defs(body)}</g>' for i in range(3)) + '</svg>'
frame = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{LIM}"/>' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="{COC}" opacity=".5"/>' for x, y, w in ((16, 16, 120), (300, 16, 84), (16, 280, 90), (170, 280, 60), (310, 280, 74))) + f'<rect x="60" y="80" width="280" height="140" fill="{TRA}"/></svg>'
seal_el = f'<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="{LIM}"/><g filter="url(#liftS)"><g filter="url(#raise)"><path d="{wax_blob(200, 150, 100, seed=6)}" fill="url(#wax)"/></g></g><g filter="url(#debossWax)">{nest(SEAL2, CAY, CAY, 125, 75, 150)}</g></svg>'
mslide(f'''<div class="pad els"><div><p class="eyebrow">Grafické prvky</p><h2>Jazyk okolo loga.</h2></div><div class="el-grid">
{el(pin, 'Prútie', 'Jemné zvislé linky ako vŕbové prúty. Pozadie pre tmavé plochy, 1 px, odtieň o krok svetlejší.')}
{el(oval, 'Oválne okno', 'Výrez pre fotografiu alebo sochárske motívy. Pomer 2 : 3, tenký Glass obrys.')}
{el(rep, 'Rytmus wordmarku', 'Wordmark v obryse, opakovaný a orezaný. Jeden riadok môže byť plný, v Cayenne.')}
{el(frame, 'Editoriálny rám', 'Drobné popisky v rohoch formátu: značka, autor, rok, miesto, číslovanie.')}
{el(seal_el, 'Pečať', 'Vosková pečať v Cayenne alebo slepotlač. Pre osobné a slávnostné momenty.')}
</div></div>''', lab='Grafické prvky')

mslide(f'''<div class="pad photo"><div class="ph-l"><p class="eyebrow">Fotografia</p><h2>Svetlo, ktoré modeluje formu.</h2>
<div class="facts">
<div><b>Šerosvit</b><p>Jeden teplý zdroj svetla, hlboké tiene, veľa negatívneho priestoru.</p></div>
<div><b>Človek ako socha</b><p>Telo a pokoj, nie výkon. Žiadne pózovanie ani úsmev do objektívu.</p></div>
<div><b>Materiál</b><p>Travertín, koža, sklo, bavlnený papier, bronz. Detail namiesto celku.</p></div>
<div><b>Farebnosť</b><p>Teplé tóny posunuté do Cocoa a Cayenne, svetlá v Glass. Jemné zrno.</p></div></div></div>
<div class="ph-r"><img src="mockups/WEIDE_13_hero-body.jpg" alt="WEIDE kampaň"></div></div>''', lab='Fotografia')

mslide('''<div class="pad grid-2"><div class="col"><p class="eyebrow">Tón komunikácie</p><h2>Hovoríme menej, s istotou.</h2>
<p class="lead">Pokojne, presne a kultivovane. Bez superlatívov, bez sľubov, ktoré nevieme overiť. Vedu vysvetľujeme ľudsky.</p></div>
<div class="col tone"><div class="tn"><span>Áno</span><p>Precízna diagnostika a osobný plán na ďalšie desaťročia.</p></div><div class="tn no"><span>Nie</span><p>Revolučná terapia, ktorá vás omladí o 20 rokov!</p></div>
<div class="tn"><span>Áno</span><p>Time, well kept.</p></div><div class="tn no"><span>Nie</span><p>Najlepšie longevity centrum v Európe.</p></div></div></div>''', lab='Tón komunikácie')

thumbs = ''.join(f'<div class="ap"><div class="ap-art"><img src="mockups/WEIDE_{nn}_{slug}.jpg" alt="{t}" loading="lazy"></div><p>{t}</p></div>' for nn, slug, t in [PH[i] for i in (14, 10, 11, 7, 6, 8, 15, 0)])
mslide(f'<div class="pad apps"><div><p class="eyebrow">Aplikácie</p><h2>WEIDE v priestore, papieri a obrazovke.</h2></div><div class="ap-grid">{thumbs}</div></div>', lab='Aplikácie')

mslide(f'''<div class="cover2"><div class="cover-top"><span>Brand Guidelines</span><span>ReVisual</span></div>
<div class="c2-mid">{mk(SEAL2, LIM, w="26%")}</div><div class="cover-bot"><span>Time, well kept.</span><span>© 2026 ReVisual</span></div></div>''', COC, LIM)

os.makedirs(OUT, exist_ok=True)
for name, title, slides in (('index', 'WEIDE Brand Identity', P), ('manual', 'WEIDE Brand Guidelines', M)):
    folio = 'WEIDE · Phase 2' if name == 'index' else 'WEIDE · Brand Guidelines'
    open(f'{OUT}/{name}.html', 'w').write(page(title, slides))
    open(f'{OUT}/{name}.render.html', 'w').write(page(title, slides, local=True))
open(f'{OUT}/ig.render.html', 'w').write('<!doctype html><meta charset="utf-8"><style>' + LOCAL + CSS + 'body{margin:0}.g{width:1080px;height:1350px}.g>svg{display:block;width:1080px;height:1350px}</style>' + GLOBAL_DEFS + ''.join(f'<div class="g">{f()}</div>' for f in SLIDES))
open(f'{OUT}/mocks.render.html', 'w').write('<!doctype html><meta charset="utf-8"><style>' + LOCAL + CSS + 'body{margin:0}.m{width:1920px;height:1080px}.m>svg{display:block;width:1920px;height:1080px}</style>' + GLOBAL_DEFS + ''.join(f'<div class="m">{f()}</div>' for t, f in MOCKS))
print(len(P), len(M))
