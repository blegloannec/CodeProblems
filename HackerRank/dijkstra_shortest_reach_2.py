#!/usr/bin/env python

import sys
from heapq import *

INF = float('inf')

def dijkstra(N,G,S):
    H = [(0,S)]
    D = [INF for _ in xrange(N)]
    D[S] = 0
    while H:
        d,u = heappop(H)
        if d>D[u]:
            continue
        for v,w in G[u]:
            nd = d+w
            if nd<D[v]:
                D[v] = nd
                heappush(H,(nd,v))
    return D

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N,M = map(int,sys.stdin.readline().split())
        G = [[] for _ in xrange(N)]
        for _ in xrange(M):
            x,y,z = map(int,sys.stdin.readline().split())
            G[x-1].append((y-1,z))
            G[y-1].append((x-1,z))
        S = int(sys.stdin.readline())-1
        D = dijkstra(N,G,S)
        res = []
        for u in xrange(N):
            if u!=S:
                if D[u]==INF:
                    res.append('-1')
                else:
                    res.append(str(D[u]))
        print ' '.join(res)

main()
