#!/usr/bin/env python3

from heapq import *
from PIL import Image

def dijkstra():
    dist = lambda i,j: lambda ii,jj: abs(X[ii]-X[i]) + abs(Y[jj]-Y[j])
    i0,j0,i1,j1 = DX[X0],DY[Y0],DX[X1],DY[Y1]
    assert Map[i0][j0] and Map[i1][j1]
    Dist = {(i0,j0): 0}
    Pred = {(i0,j0): (None,None)}
    Q = [(0,i0,j0)]
    while Q:
        d,i,j = heappop(Q)
        if d>Dist[i,j]:
            continue
        if (i,j)==(i1,j1):
            break
        distij = dist(i,j)
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<len(X) and 0<=vj<len(Y) and Map[vi][vj] and \
               ((vi,vj) not in Dist or Dist[vi,vj] > Dist[i,j]+distij(vi,vj)):
                Dist[vi,vj] = Dist[i,j] + distij(vi,vj)
                Pred[vi,vj] = (i,j)
                heappush(Q, (Dist[vi,vj],vi,vj))
    Path = []
    i,j = i1,j1
    while i is not None:
        Path.append((i,j))
        i,j = Pred[i,j]
    Path.reverse()
    return Dist[i1,j1], Path

def main():
    global X0,Y0,X1,Y1,X,Y,DX,DY,Map
    X0,Y0 =  map(int,input().split())
    X1,Y1 =  map(int,input().split())
    N = int(input())
    Clouds = [tuple(map(int,input().split())) for _ in range(N)]
    X, Y = [X0,X1], [Y0,Y1]
    for x,y,w,h in Clouds:
        X += [x-1,x,x+w-1,x+w]
        Y += [y-1,y,y+h-1,y+h]
    X, Y = sorted(set(X)), sorted(set(Y))
    DX = {x:i for i,x in enumerate(X)}
    DY = {y:i for i,y in enumerate(Y)}
    Map = [[True]*len(Y) for _ in range(len(X))]
    Img = Image.new('RGB', (len(X),len(Y)), (255,255,255))
    Pix = Img.load()
    for x,y,w,h in Clouds:
        for i in range(DX[x],DX[x+w]):
            for j in range(DY[y],DY[y+h]):
                Map[i][j] = False
                Pix[i,j] = (64,64,64)
    dist,Path = dijkstra()
    print(dist)
    for p in Path:
        Pix[p] = (255,0,0)
    Img.save('comp_map.png')

main()
