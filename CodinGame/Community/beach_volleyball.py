#!/usr/bin/env python3

# NB: This is actually analog to Descartes' law of refraction
#     following Fermat's principle.
# https://en.wikipedia.org/wiki/Snell's_law
# Indeed, if
# t(x) = √((x-x0)²+(yb-y0)²)/s0 + √((x1-x)²+(y1-yb)²)/s1
# t'(x) = (x-x0)/√((x-x0)²+(yb-y0)²)/s0 - (x1-x)/√((x1-x)²+(y1-yb)²)/s0
# for α & β the oriented angles to the normal, we have
#     sin α = (x-x0)/√((x-x0)²+(yb-y0)²)
# and sin β = (x1-x)/√((x1-x)²+(y1-yb)²)
# hence sin α / s0 = sin β / s1

# That said, this does not lead to simple explicit formulas for
# the solution x... We use ternary search below.

from math import sqrt

x0,y0 = map(int, input().split())
yb = int(input())
x1,y1 = map(int, input().split())
s0 = int(input())
s1 = int(input())

dist = lambda x: sqrt((x-x0)**2+(yb-y0)**2)/s0 + sqrt((x1-x)**2+(y1-yb)**2)/s1
xl,xr = (x0,x1) if x0<x1 else (x1,x0)
while xr-xl > 0.5:
    xml = (2.*xl+xr)/3.
    xmr = (xl+2.*xr)/3.
    if dist(xml) > dist(xmr):
        xl = xml
    else:
        xr = xmr
x = min(range(int(xl), int(xr)+2), key=dist)
print(x)
