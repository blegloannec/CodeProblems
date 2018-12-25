#!/usr/bin/env python3

import sys
from itertools import product

I = [tuple(map(int,L.strip().split(','))) for L in sys.stdin.readlines()]

NEIGH = [D for D in product(range(-3,4),repeat=4) if sum(abs(x) for x in D)<=3]
def neigh(x,y,z,t):
    for dx,dy,dz,dt in NEIGH:
        yield (x+dx,y+dy,z+dz,t+dt)

def dfs_connected_components(Pts):
    C = 0
    Compo = {}
    Seen = set()
    SI = set(Pts)
    Q = Pts[:]
    while Q:
        u = Q.pop()
        if u in Seen:
            continue
        Seen.add(u)
        if u not in Compo:
            Compo[u] = C
            C += 1
        for v in neigh(*u):
            if v in SI and v not in Compo:
                Compo[v] = Compo[u]
                Q.append(v)
    return C,Compo

C,_ = dfs_connected_components(I)
print(C)
