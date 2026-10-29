import sys,json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
F=sys.argv[1]; text=sys.argv[2]
f=TTFont(F); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
os2=f['OS/2']
out={'upm':upm,'cap':getattr(os2,'sCapHeight',0),'x':getattr(os2,'sxHeight',0),'glyphs':[]}
for ch in text:
    g=cmap[ord(ch)]; pen=SVGPathPen(gs)
    tp=TransformPen(pen,(1,0,0,-1,0,0)); gs[g].draw(tp)
    out['glyphs'].append({'ch':ch,'adv':gs[g].width,'d':pen.getCommands()})
print(json.dumps(out))
