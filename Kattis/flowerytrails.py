#!/usr/bin/env python3

from heapq import *
import sys
input = sys.stdin.readline

INF = float('inf')

def dijkstra_all_pred(u0, uf):
    Dist = [INF]*N
    Dist[u0] = 0
    Pred = [[] for _ in range(N)]  # lists of all optimal predecessors
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
                Pred[v] = [(u,w)]
                heappush(Q, (Dist[v],v))
            elif d+w==Dist[v]:
                Pred[v].append((u,w))
    return Pred

# sum of all edges belonging to a shortest path
def backward_paths(Pred, Seen, u):
    Seen[u] = True
    res = 0
    for v,w in Pred[u]:
        res += w
        if not Seen[v]:
            res += backward_paths(Pred, Seen, v)
    return res

def main():
    global N, G
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v,w = map(int, input().split())
        G[u].append((v,w))
        G[v].append((u,w))
    Pred = dijkstra_all_pred(0, N-1)
    print(2*backward_paths(Pred, [False]*N, N-1))

main()
