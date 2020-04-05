#!/usr/bin/env python3

# The markov chain is irreducible yet might not be aperiodic
# (for instance, the example is bipartite of period 2), hence
# might not converge towards the stable distribution.
# Yet it is well known (and easily checkable) for random walks
# on graphs that it is given by:
#   P(u) = degree(u) / sum of all degrees

from heapq import *

INF = float('inf')

def dijkstra(x0,y0, xf,yf):
    Dist = [[INF]*W for _ in range(H)]
    Dist[x0][y0] = 0
    Q = [(0,x0,y0)]
    while Q:
        d,x,y = heappop(Q)
        if x==xf and y==yf:
            break
        if d>Dist[x][y]:
            continue
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and Grid[vx][vy] in 'E D' and d+Weight[vx][vy]<Dist[vx][vy]:
                Dist[vx][vy] = d + Weight[vx][vy]
                heappush(Q, (Dist[vx][vy],vx,vy))
    return Dist[xf][yf]

def main():
    global H, W, Grid, Weight
    H,W = map(int,input().split())
    Grid = [input() for _ in range(H)]
    Weight = [[0]*W for _ in range(H)]  # degree of free cells
    for x in range(H):
        for y in range(W):
            if Grid[x][y]==' ':
                Weight[x][y] = (Grid[x-1][y],Grid[x+1][y],Grid[x][y-1],Grid[x][y+1]).count(' ')
            elif Grid[x][y]=='E':
                xe,ye = x,y
            elif Grid[x][y]=='D':
                xd,yd = x,y
    SumDeg = sum(sum(L) for L in Weight)
    Pmin = dijkstra(xe,ye, xd,yd) / SumDeg
    print(Pmin)

main()
