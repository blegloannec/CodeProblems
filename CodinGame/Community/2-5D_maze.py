#!/usr/bin/env python3

from collections import deque

def bfs():
    u0 = y0,x0,0
    uf = yf,xf,0
    Q = deque([u0])
    Dist = {u0: 0}
    while Q:
        u = y,x,z = Q.popleft()
        if u==uf:
            break
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            vy,vx = y+dy,x+dx
            v = vy,vx,z
            if 0<=vy<H and 0<=vx<W and G[vy][vx]!='#':
                if ((G[vy][vx]=='.' and z==0) or G[vy][vx]=='X' or (G[vy][vx]=='+' and z==1) or (G[vy][vx]=='O' and z==0)) and v not in Dist:
                    Dist[v] = Dist[u] + 1
                    Q.append(v)
                else:
                    v = y+2*dy,x+2*dx,1-z
                    if ((G[vy][vx]=='|' and dy!=0) or (G[vy][vx]=='-' and dx!=0)) and v not in Dist:
                        Dist[v] = Dist[u] + 2
                        Q.append(v)
    return Dist[uf]

if __name__=='__main__':
    y0,x0 = map(int,input().split())
    yf,xf = map(int,input().split())
    H,W = map(int,input().split())
    G = [input() for _ in range(H)]
    print(bfs())
