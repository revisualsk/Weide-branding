import json, math
from logos import G, leaf, para

# A2 — Woven: Cormorant Garamond 600, tight display spacing, woven W, breathing E
def logo_A2(sp=None):
    g=G('cg600v.json'); V=g['V']; parts=[]
    vshift=230
    parts.append(f'<path d="{V["d"]}"/>')
    parts.append(f'<path transform="translate({vshift},0)" d="{V["d"]}"/>')
    x=vshift+662
    sp=sp or {'WE':-6,'EI':22,'ID':22,'DE':14}
    prev='W'
    for ch in 'EIDE':
        x+=sp[prev+ch]; gg=g[ch]
        if ch=='E':
            parts.append(f'<g transform="translate({x},0)"><path d="{gg["d"]}" clip-path="url(#aCut)"/><rect x="236" y="-345" width="172" height="17"/></g>')
        else:
            parts.append(f'<path transform="translate({x},0)" d="{gg["d"]}"/>')
        x+=gg['adv']; prev=ch
    defs='<defs><clipPath id="aCut"><path d="M0 -700H600V-428H213V-212H600V100H0Z"/></clipPath></defs>'
    return defs+'<g>'+''.join(parts)+'</g>',(0,-625,x,628)

def seal_A():
    g=G('cg600v.json'); V=g['V']
    s=0.62; w=899*s; R=520
    ox=-w/2; oy=625*s/2
    return (f'<circle cx="0" cy="0" r="{R}" fill="none" stroke="currentColor" stroke-width="10"/>'
            f'<circle cx="0" cy="0" r="{R-40}" fill="none" stroke="currentColor" stroke-width="3"/>'
            f'<g transform="translate({ox:.1f},{oy:.1f}) scale({s})"><path d="{V["d"]}"/><path transform="translate(230,0)" d="{V["d"]}"/></g>'),(-R-6,-R-6,2*R+12,2*R+12)

# B2 — Monolith Light: constructed caps, hairline-strong strokes, wide architectural tracking
def logo_B2(S=46,T=40,th=50,gap=230):
    P=[]
    W=[(0,250),(470,250),(470,720),(940,720)]
    for xt,xb in W: P.append(('',para(xt,xb,th)))
    x=940+th
    def E(x0):
        w=430
        return f'M{x0} -700H{x0+w}V{-700+T}H{x0+S}V{-350-T/2}H{x0+w-30}V{-350+T/2}H{x0+S}V{-T}H{x0+w}V0H{x0}Z', x0+w
    x+=gap; d,x=E(x); P.append(('',d))
    x+=gap; P.append(('I',f'M{x} -700H{x+S}V0H{x}Z')); x+=S
    x+=gap
    R=350; L=110; x0=x
    outer=f'M{x0} -700H{x0+L}A{R} {R} 0 0 1 {x0+L} 0H{x0}Z'
    ri=R-T; cx=x0+L-(S-T)
    inner=f'M{x0+S} {-700+T}H{cx}A{ri} {ri} 0 0 1 {cx} {-T}H{x0+S}Z'
    P.append(('',outer+inner)); x=x0+L+R
    x+=gap; d,x=E(x); P.append(('',d))
    body=''.join(f'<path fill-rule="evenodd" {"class=\"accent\"" if k=="I" else ""} d="{d}"/>' for k,d in P)
    return body,(0,-700,x,700)

def symbol_B2(S=46):
    w=520; R=w/2; h=900
    outer=f'M0 0V{-(h-R)}A{R} {R} 0 0 1 {w} {-(h-R)}V0H{w-S}V{-(h-R)}A{R-S} {R-S} 0 0 0 {S} {-(h-R)}V0Z'
    col=f'M{R-S/2} 0V{-(h-R)-60}H{R+S/2}V0Z'
    return f'<path d="{outer}"/><path class="accent" d="{col}"/>',(0,-h,w,h)

# C2 — Living Willow: Cormorant Garamond 500 lowercase, leaf tittle, cut ascender
def logo_C2():
    d=json.load(open('CormorantGaramond-500.json')); gl={g['ch']:g for g in d['glyphs'][5:]}
    sp={'we':-14,'ei':-4,'id':-2,'de':-6}
    parts=[];x=0;prev=None
    for ch in 'weide':
        if prev: x+=sp[prev+ch]
        gg=gl[ch]; dd=gg['d']
        if ch=='i':
            stem=dd[:dd.index('Z')+1]
            parts.append(f'<path transform="translate({x},0)" d="{stem}"/>')
            parts.append(f'<path class="accent" transform="translate({x},0)" d="{leaf(142,-572,190,40,-60)}"/>')
        elif ch=='d':
            parts.append(f'<path transform="translate({x},0)" clip-path="url(#cCut2)" d="{dd}"/>')
        else:
            parts.append(f'<path transform="translate({x},0)" d="{dd}"/>')
        x+=gg['adv']; prev=ch
    defs='<defs><clipPath id="cCut2"><path d="M-50 100V-560H300L460 -700V100Z"/></clipPath></defs>'
    return defs+''.join(parts),(0,-665,x,678)

def symbol_C2():
    d=json.load(open('CormorantGaramond-500.json')); dd=d['glyphs'][7]['d']; stem=dd[:dd.index('Z')+1]
    return f'<path d="{stem}"/><path class="accent" d="{leaf(142,-572,190,40,-60)}"/>',(0,-680,270,680)

if __name__=='__main__':
    from logos import svg
    h='<body style="margin:0;background:#F2EDE5">'
    for (b,box),acc in [(logo_A2(),None),(logo_B2(),'#9D3F0D'),(logo_C2(),'#9D3F0D')]:
        h+='<div style="padding:30px 40px">'+svg(b,box,accent=acc,pad=20,h=170)+'</div>'
        h+='<div style="padding:30px 40px;background:#391B17">'+svg(b,box,fill='#F2EDE5',accent='#9AB0AA' if acc else None,pad=20,h=170)+'</div>'
    h+='<div style="padding:20px;display:flex;gap:40px;color:#391B17">'
    for b,box in [seal_A(),symbol_B2(),symbol_C2()]:
        h+=svg(b,box,accent='#9D3F0D',pad=20,h=180)
    h+='</div>'
    open('logos2.html','w').write(h)
