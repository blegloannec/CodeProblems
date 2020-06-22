#!/usr/bin/env python3

from math import *
from heapq import *
import sys
input = sys.stdin.readline

Diam = 2.*6381.

# https://en.wikipedia.org/wiki/Haversine_formula
def haversine(A, B):
    lat1,lon1 = A
    lat2,lon2 = B
    sindlat = sin((lat1-lat2)/2.)
    sindlon = sin((lon1-lon2)/2.)
    return Diam*asin(sqrt(sindlat*sindlat + cos(lat1)*cos(lat2)*sindlon*sindlon))

INF = float('inf')

def dijkstra(G, u0, uf):
    Dist = [INF]*len(G)
    Dist[u0] = 0
    Q = [(0,u0)]
    while Q:
        d,u = heappop(Q)
        if u==uf:
            break
        if Dist[u]<d:
            continue
        for v,w in G[u]:
            if d+w<Dist[v]:
                Dist[v] = d+w
                heappush(Q, (Dist[v],v))
    return Dist[uf]

def main():
    N,M = map(int, input().split())
    cod0,codf = input().split()
    Num = {}
    Pos = []
    for i in range(N):
        code,lat,lon = input().split()
        Num[code] = i
        Pos.append((radians(float(lat)), radians(float(lon))))
    G = [[] for _ in range(N)]
    for _ in range(M):
        codu,codv = input().split()
        u,v = Num[codu], Num[codv]
        d = haversine(Pos[u], Pos[v]) + 100.
        G[u].append((v, d))
        G[v].append((u, d))
    res = dijkstra(G, Num[cod0], Num[codf])
    print(res if res<INF else -1)

main()
