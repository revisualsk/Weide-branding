import json, math
def G(f): 
    d=json.load(open(f)); return {g['ch']:g for g in d['glyphs']}

# ---------- A  Editorial Luxury: Cormorant Garamond 600, woven W, breathing E ----------
def logo_A(track=None):
    g=G('cg600v.json')
    V=g['V']; parts=[]; x=0
    # woven W: two interlocking V's (willow weave). overlap tuned
    vshift=230
    parts.append(f'<path d="{V["d"]}"/>')
    parts.append(f'<path transform="translate({vshift},0)" d="{V["d"]}"/>')
    x=vshift+662
    sp={'WE':70,'EI':120,'ID':120,'DE':115}
    seq='EIDE'; prev='W'
    for ch in seq:
        x+=sp[prev+ch]
        gg=g[ch]
        if ch=='E':
            # mask out middle arm + spur, redraw detached hairline arm
            mid=f'''<g transform="translate({x},0)"><path d="{gg['d']}" clip-path="url(#aCut)"/><rect x="236" y="-345" width="172" height="17"/></g>'''
            parts.append(mid)
        else:
            parts.append(f'<path transform="translate({x},0)" d="{gg["d"]}"/>')
        x+=gg['adv']; prev=ch
    defs='<defs><clipPath id="aCut"><path d="M0 -700H600V-428H213V-212H600V100H0Z"/></clipPath></defs>'
    return defs+'<g>'+''.join(parts)+'</g>', (0,-625,x,628)

# ---------- B  Architectural Modernism: custom constructed caps ----------
def para(xt,xb,th,h=700): return f'M{xt} {-h}H{xt+th}L{xb+th} 0H{xb}Z'
def logo_B(icol=None):
    H=700; S=96; T=80; P=[]; x=0
    th=104
    W=[(0,230),(430,230),(430,640),(860,640)]
    for xt,xb in W: P.append(('',para(xt,xb,th)))
    x=860+th
    def E(x0):
        w=455
        return f'M{x0} -700H{x0+w}V{-700+T}H{x0+S}V{-350-T/2+6}H{x0+w-25}V{-350+T/2+6}H{x0+S}V{-T}H{x0+w}V0H{x0}Z', x0+w
    x+=150; d,x=E(x); P.append(('',d))
    x+=150; P.append(('I',f'M{x} -700H{x+S}V0H{x}Z')); x+=S
    x+=150
    R=350; L=150; x0=x
    # D: stem + straight + semicircle ; counter offset so curve weight == S
    outer=f'M{x0} -700H{x0+L}A{R} {R} 0 0 1 {x0+L} 0H{x0}Z'
    ri=R-T; cx=x0+L-(S-T)
    inner=f'M{x0+S} {-700+T}H{cx}A{ri} {ri} 0 0 1 {cx} {-T}H{x0+S}Z'
    P.append(('',outer+inner)); x=x0+L+R
    x+=150; d,x=E(x); P.append(('',d))
    body=''.join(f'<path fill-rule="evenodd" {"class=\"accent\"" if k=="I" else ""} d="{d}"/>' for k,d in P)
    return body,(0,-700,x,700)

def symbol_B():
    # arch portal with column: outer arch, inner opening, central column
    S=96; w=560; R=w/2; h=900
    outer=f'M0 0V{-(h-R)}A{R} {R} 0 0 1 {w} {-(h-R)}V0H{w-S}V{-(h-R)}A{R-S} {R-S} 0 0 0 {S} {-(h-R)}V0Z'
    col=f'M{R-S/2} 0V{-(h-R)-40}H{R+S/2}V0Z'
    return f'<path d="{outer}"/><path class="accent" d="{col}"/>',(0,-h,w,h)

# ---------- C  Contemporary Longevity: DM Serif Display lowercase, leaf tittle, cut ascender ----------
def leaf(cx,cy,L,Wd,ang):
    a=math.radians(ang); ca,sa=math.cos(a),math.sin(a)
    def p(u,v): return f'{cx+u*ca-v*sa:.1f} {cy+u*sa+v*ca:.1f}'
    k=Wd*1.33
    return f'M{p(-L/2,0)}C{p(-L/4,-k)} {p(L/4,-k*0.9)} {p(L/2,0)}C{p(L/4,k*0.9)} {p(-L/4,k)} {p(-L/2,0)}Z'
def logo_C():
    g=G('DMSerifDisplay-400.json')
    gl={c:g[c] for c in 'weid'}
    sp={'we':-6,'ei':4,'id':6,'de':-2}
    parts=[];x=0;prev=None
    for ch in 'weide':
        if prev: x+=sp[prev+ch]
        gg=gl[ch]; d=gg['d']
        if ch=='i':
            stem=d[d.index('Z')+1:]
            parts.append(f'<path transform="translate({x},0)" d="{stem}"/>')
            parts.append(f'<path class="accent" transform="translate({x},0)" d="{leaf(146,-655,236,54,-60)}"/>')
        elif ch=='d':
            parts.append(f'<path transform="translate({x},0)" clip-path="url(#cCut)" d="{d}"/>')
        else:
            parts.append(f'<path transform="translate({x},0)" d="{d}"/>')
        x+=gg['adv']; prev=ch
    defs='<defs><clipPath id="cCut"><path d="M-50 100V-505L372 -505L372 -604L512 -690V100Z"/></clipPath></defs>'
    return defs+''.join(parts),(0,-745,x,760)

def symbol_C():
    g=G('DMSerifDisplay-400.json'); d=g['i']['d']; stem=d[d.index('Z')+1:]
    return f'<path d="{stem}"/><path class="accent" d="{leaf(146,-655,236,54,-60)}"/>',(0,-760,280,760)

def symbol_A():
    g=G('cg600v.json'); V=g['V']
    return f'<path d="{V["d"]}"/><path transform="translate(230,0)" d="{V["d"]}"/>',(0,-625,899,628)

def svg(body,box,fill='#391B17',accent=None,pad=0,h=None,cls=''):
    x,y,w,hh=box; accent=accent or fill
    hs=f' height="{h}"' if h else ''
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{x-pad} {y-pad} {w+2*pad} {hh+2*pad}"{hs} fill="{fill}"><style>.accent{{fill:{accent}}}</style>{body}</svg>'
if __name__=='__main__':
    h='<body style="margin:0;background:#F2EDE5">'
    for (b,box),acc in [(logo_A(),None),(logo_B(),'#9D3F0D'),(logo_C(),'#9D3F0D')]:
        h+='<div style="padding:30px">'+svg(b,box,accent=acc,pad=20,h=180)+'</div>'
        h+='<div style="padding:30px;background:#391B17">'+svg(b,box,fill='#F2EDE5',accent='#9AB0AA' if acc else None,pad=20,h=180)+'</div>'
    for b,box in [symbol_A(),symbol_B(),symbol_C()]:
        h+=svg(b,box,accent='#9D3F0D',pad=40,h=160)
    open('logos.html','w').write(h)
