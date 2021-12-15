#!/usr/bin/env python3

import sys
from heapq import *

INF = 1<<30

def dijkstra(Map, i0,j0, i1,j1):
    S = len(Map)
    Dist = [[INF]*S for _ in range(S)]
    Dist[i0][j0] = 0
    Q = [(0,i0,j0)]
    while Q:
        d,i,j = heappop(Q)
        if i==i1 and j==j1:
            break
        if d>Dist[i][j]:
            continue
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<S and 0<=vj<S and Dist[i][j]+Map[vi][vj]<Dist[vi][vj]:
                Dist[vi][vj] = Dist[i][j]+Map[vi][vj]
                heappush(Q, (Dist[vi][vj],vi,vj))
    return Dist[i1][j1]

def main():
    # Part 1
    Map = [list(map(int, L.strip())) for L in sys.stdin.readlines()]
    S = len(Map)
    print(dijkstra(Map, 0,0, S-1,S-1))
    # Part 2
    S5 = 5*S
    Map5 = [[(Map[i%S][j%S]+i//S+j//S-1)%9+1 for j in range(S5)] for i in range(S5)]
    print(dijkstra(Map5, 0,0, S5-1,S5-1))

main()
