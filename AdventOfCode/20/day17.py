#!/usr/bin/env python3

# Game of Life in 3D and 4D, 2nd CA pb after the 2D CA of day 11

import sys
from itertools import product

I = [L.strip() for L in sys.stdin.readlines()]
H = len(I)
W = len(I[0])

Init = []
for i,L in enumerate(I):
    for j,c in enumerate(L):
        if c=='#':
            Init.append((i,j))


# Part 1 - 3D
def part1(T=6):
    C = {(i,j,0) for i,j in Init}
    for t in range(1,T+1):
        C0 = C.copy()
        for u in product(range(-t,H+t), range(-t,W+t), range(-t,1+t)):
            i,j,k = u
            o = 0
            for v in product(range(i-1,i+2), range(j-1,j+2), range(k-1,k+2)):
                o += v in C0
            active = u in C0
            if not active and o==3:
                C.add(u)
            elif active and not 2<=o-1<=3:
                C.remove(u)
    return len(C)

print(part1())


# Part 2 is literally part 1 in 4D
# Faster sparse implementation here
def part2(T=6):
    C = {(i,j,0,0) for i,j in Init}
    for t in range(1,T+1):
        Vcnt = {}
        for u in C:
            i,j,k,l = u
            for v in product(range(i-1,i+2), range(j-1,j+2), range(k-1,k+2), range(l-1,l+2)):
                Vcnt[v] = Vcnt.get(v, 0) + 1
        for u,c in Vcnt.items():
            if u in C:
                if not 2<=c-1<=3:
                    C.remove(u)
            else:
                if c==3:
                    C.add(u)
    return len(C)

print(part2())
