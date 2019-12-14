#!/usr/bin/env python3

import sys
from collections import defaultdict


# ===== Part 1 =====
# Parsing input into a DAG and successors counters
Reac = {}
Succ = defaultdict(int)
for LR in sys.stdin.readlines():
    L,R = LR.strip().split(' => ')
    L = L.split(', ')
    E = []
    for ce in L:
        c,e = ce.split()
        E.append((int(c),e))
        Succ[e] += 1
    cr,er = R.split()
    Reac[er] = (int(cr),E)

# DP on the (reversed) reaction DAG (following a topological sort)
def ore_per_fuel(f=1):
    Cnt = Succ.copy()
    Req = defaultdict(int)
    Req['FUEL'] = f
    Q = ['FUEL']
    while Q:
        er = Q.pop()
        if er=='ORE':
            break
        cr,L = Reac[er]
        k = (Req[er]+cr-1)//cr
        for c,e in L:
            Req[e] += k*c
            Cnt[e] -= 1
            if Cnt[e]==0:
                Q.append(e)
    return Req['ORE']

print(ore_per_fuel())


# ===== Part 2 =====
def dicho(o=10**12):
    l, r = 0, 1<<60
    while l<r:
        m = (l+r+1)//2
        if ore_per_fuel(m)>o:
            r = m-1
        else:
            l = m
    return l

print(dicho())
