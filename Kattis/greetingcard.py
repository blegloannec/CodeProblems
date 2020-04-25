#!/usr/bin/env python3

import sys

Pyth = ((0,2018),(1118,1680),(1118,-1680),(1680,1118),(1680,-1118),(2018,0))

N = int(sys.stdin.readline())
Pts = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
key = lambda x,y: (y<<32)|x
S = set(key(*p) for p in Pts)
res = 0
for x,y in Pts:
    for dx,dy in Pyth:
        if key(x+dx,y+dy) in S:
            res += 1
print(res)
