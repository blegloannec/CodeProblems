#!/usr/bin/env python3

from math import hypot

T = int(input())
for _ in range(T):
    W,G,H,R = map(int,input().split())
    G -= R
    H -= R
    L = lambda x: hypot(G,x) + hypot(W-x,H)
    lmin = hypot(G-H,W)
    lmax = lmin if H==G==0 else L(G*W/(G+H))
    print(lmin, lmax)
