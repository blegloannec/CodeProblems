#!/usr/bin/env python

import sys

def find(x):
    if T[x]<0:
        return x
    x0 = find(T[x])
    T[x] = x0
    return x0

def union(x,y):
    x0 = find(x)
    y0 = find(y)
    T[y0] = x0
    
def tarjan(E):
    G = [[] for _ in xrange(N)]
    for (c,u,v) in E:
        if find(u)!=find(v):
            union(u,v)
            G[u].append((v,c))
            G[v].append((u,c))
    return G

def dfs(G,u,v,c0):
    nv = 1
    s = 0
    for (w,c) in G[v]:
        if w!=u:
             nw,sw = dfs(G,v,w,c)
             nv += nw
             s += sw
    s += (1<<c0)*nv*(N-nv)
    return nv,s

def main():
    global N,T
    N,M = map(int,sys.stdin.readline().split())
    E = []
    for _ in xrange(M):
        A,B,C = map(int,sys.stdin.readline().split())
        E.append((C,A-1,B-1))
    E.sort()
    T = [-1 for _ in xrange(N)]
    print bin(dfs(tarjan(E),None,0,0)[1])[2:]

main()
