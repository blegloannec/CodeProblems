#!/usr/bin/env python3

import sys
from math import log, exp
from heapq import *
input = sys.stdin.readline

def dijkstra(G, u0, uf):
    Dist = [float('inf')]*len(G)
    Dist[u0] = 0.
    Q = [(0., u0)]
    while Q:
        d,u = heappop(Q)
        if u==uf:
            break
        if d>Dist[u]:
            continue
        for v,w in G[u]:
            if d+w < Dist[v]:
                Dist[v] = d+w
                heappush(Q, (Dist[v], v))
    return Dist[uf]

def main():
    while True:
        N,M = map(int, input().split())
        if N==0:
            break
        G = [[] for _ in range(N)]
        for _ in range(M):
            u,v,f = input().split()
            u = int(u); v = int(v)
            w = -log(float(f))
            G[u].append((v,w))
            G[v].append((u,w))
        f = exp(-dijkstra(G, 0, N-1))
        sys.stdout.write(f'{f:.4f}\n')

main()
