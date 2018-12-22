#!/usr/bin/env python3

from heapq import *

# Input
D = 7863
TX,TY = 14,760


# Part 1
def gen(H,W):
    G = [[0]*W for _ in range(H)]
    E = [[0]*W for _ in range(H)]
    C = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i==j==0 or (i,j)==(TX,TY):
                G[i][j] = 0
            elif j==0:
                G[i][j] = i*16807
            elif i==0:
                G[i][j] = j*48271
            else:
                G[i][j] = E[i-1][j]*E[i][j-1]
            E[i][j] = (G[i][j]+D)%20183
            C[i][j] = E[i][j]%3
    return C

C = gen(TX+1,TY+1)
print(sum(sum(L) for L in C))


# Part 2
C = gen(TX+800,TY+800)

# using the coding neither = 0, torch = 1, climbing gear = 2
# the excluded tool at (i,j) is exactly C[i][j]!
# (rocky = 0 = neither excluded, wet = 1 = torch excluded, ...)
def succ(i,j,tool):
    # move
    for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if x>=0 and y>=0 and tool!=C[x][y]:
            yield ((x,y,tool),1)
    # change tool
    other_tool = 3-tool-C[i][j]
    yield ((i,j,other_tool),7)

def dijkstra():
    u0 = (0,0,1)
    uf = (TX,TY,1)
    Dist = {u0: 0}
    Q = [(0,u0)]
    while Q:
        d,u = heappop(Q)
        if d>Dist[u]:
            continue
        if u==uf:
            break
        for v,w in succ(*u):
            if v not in Dist or Dist[u]+w<Dist[v]:
                Dist[v] = Dist[u]+w
                heappush(Q,(Dist[v],v))
    return Dist[uf]

print(dijkstra())
