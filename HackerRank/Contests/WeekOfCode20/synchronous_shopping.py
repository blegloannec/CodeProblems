#!/usr/bin/env python

import sys
from heapq import *

def dijkstra():
    H = [(0,0,T[0])]
    D = [[float('inf') for j in xrange(1<<K)] for i in xrange(N)]
    D[0][T[0]] = 0
    while H:
        d,u,p = heappop(H)
        if d>D[u][p]:
            continue
        for v,w in G[u]:
            q = p|T[v]
            nd = d+w
            if nd<D[v][q]:
                D[v][q] = nd
                heappush(H,(nd,v,q))
    return D

def main():
    global N,T,G,K
    N,M,K = map(int,sys.stdin.readline().split())
    T = [0 for _ in xrange(N)]
    for i in xrange(N):
        t = map(int,sys.stdin.readline().split())
        for j in xrange(1,len(t)):
            T[i] |= 1<<(t[j]-1)
    G = [[] for _ in xrange(N)]
    for _ in xrange(M):
        x,y,z = map(int,sys.stdin.readline().split())
        G[x-1].append((y-1,z))
        G[y-1].append((x-1,z))
    D = dijkstra()
    m = float('inf')
    full = (1<<K)-1
    for p1 in xrange(full+1):
        for p2 in xrange(p1,full+1):
            if p1|p2==full:
                m = min(m,max(D[N-1][p1],D[N-1][p2]))
    print m

main()
