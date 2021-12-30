#!/usr/bin/env python3

from math import sqrt
from heapq import *
import sys
input = sys.stdin.readline

def dist(i,j):
    xi,yi,ri = C[i]; xj,yj,rj = C[j]
    dx = xi-xj; dy = yi-yj
    return sqrt(dx*dx+dy*dy)-ri-rj

def prim(u0=0):
    mst = 0.
    Seen = [False]*N
    Dist = [float('inf')]*N
    Dist[u0] = 0.
    Q = [(0.,u0)]
    while Q:
        d,u = heappop(Q)
        if Seen[u]:
            continue
        Seen[u] = True
        mst += d
        for v in range(N):
            if not Seen[v]:
                d = dist(u,v)
                if d<Dist[v]:
                    Dist[v] = d
                    heappush(Q, (d,v))
    return mst

def main():
    global N,C
    N = int(input())
    C = [tuple(map(int, input().split())) for _ in range(N)]
    print(prim())

main()
