#!/usr/bin/env python3

import sys
from collections import defaultdict

DNAS = [L.strip() for L in sys.stdin.readlines()]
N = len(DNAS)
K = len(DNAS[0])-1

# renumerotation comptant les multiplicites
UDNAS = []  # DNAs uniques
Mult = []   # multiplicites
Num = defaultdict(int)
for i in range(N):
    if DNAS[i] not in Num:
        Num[DNAS[i]] = len(UDNAS)
        UDNAS.append(DNAS[i])
        Mult.append(1)
    else:
        Mult[Num[DNAS[i]]] += 1
M = len(Mult)

# construction du graphe
G = defaultdict(list)
for E in Num:
    G[E[:-1]].append(Num[E])

# backtracking cycles
e0 = 0  # starting edge
u0,u1 = DNAS[e0][:-1],DNAS[e0][1:]
seen = [0]*M
seen[Num[DNAS[e0]]] = 1
sol = [DNAS[e0]]
def cycles(u=u1):
    if u==u0 and len(sol)==N:
        yield ''.join(sol[:-K])
    else:
        for e in G[u]:
            if seen[e]<Mult[e]:
                seen[e] += 1
                v = UDNAS[e][1:]
                sol.append(v[-1])
                yield from cycles(v)
                sol.pop()
                seen[e] -= 1

for C in cycles():
    print(C)
