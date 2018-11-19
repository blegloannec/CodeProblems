#!/usr/bin/env python3

from itertools import groupby

W,H = map(int,input().split())
Pic = [input() for _ in range(H)]
Hist = [next(i for i in range(H+1) if i==H or Pic[H-1-i][j]==' ') for j in range(W)]
hmax = max(Hist)
Res = []
for v,g in groupby(Hist,(lambda x: x!=0)):
    if v:
        h = list(g)
        if max(h)==hmax:
            Res.append('\n'.join(''.join('#' if h[j]>=i else ' ' for j in range(len(h))).rstrip() for i in range(hmax,0,-1)))
print('\n\n'.join(Res))
