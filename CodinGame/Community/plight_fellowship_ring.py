#!/usr/bin/env python3

from math import sqrt,ceil
from collections import deque

INF = float('inf')  # +oo

def dist(A,B):
    return sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

def bfs(s,e):
    D = [None]*N  # dist
    P = [None]*N  # pred
    D[s] = 0
    Q = deque([s])
    while Q:
        u = Q.popleft()
        if u==e:
            break
        for v in G[u]:
            if D[v]==None and D[u]+1<T[v]:
                D[v] = D[u]+1
                P[v] = u
                Q.append(v)
    if P[e]==None:
        return None
    Path = []
    while e!=s:
        Path.append(e)
        e = P[e]
    Path.append(s)
    return Path[::-1]

def main():
    global N,G,T
    N = int(input())
    M = int(input())
    L = int(input())
    S = [tuple(map(int,input().split())) for _ in range(N)]
    O = [tuple(map(int,input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for _ in range(L):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    s = int(input())
    e = int(input())
    
    # limit time for each spot
    T = [INF]*N
    for i in range(N):
        for o in range(M):
            T[i] = min(T[i],ceil(dist(S[i],O[o])))
    
    P = bfs(s,e)
    if P:
        print(*P)
    else:
        print('IMPOSSIBLE')

main()
