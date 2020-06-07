#!/usr/bin/env python3

# Looks like an hard problem at first (~ Kattis/shovelling),
# but actually groups can only split at S and A positions,
# so that's a simple MST in the S&A graph.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(H,W, G, u0):
    Dist = [[None]*W for _ in range(H)]
    i0,j0 = u0
    Dist[i0][j0] = 0
    Q = deque([u0])
    while Q:
        i,j = u = Q.popleft()
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if G[vi][vj]!='#' and Dist[vi][vj] is None:
                Dist[vi][vj] = Dist[i][j] + 1
                Q.append((vi,vj))
    return Dist

def find(T, x):
    if T[x] is None:
        return x
    T[x] = find(T, T[x])
    return T[x]

def union(T, x, y):
    x0 = find(T, x)
    y0 = find(T, y)
    if x0==y0:
        return False
    T[y0] = x0
    return True

def kruskal(N, E):
    E.sort()
    T = [None]*N
    mst = 0
    for d,u,v in E:
        if union(T, u, v):
            mst += d
            N -= 1
            if N==1:
                break
    return mst

def main():
    T = int(input())
    for _ in range(T):
        W,H = map(int, input().split())
        G = [input() for _ in range(H)]
        A = []
        for i in range(H):
            for j in range(W):
                if G[i][j]=='A':
                    A.append((i,j))
                elif G[i][j]=='S':
                    A = [(i,j)] + A
        N = len(A)
        E = []
        for u,a in enumerate(A):
            Da = bfs(H,W, G, a)
            for v in range(u+1, N):
                i,j = A[v]
                E.append((Da[i][j], u,v))
        print(kruskal(N, E))

main()
