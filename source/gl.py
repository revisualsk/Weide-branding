from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
_c={}
def font(p):
    if p not in _c: _c[p]=TTFont(p)
    return _c[p]
def glyph(p, name):
    f=font(p); gs=f.getGlyphSet()
    if len(name)==1: name=f.getBestCmap()[ord(name)]
    pen=SVGPathPen(gs); gs[name].draw(TransformPen(pen,(1,0,0,-1,0,0)))
    bp=BoundsPen(gs); gs[name].draw(bp)
    return pen.getCommands(), gs[name].width, bp.bounds
def kern(p,a,b):
    # GPOS pair kerning lookup (simple pairpos)
    f=font(p); cm=f.getBestCmap()
    a=cm.get(ord(a),a) if len(a)==1 else a; b=cm.get(ord(b),b) if len(b)==1 else b
    if 'GPOS' not in f: return 0
    for lk in f['GPOS'].table.LookupList.Lookup:
        for st in lk.SubTable:
            if getattr(st,'LookupType',0)==9: st=st.ExtSubTable
            if getattr(st,'Format',0)==1 and hasattr(st,'PairSet'):
                cov=st.Coverage.glyphs
                if a in cov:
                    for pv in st.PairSet[cov.index(a)].PairValueRecord:
                        if pv.SecondGlyph==b and pv.Value1: return getattr(pv.Value1,'XAdvance',0) or 0
            if getattr(st,'Format',0)==2 and hasattr(st,'ClassDef1'):
                if a in st.Coverage.glyphs:
                    c1=st.ClassDef1.classDefs.get(a,0); c2=st.ClassDef2.classDefs.get(b,0)
                    v=st.Class1Record[c1].Class2Record[c2].Value1
                    if v: return getattr(v,'XAdvance',0) or 0
    return 0
def word(p, names, track=0, extra=None):
    x=0; parts=[]; extra=extra or {}
    for i,n in enumerate(names):
        d,adv,_=glyph(p,n)
        parts.append(f'<path transform="translate({x},0)" d="{d}"/>')
        x+=adv+track+extra.get(i,0)
        if i+1<len(names) and len(n)==1 and len(names[i+1])==1: x+=kern(p,n,names[i+1])
    return ''.join(parts), x-track
