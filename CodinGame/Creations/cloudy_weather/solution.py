#!/usr/bin/env python3

from heapq import *

dist = lambda i,j: lambda ii,jj: abs(X[ii]-X[i]) + abs(Y[jj]-Y[j])

# considering the given maps, A* would be more efficient in most cases,
# however I want it to pass with Dijkstra in a slow language
def dijkstra(i0,j0, i1,j1):
    Dist = {(i0,j0): 0}
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
                heappush(Q, (Dist[vi,vj],vi,vj))
    return Dist[i1,j1]

def build_compressed_map(x0,y0, x1,y1, Clouds):
    global X,Y,XIdx,YIdx,Map
    # "compressing" coordinates
    X, Y = [x0,x1], [y0,y1]
    for x,y,w,h in Clouds:
        X += [x-1,x,x+w-1,x+w]
        Y += [y-1,y,y+h-1,y+h]
    X, Y = sorted(set(X)), sorted(set(Y))
    XIdx, YIdx = {x:i for i,x in enumerate(X)}, {y:i for i,y in enumerate(Y)}
    # we efficiently compute the union of rectangles, though it is not
    # actually needed for the given testcases (the overlapping surface
    # always remain reasonable)
    Events  = [(XIdx[x],   YIdx[y], YIdx[y+h],  1) for x,y,w,h in Clouds]
    Events += [(XIdx[x+w], YIdx[y], YIdx[y+h], -1) for x,y,w,h in Clouds]
    Events.sort()
    Map = []
    Curr = [0]*len(Y)
    e = 0
    for i in range(len(X)):
        while e<len(Events) and Events[e][0]==i:
            _,jl,jr,c = Events[e]
            for j in range(jl,jr):
                Curr[j] += c
            e += 1
        Map.append([c==0 for c in Curr])

def main():
    Xs,Ys = map(int,input().split())
    Xd,Yd = map(int,input().split())
    N = int(input())
    Clouds = [tuple(map(int,input().split())) for _ in range(N)]
    build_compressed_map(Xs,Ys, Xd,Yd, Clouds)
    print(dijkstra(XIdx[Xs],YIdx[Ys], XIdx[Xd],YIdx[Yd]))

main()
