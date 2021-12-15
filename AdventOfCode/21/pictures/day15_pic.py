#!/usr/bin/env python3

import sys
from heapq import *
from PIL import Image

INF = 1<<30

def dijkstra(Map, i0,j0, i1,j1):
    S = len(Map)
    Dist = [[INF]*S for _ in range(S)]
    Pred = [[None]*S for _ in range(S)]
    Dist[i0][j0] = 0
    Q = [(0,i0,j0)]
    while Q:
        d,i,j = heappop(Q)
        if i==i1 and j==j1:
            break
        if d>Dist[i][j]:
            continue
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<S and 0<=vj<S and Dist[i][j]+Map[vi][vj]<Dist[vi][vj]:
                Dist[vi][vj] = Dist[i][j]+Map[vi][vj]
                Pred[vi][vj] = (i,j)
                heappush(Q, (Dist[vi][vj],vi,vj))
    Path = []
    i,j = i1,j1
    while (i,j)!=(i0,j0):
        Path.append((i,j))
        i,j = Pred[i][j]
    Path.append((i0,j0))
    Path.reverse()
    return (Dist[i1][j1], Path)

def draw_img(Map, Path):
    S = len(Map)
    Img = Image.new('RGB', (S,S))
    Pix = Img.load()
    for i in range(S):
        for j in range(S):
            Pix[j,i] = (0, 5*Map[i][j], 10*Map[i][j])
    for i,j in Path:
        Pix[j,i] = (20*Map[i][j]+50, 0, 0)
    return Img

def main():
    # Part 1
    Map = [list(map(int, L.strip())) for L in sys.stdin.readlines()]
    S = len(Map)
    d, Path = dijkstra(Map, 0,0, S-1,S-1)
    #print(d)
    draw_img(Map, Path).resize((5*S,5*S), Image.NEAREST).save('pic15_1.png')
    # Part 2
    S5 = 5*S
    Map5 = [[(Map[i%S][j%S]+i//S+j//S-1)%9+1 for j in range(S5)] for i in range(S5)]
    d5, Path5 = dijkstra(Map5, 0,0, S5-1,S5-1)
    #print(d5)
    draw_img(Map5, Path5).save('pic15_2.png')

main()
