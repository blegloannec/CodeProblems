#!/usr/bin/env python3

import sys
import rosalib
from bisect import bisect_left

W = sorted((rosalib.W[a],a) for a in rosalib.W)
P = list(map(float,sys.stdin.readlines()))
sol = []
for i in range(1,len(P)):
    w = P[i]-P[i-1]
    a = bisect_left(W,(w,'Z'))
    if a==len(W) or (a>0 and W[a][0]-w>w-W[a-1][0]):
        a -= 1
    sol.append(W[a][1])
print(''.join(sol))
