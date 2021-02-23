#!/usr/bin/env python3

from collections import deque

S = 8
V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))

def bfs(i0,j0):
    Dist = [[-1]*S for _ in range(S)]
    Dist[i0][j0] = 0
    Q = deque([(i0,j0)])
    while Q:
        i,j = Q.popleft()
        for di,dj in V:
            vi,vj = i+di,j+dj
            if 0<=vi<S and 0<=vj<S and Dist[vi][vj]<0:
                Dist[vi][vj] = Dist[i][j] + 1
                Q.append((vi,vj))
    return Dist

def main():
    N = int(input())
    for _ in range(N):
        p = input()
        i = ord(p[0])-ord('a')
        j = ord(p[1])-ord('1')
        Dist = bfs(i,j)
        dmax = max(max(L) for L in Dist)
        Sol = []
        for j in range(S-1, -1, -1):
            for i in range(S):
                if Dist[i][j] == dmax:
                    Sol.append(chr(i+ord('a')) + chr(j+ord('1')))
        print(dmax, *Sol)

main()
