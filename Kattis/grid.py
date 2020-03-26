#!/usr/bin/env python3

from collections import deque

def bfs(i0,j0, i1,j1):
    D = [[-1]*W for _ in range(H)]
    Q = deque([(i0,j0)])
    D[i0][j0] = 0
    while Q:
        i,j = Q.popleft()
        if (i,j)==(i1,j1):
            break
        d = G[i][j]
        for vi,vj in ((i-d,j),(i+d,j),(i,j-d),(i,j+d)):
            if 0<=vi<H and 0<=vj<W and D[vi][vj]<0:
                D[vi][vj] = D[i][j]+1
                Q.append((vi,vj))
    return D[i1][j1]

def main():
    global H,W,G
    H,W = map(int,input().split())
    G = [list(map(int,input())) for _ in range(H)]
    print(bfs(0,0, H-1,W-1))

main()
