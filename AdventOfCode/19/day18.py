#!/usr/bin/env pypy

import sys
from collections import deque
from heapq import *


G = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])

is_key  = lambda c: 'a'<=c<='z'
is_door = lambda c: 'A'<=c<='Z'
key     = lambda c: ord(c)-ord('a')
door    = lambda c: ord(c)-ord('A')


# ===== Part 1 =====
def bfs(x0,y0):
    u0 = (x0,y0,0)
    Dist = {u0: 0}
    Q = deque([u0])
    while Q:
        x,y,k = u = Q.popleft()  # k the mask of found keys
        if k==kfull:
            return Dist[u]
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and G[vx][vy]!='#':
                kv = k
                if is_key(G[vx][vy]):
                    kv |= 1<<key(G[vx][vy])
                elif is_door(G[vx][vy]) and kv&(1<<door(G[vx][vy]))==0:
                    continue
                v = (vx,vy,kv)
                if v not in Dist:
                    Dist[v] = Dist[u] + 1
                    Q.append(v)

kfull = 0
key_cnt = 0
for i in xrange(H):
    for j in xrange(W):
        if is_key(G[i][j]):
            kfull |= 1<<key(G[i][j])
            key_cnt += 1
        elif G[i][j]=='@':
            x0,y0 = i,j
G[x0][y0] = '.'
print(bfs(x0,y0))


# ===== Part 2 =====
G[x0-1][y0] = '#'
G[x0][y0]   = '#'
G[x0+1][y0] = '#'
G[x0][y0-1] = '#'
G[x0][y0+1] = '#'
# by closing the central area, we divide the graph into 4 trees
# now we know the path between two keys is unique (hence the doors
# on the path have all to be unlocked)

# we build the key to key graph
# each edge is labeled by the distance and the mask of required keys
def bfs_key_to_key(x0,y0):
    u0 = (x0,y0)
    DistReq = {u0: (0,0)}  # distance & mask of required keys
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
                    Q.append(v)
    return [(key(G[x][y]),d,k) for (x,y),(d,k) in DistReq.items() if is_key(G[x][y])]

KeyGraph = [None for _ in xrange(key_cnt)]
for i in xrange(H):
    for j in xrange(W):
        if is_key(G[i][j]):
            KeyGraph[key(G[i][j])] = bfs_key_to_key(i,j)
KeyGraph.append(bfs_key_to_key(x0-1,y0-1))  # adding starting positions as nodes
KeyGraph.append(bfs_key_to_key(x0-1,y0+1))  # (NB: without in-going edges as bfs_key_to_key()
KeyGraph.append(bfs_key_to_key(x0+1,y0-1))  #      only returns keys)
KeyGraph.append(bfs_key_to_key(x0+1,y0+1))

# computing shortest path to final state (same as the bfs of part 1
# but in the smaller graph of keys and with 4 positions in the state)
def dijkstra_in_key_graph():
    u0 = (key_cnt, key_cnt+1, key_cnt+2, key_cnt+3, 0)
    Dist = {u0: 0}
    Q = [(0,u0)]
    while Q:
        d,u = heappop(Q)  # k the mask of found keys
        if d>Dist[u]:
            continue
        u1,u2,u3,u4,k = u
        if k==kfull:
            return Dist[u]
        for v1,d,kv in KeyGraph[u1]:
            if kv&k==kv:
                v = (v1, u2, u3, u4, k|(1<<v1))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    heappush(Q,(Dist[v],v))
        for v2,d,kv in KeyGraph[u2]:
            if kv&k==kv:
                v = (u1, v2, u3, u4, k|(1<<v2))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    heappush(Q,(Dist[v],v))
        for v3,d,kv in KeyGraph[u3]:
            if kv&k==kv:
                v = (u1, u2, v3, u4, k|(1<<v3))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    heappush(Q,(Dist[v],v))
        for v4,d,kv in KeyGraph[u4]:
            if kv&k==kv:
                v = (u1, u2, u3, v4, k|(1<<v4))
                if v not in Dist or Dist[v]>Dist[u]+d:
                    Dist[v] = Dist[u] + d
                    heappush(Q,(Dist[v],v))

print(dijkstra_in_key_graph())
