#!/usr/bin/env python3

import sys
from collections import deque

G = [L.rstrip('\n') for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])


# Part 1
def bfs():
    u0 = (x0,y0)
    u1 = (x1,y1)
    Dist = {u0: 0}
    Q = deque([u0])
    while Q:
        x,y = u = Q.popleft()
        if u==u1:
            return Dist[u]
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and \
               (G[vx][vy]=='.' or ('A'<=G[vx][vy]<='Z' and (vx,vy) in Portal)):
                if 'A'<=G[vx][vy]<='Z':
                    vx,vy,_ = Portal[vx,vy]
                v = (vx,vy)
                if v not in Dist:
                    Dist[v] = Dist[u] + 1
                    Q.append(v)

Seen = set()
Label = {}
Portal = {}
for i in range(H):
    for j in range(W):
        if 'A'<=G[i][j]<='Z' and (i,j) not in Seen:
            Seen.add((i,j))
            if 'A'<=G[i+1][j]<='Z':
                Seen.add((i+1,j))
                l = G[i][j] + G[i+1][j]
                if i+2<H and G[i+2][j]=='.':
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        out = 1 if i==0 else -1
                        Portal[i+1,j] = (ii2,jj2,-out)
                        Portal[i2,j2] = (i+2,j,out)
                    else:
                        Label[l] = ((i+1,j),(i+2,j))
                else:
                    assert G[i-1][j]=='.'
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        out = 1 if i==H-2 else -1
                        Portal[i,j] = (ii2,jj2,-out)
                        Portal[i2,j2] = (i-1,j,out)
                    else:
                        Label[l] = ((i,j),(i-1,j))
            else:
                assert 'A'<=G[i][j+1]<='Z'
                Seen.add((i,j+1))
                l = G[i][j] + G[i][j+1]
                if j+2<W and G[i][j+2]=='.':
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        out = 1 if j==0 else -1
                        Portal[i,j+1] = (ii2,jj2,-out)
                        Portal[i2,j2] = (i,j+2,out)
                    else:
                        Label[l] = ((i,j+1),(i,j+2))
                else:
                    assert G[i][j-1]=='.'
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        out = 1 if j==W-2 else -1
                        Portal[i,j] = (ii2,jj2,-out)
                        Portal[i2,j2] = (i,j-1,out)
                    else:
                        Label[l] = ((i,j),(i,j-1))

x0,y0 = Label['AA'][1]
x1,y1 = Label['ZZ'][1]
print(bfs())


# Part 2
def bfs2():
    u0 = (x0,y0,0)
    u1 = (x1,y1,0)
    Dist = {u0: 0}
    Q = deque([u0])
    while Q:
        x,y,k = u = Q.popleft()
        if u==u1:
            return Dist[u]
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and \
               (G[vx][vy]=='.' or ('A'<=G[vx][vy]<='Z' and (vx,vy) in Portal)):
                vk = k
                if 'A'<=G[vx][vy]<='Z':
                    vx,vy,dk = Portal[vx,vy]
                    vk += dk
                if vk>=0:
                    v = (vx,vy,vk)
                    if v not in Dist:
                        Dist[v] = Dist[u] + 1
                        Q.append(v)

print(bfs2())
