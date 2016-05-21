#!/usr/bin/env python

import sys

T = []
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
    global T
    N,M = map(int,sys.stdin.readline().split())
    T = [-1 for _ in xrange(N)]
    V = []
    for _ in xrange(M):
        u,v,w = map(int,sys.stdin.readline().split())
        V.append((w,u-1,v-1))
    V.sort()
    print kruskal(V)

main()
