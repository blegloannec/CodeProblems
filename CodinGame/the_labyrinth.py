#!/usr/bin/env python3

from collections import deque
import random
random.seed(42)

INF = float('inf')

def randpos():
    i,j = random.randint(0,H-1),random.randint(0,W-1)
    while G[i][j]!='?':
        i,j = random.randint(0,H-1),random.randint(0,W-1)
    return i,j

def find(c):
    for i in range(H):
        for j in range(W):
            if G[i][j]==c:
                return i,j
    return None

def BFS(i0,j0):
    Dist = [[INF]*W for _ in range(H)]
    Dist[i0][j0] = 0
    Q = deque([(i0,j0)])
    while Q:
        i,j = Q.popleft()
        for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=vi<H and 0<=vj<W and G[vi][vj]!='#' and Dist[i][j]+1<Dist[vi][vj]:
                Dist[vi][vj] = Dist[i][j]+1
                Q.append((vi,vj))
    return Dist

def main():
    global H,W,G
    H,W,A = map(int,input().split())
    step = 0
    ti = tj = None  # target
    while True:
        i,j = map(int,input().split())
        G = [input() for _ in range(H)]
        if step==0:  # looking for unidentified C
            C = find('C')
            if C is not None:
                ti,tj = C
                step = 1
            elif ti is None or (i,j)==(ti,tj) or G[ti][tj]=='#':
                ti,tj = randpos()
        if step==1:  # moving to located C
            if (i,j)==(ti,tj):  # back to T
                ti,tj = find('T')
                step = 2
        Dist = BFS(ti,tj)
        dmin = INF
        for vi,vj,D in [(i-1,j,'UP'),(i+1,j,'DOWN'),(i,j-1,'LEFT'),(i,j+1,'RIGHT')]:
            if 0<=vi<H and 0<=vj<W and Dist[vi][vj]<dmin:
                dmin = Dist[vi][vj]
                Dmin = D
        print(Dmin)

main()
