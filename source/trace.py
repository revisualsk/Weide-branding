import sys, numpy as np, potrace
from PIL import Image, ImageFilter
src, out, thr = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = Image.open(src).convert('L')
box = tuple(int(v) for v in sys.argv[4].split(','))
im = im.crop(box)
S = 6
im = im.resize((im.width * S, im.height * S), Image.LANCZOS).filter(ImageFilter.GaussianBlur(2.2))
a = np.array(im).astype(float)
bm = potrace.Bitmap(a < thr)
path = bm.trace(turdsize=60, alphamax=1.0, opticurve=True, opttolerance=0.2)
d = []
for c in path:
    s = c.start_point; d.append(f'M{s.x/S:.2f} {s.y/S:.2f}')
    for seg in c:
        if seg.is_corner:
            d.append(f'L{seg.c.x/S:.2f} {seg.c.y/S:.2f}L{seg.end_point.x/S:.2f} {seg.end_point.y/S:.2f}')
        else:
            d.append(f'C{seg.c1.x/S:.2f} {seg.c1.y/S:.2f} {seg.c2.x/S:.2f} {seg.c2.y/S:.2f} {seg.end_point.x/S:.2f} {seg.end_point.y/S:.2f}')
    d.append('Z')
w, h = box[2]-box[0], box[3]-box[1]
open(out, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill-rule="evenodd" d="{"".join(d)}"/></svg>')
print(len(path), 'paths')
