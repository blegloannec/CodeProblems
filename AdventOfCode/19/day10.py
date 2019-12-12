#!/usr/bin/env python3

import sys
from math import atan2, pi

I = [L.strip() for L in sys.stdin.readlines()]
H,W = len(I),len(I[0])
A = [(j,i) for i in range(H) for j in range(W) if I[i][j]=='#']

PREC = 9
def angle(x,y):
    a = -atan2(-y,x)  # /!\ clockwise & inverse y
    if a<0:
        a += 2.*pi
    a -= 3.*pi/2.     # 0 is up
    if a<0:
        a += 2.*pi
    return round(a,PREC)

dist2 = lambda x,y: x*x+y*y


# Part 1
smax = 0
for x,y in A:
    s = len(set(angle(ya-y,xa-x) for xa,ya in A if (xa,ya)!=(x,y)))
    if s>smax:
        smax = s
        x0,y0 = x,y
print(smax)


# Part 2
X = sorted((angle(xa-x0,ya-y0), dist2(xa-x0,ya-y0), (xa,ya)) for xa,ya in A if (xa,ya)!=(x0,y0))
X = [p for i,(a,_,p) in enumerate(X) if i==0 or a!=X[i-1][0]]  # first rot.
assert len(X)>=200  # 200th is in the first rotation
xa,ya = X[199]      # 200th
print(100*xa+ya)
