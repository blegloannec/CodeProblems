#!/usr/bin/env python

import sys
from heapq import *

M = []
Q = []
dist = []
visited = []

def voisins((x,y)):
    return filter((lambda (x,y): x>=0 and y>=0 and x<len(M) and y<len(M)),[(x-1,y),(x+1,y),(x,y-1),(x,y+1)])

def dijkstra(start,dest):
    dist[start[0]][start[1]] = M[start[0]][start[1]]
    heappush(Q,(dist[start[0]][start[1]],start))
    while Q!=[]:
        d,u = heappop(Q)
        if u==dest:
            return d
        if visited[u[0]][u[1]]:
            continue
        for v in voisins(u):
            if not visited[v[0]][v[1]]:
                nd = d+M[v[0]][v[1]]
                if nd<dist[v[0]][v[1]]:
                    dist[v[0]][v[1]] = nd
                    heappush(Q,(nd,v))
        visited[u[0]][u[1]] = True

def main():
    global N,M,dist,visited
    N = int(sys.stdin.readline())
    dist = [[1<<100 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        M.append(map(int,sys.stdin.readline().split()))
    print dijkstra((0,0),(N-1,N-1))

main()
