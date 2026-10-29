import math, random
def emboss_filter(fid, scale=-5, blur=2.4, az=235, el=38, k=2.6, inner=.14, src=False, ink=(0.08,0.03,0.02), hi=(1,.97,.92), himax=1, shmax=1, clip=False):
    flat=math.sin(math.radians(el))
    srcnode='<feMergeNode in="SourceGraphic"/>' if src else ''
    return f'''<filter id="{fid}" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
<feGaussianBlur in="SourceAlpha" stdDeviation="{blur}" result="b"/>
<feDiffuseLighting in="b" surfaceScale="{scale}" diffuseConstant="1" lighting-color="#fff" result="l"><feDistantLight azimuth="{az}" elevation="{el}"/></feDiffuseLighting>
<feColorMatrix in="l" type="matrix" values="0 0 0 0 {hi[0]}  0 0 0 0 {hi[1]}  0 0 0 0 {hi[2]}  {k} 0 0 0 {-k*flat:.3f}" result="hi0"/><feComponentTransfer in="hi0" result="hi"><feFuncA type="linear" slope="{himax}"/></feComponentTransfer>
<feColorMatrix in="l" type="matrix" values="0 0 0 0 {ink[0]}  0 0 0 0 {ink[1]}  0 0 0 0 {ink[2]}  {-k} 0 0 0 {k*flat:.3f}" result="sh0"/><feComponentTransfer in="sh0" result="sh"><feFuncA type="linear" slope="{shmax}"/></feComponentTransfer>
<feFlood flood-color="#000" flood-opacity="{inner}"/><feComposite in2="SourceAlpha" operator="in" result="inner"/>
{'<feComposite in="hi" in2="SourceAlpha" operator="in" result="hi"/><feComposite in="sh" in2="SourceAlpha" operator="in" result="sh"/>' if clip else ''}<feMerge>{srcnode}<feMergeNode in="inner"/><feMergeNode in="sh"/><feMergeNode in="hi"/></feMerge></filter>'''

def texture_filter(fid, freq='.55', oct=2, scale=1.6, seed=2, el=50, k=2.2, op=1):
    flat=math.sin(math.radians(el))
    return f'''<filter id="{fid}" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="{oct}" seed="{seed}" result="n"/>
<feDiffuseLighting in="n" surfaceScale="{scale}" lighting-color="#fff" result="l"><feDistantLight azimuth="235" elevation="{el}"/></feDiffuseLighting>
<feColorMatrix in="l" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  {k} 0 0 0 {-k*flat:.3f}" result="hi"/>
<feColorMatrix in="l" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  {-k} 0 0 0 {k*flat:.3f}" result="sh"/>
<feMerge><feMergeNode in="sh"/><feMergeNode in="hi"/></feMerge><feComposite in2="SourceGraphic" operator="in"/></filter>'''

MAT_DEFS = ''.join([
  emboss_filter('deboss', -4, 2.6, k=1.6, himax=.6, shmax=.45, inner=.04, ink=(.3,.2,.14)),
  emboss_filter('debossWax', -4, 2.2, k=1.8, himax=.45, shmax=.6, inner=.08, ink=(.25,.06,0), hi=(1,.8,.6)),
  emboss_filter('debossLeather', -7, 3.4, k=1.5, inner=.2, hi=(.62,.42,.36), himax=.6, shmax=.75),
  emboss_filter('debossDeep', -9, 3.2, inner=.22),
  emboss_filter('embossS', 4, 1.6, inner=0),
  emboss_filter('raise', 14, 9, el=42, k=1.6, inner=0, src=True, clip=True, himax=.6),
  emboss_filter('foilE', 3, 1.2, inner=0, src=True, k=3.2),
  texture_filter('leather', '.42', 3, 2.4, 5, 55, 1.6),
  texture_filter('paper', '.9', 2, 0.9, 8, 60, 1.2),
  texture_filter('clay', '.05', 4, 2.4, 3, 50, 1.0),
])

def wax_blob(cx, cy, r, seed=3, n=48):
    rnd=random.Random(seed); pts=[]
    for i in range(n):
        a=2*math.pi*i/n; rr=r*(1+0.03*math.sin(a*3+seed)+0.02*math.sin(a*7+2*seed)+rnd.uniform(-.018,.018))
        pts.append((cx+rr*math.cos(a), cy+rr*math.sin(a)))
    d='M'+' '.join(f'{x:.1f} {y:.1f}' for x,y in pts[:1])
    for i in range(1,n+1):
        x0,y0=pts[i-1]; x1,y1=pts[i%n]; d+=f' Q{x0:.1f} {y0:.1f} {(x0+x1)/2:.1f} {(y0+y1)/2:.1f}'
    return d+'Z'
