#!/usr/bin/env python3

# V(t) = A/2 (cos(2pi/12 t) + 1)
# t = 6/pi arccos(2V/A-1)

from math import tau, acos, hypot
from heapq import *

INF = float('inf')
DH = 1000
DT = 3600.
TMAX = 12.*DT

def dijkstra(x0,y0):
    Time = [[INF]*W for _ in range(H)]
    Time[x0][y0] = 0.
    Q = [(0.,x0,y0)]
    while Q:
        t,x,y = heappop(Q)
        if t>Time[x][y]:
            continue
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and    \
               I[vx][vy] is not None and  \
               abs(G[x][y]-G[vx][vy])<=DH:
                t0 = max(t, I[vx][vy][0])
                if t0+M<=min(I[x][y][1], I[vx][vy][1]) and t0+M<Time[vx][vy]:
                    Time[vx][vy] = t0+M
                    heappush(Q, (Time[vx][vy],vx,vy))
    return Time

def dijkstra_reverse(x0,y0):
    Time = [[INF]*W for _ in range(H)]
    Time[x0][y0] = 0.
    Q = [(0.,x0,y0)]
    while Q:
        t,x,y = heappop(Q)
        assert I[x][y][0]<=TMAX-t<=I[x][y][1]
        if t>Time[x][y]:
            continue
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and    \
               I[vx][vy] is not None and  \
               abs(G[x][y]-G[vx][vy])<=DH:
                t0 = max(t, TMAX-I[vx][vy][1])
                if TMAX-(t0+M)>=max(I[x][y][0], I[vx][vy][0]) and t0+M<Time[vx][vy]:
                    Time[vx][vy] = t0+M
                    heappush(Q, (Time[vx][vy],vx,vy))
    return Time

def main():
    global M,W,H,G,I
    A,M = map(float,input().split())
    A *= 1000.
    W,H,Y,X = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(H)]
    # computing intervals where each cell is dry
    I = [[None]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if G[i][j]<=A:
                t = TMAX/tau*acos(2.*G[i][j]/A-1.)
                l, r = t+DT, TMAX-t
                if l<=r and r-l>=2.*M:
                    I[i][j] = (l,r)
            else:
                I[i][j] = (0.,TMAX)
    Time_in = dijkstra(X,Y)           # earliest time you can enter a cell
    Time_out = dijkstra_reverse(X,Y)  # latest time you can leave a cell
    dmax = 0.
    for i in range(H):
        for j in range(W):
            if Time_in[i][j]<INF and Time_out[i][j]<INF and \
               Time_in[i][j] <= TMAX-Time_out[i][j]:
                dmax = max(dmax, hypot(i-X,j-Y))
    print(10.*dmax)

main()
