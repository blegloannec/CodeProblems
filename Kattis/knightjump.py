#!/usr/bin/env python3

from collections import deque

V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))

def bfs(i0,j0, i1=0,j1=0):
    Dist = {(i0,j0): 0}
    Q = deque([(i0,j0)])
    while Q:
        i,j = Q.popleft()
        if (i,j)==(i1,j1):
            return Dist[i,j]
        for di,dj in V:
            vi,vj = i+di,j+dj
            if 0<=vi<N and 0<=vj<N and G[vi][vj]=='.':
                if (vi,vj) not in Dist:
                    Dist[vi,vj] = Dist[i,j] + 1
                    Q.append((vi,vj))
    return -1

def main():
    global N,G
    N = int(input())
    G = [input() for _ in range(N)]
    i0,j0 = next((i,j) for i in range(N) for j in range(N) if G[i][j]=='K')
    print(bfs(i0,j0))

main()
