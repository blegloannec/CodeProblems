#!/usr/bin/env pypy3

import sys, re


# Input
in_re = r'x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)\n'
I = []
for line in sys.stdin.readlines():
    o = line.startswith('on')
    x1,x2,y1,y2,z1,z2 = map(int, re.search(in_re, line).groups())
    I.append((o, x1,x2, y1,y2, z1,z2))


# Part 1 -- Naive approach
On = set()
for o,x1,x2,y1,y2,z1,z2 in I:
    for x in range(max(-50,x1), min(x2,50)+1):
        for y in range(max(-50,y1), min(y2,50)+1):
            for z in range(max(-50,z1), min(z2,50)+1):
                if o:
                    On.add((x,y,z))
                else:
                    On.discard((x,y,z))
print(len(On))


# Part 2 -- Coordinates compression (over x/y) & plane sweep (along z)
from heapq import *

X = set()
Y = set()
Z = []
for i,(_,x1,x2,y1,y2,z1,z2) in enumerate(I):
    X.update((x1,x2+1))
    Y.update((y1,y2+1))
    Z.extend(((z1,i),(z2+1,i)))  # z-event
X = sorted(X)
Y = sorted(Y)
Z.sort()

Xidx = {x:i for i,x in enumerate(X)}
Yidx = {y:i for i,y in enumerate(Y)}

XYheap = [[[] for _ in range(len(Y))] for _ in range(len(X))]
part2 = xyarea = z0 = 0
for z,i in Z:
    # update volume
    part2 += xyarea*(z-z0)
    z0 = z
    # update event
    o,x1,x2,y1,y2,z1,z2 = I[i]
    for x in range(Xidx[x1], Xidx[x2+1]):
        for y in range(Yidx[y1], Yidx[y2+1]):
            # cell (x,y) -> rectangle [X[x],X[x+1][ x [Y[y],Y[y+1][
            # because we have on/off operations to keep track of
            # (and not simply, for instance, a count of flips)
            # we maintain a heap of operations for each cell
            H = XYheap[x][y]
            s0 = len(H)>0 and H[0][2]     # current state
            if z==z1:                     # push new op.
                heappush(H, (-i, z2, o))
            else:                         # pop obsolete op.
                while H and H[0][1]<z:
                    heappop(H)
            s1 = len(H)>0 and H[0][2]     # new state
            if s0!=s1:                    # update area
                a = (X[x+1]-X[x])*(Y[y+1]-Y[y])
                xyarea += a if s1 else -a
print(part2)
