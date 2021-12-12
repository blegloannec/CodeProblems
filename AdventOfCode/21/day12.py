#!/usr/bin/env python3

import sys


# Parsing input and building graph
Idx = {}
Graph = []
Small = []
for L in sys.stdin.readlines():
    u,v = L.strip().split('-')
    for w in (u,v):
        if w not in Idx:
            Idx[w] = len(Graph)
            Graph.append([])
            Small.append(w.islower())
    for a,b in ((u,v),(v,u)):
        if a!='end' and b!='start':
            Graph[Idx[a]].append(Idx[b])
U0 = Idx['start']
Uf = Idx['end']


# DFS with backtracking to count all paths
def dfs(u, Used, twice=False):
    if u==Uf:
        return 1
    if Small[u]:
        if Used[u]==1 and twice:
            twice = False
        elif Used[u]>=1:
            return 0
    res = 0
    Used[u] += 1
    for v in Graph[u]:
        res += dfs(v, Used, twice)
    Used[u] -= 1
    return res

print(dfs(U0, [0]*len(Graph)))        # Part 1
print(dfs(U0, [0]*len(Graph), True))  # Part 2
