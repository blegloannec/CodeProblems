#!/usr/bin/env python3

import sys

I = sys.stdin.readlines()
N = len(I)
G = [[] for _ in range(N)]
for L in I:
    L = L.split(' <-> ')
    u = int(L[0])
    for v in L[1].split(','):
        G[u].append(int(v))

seen = [False]*N
def dfs(u):
    nb = 1
    seen[u] = True
    for v in G[u]:
        if not seen[v]:
            nb += dfs(v)
    return nb

# Part 1
print(dfs(0))

# Part 2
nb_compo = 1  # component of 0 already seen
for u in range(N):
    if not seen[u]:
        dfs(u)
        nb_compo += 1
print(nb_compo)
