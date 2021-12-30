#!/usr/bin/env python3

# retake on the (former) Teads challenge
# computing the center of a tree in O(N) through a two-pass DP

import sys
sys.setrecursionlimit(2000)

def depth(u=0, u0=None):
    for v in T[u]:
        if v!=u0:
            D[u] = max(D[u], 1+depth(v,u))
    return D[u]

def maj(u=0, u0=None, p0=0):
    p,p2 = p0,0
    for v in T[u]:
        if v!=u0:
            dv = 1+D[v]
            if dv>p:
                p,p2 = dv,p
            elif dv>p2:
                p2 = dv
    P[u] = p
    for v in T[u]:
        if v!=u0:
            maj(v, u, 1+p2 if 1+D[v]==p else 1+p)

if __name__=='__main__':
    N = int(input())
    T = [[] for _ in range(N+1)]
    for _ in range(N):
        u,v = map(int,input().split())
        T[u].append(v)
        T[v].append(u)
    D = [0]*(N+1)
    depth()
    P = [0]*(N+1)
    maj()
    print(min(P))
