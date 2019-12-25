#!/usr/bin/env python3

import sys, os
from collections import deque
from heapq import *
from PIL import Image, ImageDraw

G = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])

is_key  = lambda c: 'a'<=c<='z'
is_door = lambda c: 'A'<=c<='Z'
key     = lambda c: ord(c)-ord('a')
door    = lambda c: ord(c)-ord('A')

kfull = 0
key_cnt = 0
for i in range(H):
    for j in range(W):
        if is_key(G[i][j]):
            kfull |= 1<<key(G[i][j])
            key_cnt += 1
        elif G[i][j]=='@':
            x0,y0 = i,j
G[x0-1][y0] = '#'
G[x0][y0]   = '#'
G[x0+1][y0] = '#'
G[x0][y0-1] = '#'
G[x0][y0+1] = '#'

# key to key graph
def bfs_key_to_key(x0,y0):
    u0 = (x0,y0)
    DistReq = {u0: (0,0)}  # distance & mask of required keys
    Pred = {u0: None}
    Q = deque([u0])
    while Q:
        x,y = u = Q.popleft()
        d,k = DistReq[u]
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and G[vx][vy]!='#':
                kv = k
                if is_door(G[vx][vy]):
                    kv |= 1<<door(G[vx][vy])
                v = (vx,vy)
                if v not in DistReq:
                    DistReq[v] = (d+1,kv)
                    Pred[v] = u
                    Q.append(v)
    Neigh = [(key(G[x][y]),d,k) for (x,y),(d,k) in DistReq.items() if is_key(G[x][y])]
    return Neigh,Pred

KeyPos = [None]*key_cnt
DoorPos = [None]*key_cnt
KeyGraph = [None]*key_cnt
KeyPred = [None]*key_cnt
for i in range(H):
    for j in range(W):
        if is_key(G[i][j]):
            k = key(G[i][j])
            KeyPos[k] = (i,j)
            Neigh,Pred = bfs_key_to_key(i,j)
            KeyGraph[k] = Neigh
            KeyPred[k] = Pred
        elif is_door(G[i][j]):
            DoorPos[door(G[i][j])] = (i,j)
KeyPos.append((x0-1,y0-1))
Neigh,Pred = bfs_key_to_key(x0-1,y0-1)
KeyGraph.append(Neigh)
KeyPred.append(Pred)
KeyPos.append((x0-1,y0+1))
Neigh,Pred = bfs_key_to_key(x0-1,y0+1)
KeyGraph.append(Neigh)
KeyPred.append(Pred)
KeyPos.append((x0+1,y0-1))
Neigh,Pred = bfs_key_to_key(x0+1,y0-1)
KeyGraph.append(Neigh)
KeyPred.append(Pred)
KeyPos.append((x0+1,y0+1))
Neigh,Pred = bfs_key_to_key(x0+1,y0+1)
KeyGraph.append(Neigh)
KeyPred.append(Pred)

def dijkstra_in_key_graph():
    u0 = (key_cnt, key_cnt+1, key_cnt+2, key_cnt+3, 0)
    Dist = {u0: 0}
    Pred = {u0: None}
    Q = [(0,u0)]
    while Q:
        d,u = heappop(Q)  # k the mask of found keys
        if d>Dist[u]:
            continue
        u1,u2,u3,u4,k = u
        if k==kfull:
            break
        for v1,d,kv in KeyGraph[u1]:
            if kv&k==kv:
                v = (v1, u2, u3, u4, k|(1<<v1))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    Pred[v] = u
                    heappush(Q,(Dist[v],v))
        for v2,d,kv in KeyGraph[u2]:
            if kv&k==kv:
                v = (u1, v2, u3, u4, k|(1<<v2))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    Pred[v] = u
                    heappush(Q,(Dist[v],v))
        for v3,d,kv in KeyGraph[u3]:
            if kv&k==kv:
                v = (u1, u2, v3, u4, k|(1<<v3))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    Pred[v] = u
                    heappush(Q,(Dist[v],v))
        for v4,d,kv in KeyGraph[u4]:
            if kv&k==kv:
                v = (u1, u2, u3, v4, k|(1<<v4))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    Pred[v] = u
                    heappush(Q,(Dist[v],v))
    Path = []
    while u is not None:
        Path.append(u)
        u = Pred[u]
    Path.reverse()
    return Path

Path = dijkstra_in_key_graph()

Col = {'.': (220,220,220), '#': (50,50,50), '@': (255,0,0)}
for i in range(key_cnt):
    Col[chr(i+ord('a'))] = (0,220,220)
    Col[chr(i+ord('A'))] = (0,0,150)

A = 5
Img = Image.new('RGB',(W,H))
Pix = Img.load()
for i in range(H):
    for j in range(W):
        Pix[j,i] = Col[G[i][j]]
os.system('mkdir anim18')
f = 0
for i in range(len(Path)-1):
    u1,u2,u3,u4,_ = Path[i]
    v1,v2,v3,v4,_ = Path[i+1]
    i1,j1 = KeyPos[u1]
    i2,j2 = KeyPos[u2]
    i3,j3 = KeyPos[u3]
    i4,j4 = KeyPos[u4]
    Pix[j1,i1] = Pix[j2,i2] = Pix[j3,i3] = Pix[j4,i4] = Col['@']
    u,v = next((u,v) for u,v in zip(Path[i],Path[i+1]) if u!=v)
    w = KeyPos[v]
    SubPath = []
    while w is not None:
        SubPath.append(w)
        w = KeyPred[u][w]
    SubPath.reverse()
    for i,j in SubPath:
        Pix[j,i] = (255,0,0)
        if (i,j)==KeyPos[v]:
            di,dj = DoorPos[v]
            Pix[dj,di] = Col['.']
            Img1 = Img.copy()
            Drw = ImageDraw.Draw(Img1)
            Drw.line((j,i,dj,di), fill=(100,255,200))
            Img1.resize((A*W,A*H)).save('anim18/frame%04d.gif' % f)
            Img1.close()
        else:
            Img.resize((A*W,A*H)).save('anim18/frame%04d.gif' % f)
        f += 1
        Pix[j,i] = Col['.']
Img.close()
os.system('gifsicle -O3 -l -d4 anim18/*.gif > anim18.gif')
os.system('rm -r anim18')
