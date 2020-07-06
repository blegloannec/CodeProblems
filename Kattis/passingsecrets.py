#!/usr/bin/env python3

from heapq import *
import sys
input = sys.stdin.readline

INF = float('inf')

def dijkstra(G, u0, uf):
    Dist = [INF]*len(G)
    Dist[u0] = 0
    Pred = [None]*len(G)
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
                Pred[v] = u
                heappush(Q, (Dist[v],v))
    return Dist[uf], Pred

def main():
    while True:
        try:
            name0, namef = input().split()
        except ValueError:
            break
        N = 2
        Name = [name0, namef]
        Idx = {name0: 0, namef: 1}
        Graph = [[],[]]
        G = int(input())
        for _ in range(G):
            group = []
            for name in input().split():
                if name not in Idx:
                    Name.append(name)
                    Idx[name] = N
                    N += 1
                    Graph.append([])
                group.append(Idx[name])
            w = len(group)-1
            for u in group:
                for v in group:
                    if u!=v:
                        Graph[u].append((v,w))
        d, Pred = dijkstra(Graph, 0, 1)
        if d==INF:
            sys.stdout.write('impossible\n')
        else:
            Path = []
            u = 1
            while u!=0:
                Path.append(Name[u])
                u = Pred[u]
            Path.append(Name[0])
            sys.stdout.write(f'{d-1} {" ".join(reversed(Path))}\n')

main()
