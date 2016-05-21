#!/usr/bin/env python

import sys

N = 40
T = [-1 for _ in xrange(N)]

def find(x):
    if T[x]<0:
        return x
    x0 = find(T[x])
    T[x] = x0
    return x0

def union(x,y):
    x0,y0 = find(x),find(y)
    T[y0] = x0

def kruskal(V):
    # V is assumed sorted
    #mst = []
    W = 0
    for (w,u,v) in V:
        if find(u)!=find(v):
            #mst.append((u,v))
            W += w
            union(u,v)
    return W

def main():
    V = []
    W = 0
    for u in xrange(N):
        L = sys.stdin.readline().strip().split(',')
        for v in xrange(N):
            if v>u and L[v]!='-':
                w = int(L[v])
                W += w
                V.append((w,u,v))
    V.sort()
    print W-kruskal(V)

main()
