#!/usr/bin/env python3

import sys
input = sys.stdin.readline

# Can we partition a directed graph into cycles?
# Equivalent to find a permutation of the vertices using arcs.
# Hence equivalent to a perfect matching in the bipartite graph
# representing (left end, right end) of arcs.

### max bipartite matching from tryalgo ###
def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph, visit, match):
                match[v] = u
                return True
    return False

def bip_match(bigraph, nU, nV):
    match = [None]*nV
    for u in range(nU):
        augment(u, bigraph, [False]*nV, match)
    return match
### ===== ###

def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int, input().split())
        G[u].append(v)
    match = bip_match(G, N, N)
    perm = None not in match
    print('YES' if perm else 'NO')

main()
