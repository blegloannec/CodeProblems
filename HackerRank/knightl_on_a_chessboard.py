#!/usr/bin/env python3

from collections import deque

def bfs(a,b):
    Dist = [[-1]*N for _ in range(N)]
    Dist[0][0] = 0
    Q = deque([(0,0)])
    while Q:
        x,y = Q.popleft()
        if x==y==N-1:
            break
        for vx,vy in ((x-a,y-b),(x-a,y+b),(x+a,y-b),(x+a,y+b),\
                      (x-b,y-a),(x-b,y+a),(x+b,y-a),(x+b,y+a)):
            if 0<=vx<N and 0<=vy<N and Dist[vx][vy]<0:
                Dist[vx][vy] = Dist[x][y] + 1
                Q.append((vx,vy))
    return Dist[N-1][N-1]

def main():
    global N
    N = int(input())
    for a in range(1,N):
        print(*(bfs(a,b) for b in range(1,N)))

main()
