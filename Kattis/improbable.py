#!/usr/bin/env python3

# We can reorganize the crates as we want, except that the top view
# forbids to fill 0 cells or empty >0 cells. This is then equivalent
# to work on the "partial" grid of >0 cells & apply -1 to all values.
# Each row/col. has a target height and we need to use at least one
# cell to reach it. Minimizing the nb of forced cells is equivalent
# to maximizing the nb of cells shared between a row and a column
# that have the same target. We build a bipartite (rows, cols) graph
# using these candidate cells as edges and compute a max. bip. matching.

import sys
input = sys.stdin.readline

def aug(u,G,M,seen):
    for v in G[u]:
        if not seen[v]:
            seen[v] = True
            if M[v]==None or aug(M[v],G,M,seen):
                M[v] = u
                return True
    return False

def bip_match(G,Us,Vs):
    M = [None]*Vs
    for u in range(Us):
        aug(u,G,M,[False]*Vs)
    return M

def main():
    H,W = map(int, input().split())
    Grid = [list(map(int, input().split())) for _ in range(H)]
    Hmax = [max(L) for L in Grid]  # side
    Vmax = [max(Grid[i][j] for i in range(H)) for j in range(W)]  # front
    Graph = [[] for _ in range(H)]
    for i in range(H):
        if Hmax[i]>0:
            for j in range(W):
                if Grid[i][j]>0 and Hmax[i]==Vmax[j]:
                    Graph[i].append(j)
    M = bip_match(Graph, H, W)
    keep = sum(h-1 for h in Hmax if h>0) + sum(v-1 for v in Vmax if v>0)
    for j in range(W):
        if M[j] is not None:
            keep -= Vmax[j]-1
    avail = sum(x-1 for L in Grid for x in L if x>0)
    print(avail-keep)

main()
