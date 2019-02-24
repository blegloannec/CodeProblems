#!/usr/bin/env python3

from collections import deque

def bfs(x0,y0,xf,yf):
    Q = deque([(x0,y0)])
    Dist = {(x0,y0):0}
    while Q:
        x,y = Q.popleft()
        if (x,y)==(xf,yf):
            break
        for c,v in [(1,(x+1,y)),(2,(x,y-1)),(4,(x-1,y)),(8,(x,y+1))]:
            if G[x][y]&c==0 and v not in Dist:
                Dist[v] = Dist[x,y] + 1
                Q.append(v)
    return Dist[xf,yf]

if __name__=='__main__':
    ys,xs = map(int,input().split())
    yr,xr = map(int,input().split())
    w,h = map(int,input().split())
    G = [[int(c,16) for c in input()] for _ in range(h)]
    print(bfs(xs,ys,xr,yr),bfs(xr,yr,xs,ys))
