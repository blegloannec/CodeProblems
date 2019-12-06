#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000)
from collections import defaultdict

def dfs_sum_depth(u='COM', d=0):
    Depth[u] = d
    return d + sum(dfs_sum_depth(v,d+1) for v in Children[u])

Parent = {}
Children = defaultdict(list)
Depth = {}
for L in sys.stdin.readlines():
    A,B = L.strip().split(')')
    Parent[B] = A
    Children[A].append(B)
print(dfs_sum_depth())


# Part 2
u, v = Parent['YOU'], Parent['SAN']
if Depth[u]>Depth[v]:
    u,v = v,u
dist = 0
while Depth[u]!=Depth[v]:
    v = Parent[v]
    dist += 1
while u!=v:
    u, v = Parent[u], Parent[v]
    dist += 2    
print(dist)
