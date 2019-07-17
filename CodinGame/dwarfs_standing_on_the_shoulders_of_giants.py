#!/usr/bin/env python3

from collections import defaultdict

G = defaultdict(list)
n = int(input())  # the number of relationships of influence
for _ in range(n):
    # x: a relationship of influence between two people (x influences y)
    x,y = map(int,input().split())
    G[x].append(y)

D = {}
def depth(u):
    if u not in D:
        D[u] = 1
        if u in G:
            D[u] += max(depth(v) for v in G[u])
    return D[u]

# The number of people involved in the longest succession of influences
print(max(depth(u) for u in G))
