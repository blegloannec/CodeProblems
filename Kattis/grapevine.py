#!/usr/bin/env python3

import sys
from collections import deque

def spread(u0, D):
    Q = deque([(0,u0)])
    Count = [0]*N
    Count[u0] = 1
    while Q:
        d,u = Q.popleft()
        if d>=D:
            break
        for v in G[u]:
            Count[v] += 1
            if Count[v]==Thresh[v]:
                Q.append((d+1,v))
    return sum(min(c,1) for c in Count)-1

def main():
    global N, G, Thresh
    N, M, D = map(int, sys.stdin.readline().split())
    NameIdx = {}
    Thresh = []
    for i in range(N):
        name, t = sys.stdin.readline().split()
        NameIdx[name] = i
        Thresh.append(int(t))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(NameIdx.get, sys.stdin.readline().split())
        G[u].append(v)
        G[v].append(u)
    u0 = NameIdx[sys.stdin.readline().strip()]
    print(spread(u0, D))

main()
