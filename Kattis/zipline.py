#!/usr/bin/env python3

from math import hypot

T = int(input())
for _ in range(T):
    W,G,H,R = map(int,input().split())
    L = lambda x: hypot(G-R,x) + hypot(W-x,H-R)
    dL = lambda x: x/hypot(G-R,x) + (x-W)/hypot(W-x,H-R)
    xl, xr = 0, W
    while xr-xl>1e-6:
        xm = (xl+xr)/2.
        if dL(xm)<0:
            xl = xm
        else:
            xr = xm
    lmin = hypot(abs(G-H),W)
    print(lmin, L(xl))
