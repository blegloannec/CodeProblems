#!/usr/bin/env python3

# similar (and partially recycled from) GCJ 17.1B.C.Pony_Express.py

from collections import deque
from heapq import *

INF = float('inf')

def floyd_warshall(weight):
    for k in range(len(weight)):
        for u in range(len(weight)):
            for v in range(len(weight)):
                weight[u][v] = min(weight[u][v],weight[u][k]+weight[k][v])

def dEsopoPape(G, u0, uf):
    N = len(G)
    Dist = [None]*N
    Dist[u0] = 0
    Q = deque([u0])
    inQ = [False]*N
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v,w in G[u]:
            if Dist[v] is None:
                Dist[v] = Dist[u]+w
                Q.append(v)
                inQ[v] = True
            elif Dist[u]+w<Dist[v]:
                Dist[v] = Dist[u]+w
                if not inQ[v]:
                    Q.appendleft(v)
                    inQ[v] = True
    return Dist[uf]

def dijkstra(G, u0, uf):
    N = len(G)
    Dist = [INF]*N
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
    N,M,T,D = map(int,input().split())
    Stations = [0] + [int(u)-1 for u in input().split()] + [N-1]
    T += 2
    Weight = [[INF]*N for _ in range(N)]
    for _ in range(M):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        Weight[u][v] = Weight[v][u] = w
    floyd_warshall(Weight)
    G = [[]*T for _ in range(T)]
    for i,u in enumerate(Stations):
        for j,v in enumerate(Stations):
            if Weight[u][v]<=D:
                G[i].append((j,Weight[u][v]))
    #d = dEsopoPape(G, 0, T-1)
    #print('stuck' if d is None else d)
    d = dijkstra(G, 0, T-1)
    print(d if d<INF else 'stuck')

main()
