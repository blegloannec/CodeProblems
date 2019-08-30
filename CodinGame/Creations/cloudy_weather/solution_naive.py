#!/usr/bin/env python3

from collections import deque
from PIL import Image

def bfs():
    assert Map[X0][Y0] and Map[X1][Y1]
    Dist = {(X0,Y0): 0}
    Pred = {(X0,Y0): (None,None)}
    Q = deque([(X0,Y0)])
    while Q:
        x,y = Q.popleft()
        if (x,y)==(X1,Y1):
            break
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<Xmax and 0<=vy<Ymax and Map[vx][vy] and (vx,vy) not in Dist:
                Dist[vx,vy] = Dist[x,y] + 1
                Pred[vx,vy] = (x,y)
                Q.append((vx,vy))
    Path = []
    x,y = X1,Y1
    while x is not None:
        Path.append((x,y))
        x,y = Pred[x,y]
    Path.reverse()
    return Dist[X1,Y1], Path

def main():
    global X0,Y0,X1,Y1,Xmax,Ymax,Map
    X0,Y0 =  map(int,input().split())
    X1,Y1 =  map(int,input().split())
    N = int(input())
    Clouds = [tuple(map(int,input().split())) for _ in range(N)]
    Xmax = max(max(x+w for x,_,w,_ in Clouds),X0+1,X1+1)
    Ymax = max(max(y+h for _,y,_,h in Clouds),Y0+1,Y1+1)
    Map = [[True]*Ymax for _ in range(Xmax)]
    Img = Image.new('RGB', (Xmax,Ymax), (255,255,255))
    Pix = Img.load()
    for x,y,w,h in Clouds:
        for i in range(x,x+w):
            for j in range(y,y+h):
                Map[i][j] = False
                Pix[i,j] = (64,64,64)
    dist,Path = bfs()
    print(dist)
    for p in Path:
        Pix[p] = (255,0,0)
    Img.save('full_map.png')

main()
