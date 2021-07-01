#!/usr/bin/env python3

from math import *

W,H,r,s,x0,y0 = (float(input()) for _ in range(6))

dx = s*cos(r)
dy = s*sin(r)
x1 = W if dx>0. else 0.
t = ceil((x1-x0)/dx)
y1 = y0 + t*dy
cy,y1 = divmod(y1, H)
if cy%2.:
    y1 = H-y1
print(t, round(y1,2) if y1%1. else int(y1))
