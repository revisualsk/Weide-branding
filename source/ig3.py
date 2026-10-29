import os, sys
from ig2 import *
PH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'photos'))

def counter(n, fg=LIM):
    return f'<text x="1024" y="1300" text-anchor="end" class="t-sans" font-size="15" letter-spacing="3" fill="{fg}" opacity=".8">{n:02d} / 10</text>'

def photo(name, n, fg=LIM, align='xMidYMid'):
    return (f'<svg class="igs" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">'
            f'<image href="file://{PH}/{name}.jpg" x="0" y="0" width="1080" height="1350" preserveAspectRatio="{align} slice"/>'
            f'{counter(n, fg)}</svg>')

def typo(fn, n):
    # reuse vector slides, renumbered
    svg = fn()
    import re
    return re.sub(r'\d\d / 10', f'{n:02d} / 10', svg)

SLIDES3 = [
 lambda: photo('hero-body', 1),
 lambda: typo(s2, 2),
 lambda: typo(s3, 3),
 lambda: photo('entrance', 4),
 lambda: photo('palette-vertical', 5, COC),
 lambda: photo('business-cards', 6),
 lambda: photo('fluted-glass', 7),
 lambda: photo('treatment-room', 8),
 lambda: photo('web-tablet', 9),
 lambda: photo('stationery', 10),
]
if __name__ == '__main__':
    css = open('deck.css').read() + open('p2.css').read()
    fd = os.environ['FONTDIR']
    faces = '\n'.join(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{fd}/{fn}.ttf')}}" for fn, fam, w, st in
        [('CormorantGaramond-400', 'Cormorant Garamond', 400, 'normal'), ('CormorantGaramond-500', 'Cormorant Garamond', 500, 'normal'), ('CormorantGaramond-400i', 'Cormorant Garamond', 400, 'italic'), ('DMSans-400', 'DM Sans', 400, 'normal'), ('DMSans-500', 'DM Sans', 500, 'normal')])
    open(sys.argv[1], 'w').write('<!doctype html><meta charset="utf-8"><style>' + faces + css + 'body{margin:0}.g{width:1080px;height:1350px}.g>svg{display:block;width:1080px;height:1350px}</style>' + GLOBAL_DEFS + ''.join(f'<div class="g">{f()}</div>' for f in SLIDES3))
