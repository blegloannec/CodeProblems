#!/usr/bin/env python3

from collections import deque

def bfs():
    for i in range(H):
        for j in range(W):
            if G[i][j]=='B':
                x0,y0 = i,j
                G[i][j] = '.'
            elif G[i][j]=='E':
                xf,yf = i,j
                G[i][j] = '.'
    Q = deque([(x0,y0)])
    D = {(x0,y0):0}
    while Q:
        x,y = Q.popleft()
        if (x,y)==(xf,yf):
            return D[xf,yf]
        for vx,vy in [(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1)]:
            if 0<=vx<H and 0<=vy<W and G[vx][vy]=='.' and (vx,vy) not in D:
                D[vx,vy] = D[x,y]+1
                Q.append((vx,vy))
    return 'Impossible'

def main():
    global W,H,G
    W,H = map(int,input().split())
    G = [list(input()) for _ in range(H)]
    print(bfs())

main()
