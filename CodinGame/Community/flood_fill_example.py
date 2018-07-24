#!/usr/bin/env python3

from collections import deque

INF = float('inf')

def bfs(i0,j0):
    Q = deque([(i0,j0)])
    Dist0 = [[INF]*W for _ in range(H)]
    Dist0[i0][j0] = 0
    while Q:
        i,j = Q.popleft()
        if Dist0[i][j]<Dist[i][j]:
            Dist[i][j] = Dist0[i][j]
            G[i][j] = G0[i0][j0]
        elif Dist0[i][j]==Dist[i][j]:
            G[i][j] = '+'
        for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=vi<H and 0<=vj<W and G0[vi][vj]=='.' and Dist0[vi][vj]==INF:
                Dist0[vi][vj] = Dist0[i][j]+1
                Q.append((vi,vj))

def main():
    global W,H,G0,G,Dist
    W = int(input())
    H = int(input())
    G0 = [input() for _ in range(H)]
    G = [list(L0) for L0 in G0]
    Dist = [[INF]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if G0[i][j] not in ['.','#']:
                bfs(i,j)
    for L in G:
        print(''.join(L))

main()
