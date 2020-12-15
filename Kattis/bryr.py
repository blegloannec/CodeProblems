#!/usr/bin/env python3

import sys
from collections import deque
input = sys.stdin.readline

def bfs01(G, u0, uf):
    Dist = [float('inf')]*len(G)
    Dist[u0] = 0
    Seen = [False]*len(G)
    Q = deque([u0])
    while Q:
        u = Q.popleft()
        if u==uf:
            break
        if Seen[u]:
            continue
        Seen[u] = True
        for v,w in G[u]:
            dv = Dist[u]+w
            if dv < Dist[v]:
                Dist[v]= dv
                if w==0: Q.appendleft(v)
                else:    Q.append(v)
    return Dist[uf]

def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int, input().split())
        a -= 1; b -= 1
        G[a].append((b,c))
        G[b].append((a,c))
    print(bfs01(G, 0, N-1))

main()
