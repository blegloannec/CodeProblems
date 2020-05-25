#!/usr/bin/env python3

import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

def ham(u,v):
    return sum(1 for a,b in zip(u,v) if a!=b)

def bfs(u0):
    Dist = [INF]*N
    Dist[u0] = 0
    Q = deque([u0])
    while Q:
        w = Q.popleft()
        for v in G[w]:
            if Dist[v]==INF:
                Dist[v] = Dist[w]+1
                Q.append(v)
    return Dist

def main():
    global N, G
    N = int(input())
    W = [input().strip() for _ in range(N)]
    # building graph
    D = [[0]*N for _ in range(N)]
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            dij = ham(W[i],W[j])
            D[i][j] = D[j][i] = dij
            if dij==1:
                G[i].append(j)
                G[j].append(i)
    # BFS
    u0, uf = 0, 1
    Dist0 = bfs(u0)
    Distf = bfs(uf)
    # looking for shortcut
    best_dist = Dist0[uf]
    best_word = '0'
    for i in range(N):
        if Dist0[i]<INF:
            for j in range(N):
                if D[i][j]==2 and Distf[j]<INF:
                    dij = Dist0[i] + 2 + Distf[j]
                    if dij<=best_dist:
                        p = next(k for k,(a,b) in enumerate(zip(W[i],W[j])) if a!=b)
                        word = min(''.join(a if k==p else b for k,(a,b) in enumerate(zip(W[i],W[j]))),
                                   ''.join(b if k==p else a for k,(a,b) in enumerate(zip(W[i],W[j]))))
                        if dij<best_dist or word<best_word:
                            best_dist = dij
                            best_word = word
    print(best_word)
    print(best_dist if best_dist<INF else -1)

main()
