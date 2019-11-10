#!/usr/bin/env python3

import sys
from collections import deque

INF = float('inf')

def bfs(G, u0, u1):
    Q = deque([u0])
    Dist = [INF]*len(G)
    Dist[u0] = 0
    while Q:
        u = Q.popleft()
        if u==u1:
            break
        for v in G[u]:
            if Dist[v]==INF:
                Dist[v] = Dist[u]+1
                Q.append(v)
    return Dist[u1]

def main():
    E,F = map(int,sys.stdin.readline().split())
    H,W = map(int,sys.stdin.readline().split())
    G = [sys.stdin.readline() for _ in range(H)]
    Cells = []
    for i in range(H):
        for j in range(W):
            if G[i][j]!='B':
                if G[i][j]=='S':
                    u0 = len(Cells)
                elif G[i][j]=='G':
                    u1 = len(Cells)
                Cells.append((i,j))
    N = len(Cells)
    # we are guaranteed that N <= 1000, we build both graphs in O(N^2)
    # build E graph
    Ge = [[] for _ in range(N)]
    e_reach = lambda x1,y1: lambda x2,y2: (x2-x1)**2+(y2-y1)**2<=E**2
    for i in range(N):
        can_reach = e_reach(*Cells[i])
        for j in range(i+1,N):
            if can_reach(*Cells[j]):
                Ge[i].append(j)
                Ge[j].append(i)
    de = bfs(Ge,u0,u1)
    # build F graph
    Gf = [[] for _ in range(N)]
    f_reach = lambda x1,y1: lambda x2,y2: (x1==x2 and abs(y2-y1)<=F) or (y1==y2 and abs(x2-x1)<=F)
    for i in range(N):
        can_reach = f_reach(*Cells[i])
        for j in range(i+1,N):
            if can_reach(*Cells[j]):
                Gf[i].append(j)
                Gf[j].append(i)
    df = bfs(Gf,u0,u1)
    # result
    if de==df:
        print('SUCCESS' if de!=INF else 'NO WAY')
    else:
        print('GO FOR IT' if de<df else 'NO CHANCE')

main()
