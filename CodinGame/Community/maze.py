#!/usr/bin/env python3

def dfs(x,y):
    if x==0 or x==H-1 or y==0 or y==W-1:
        yield (y,x)
    seen[x][y] = True
    for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=vx<H and 0<=vy<W and G[vx][vy] and not seen[vx][vy]:
            yield from dfs(vx,vy)

def main():
    global W,H,G,seen
    W,H = map(int,input().split())
    Y,X = map(int,input().split())
    G = [[c=='.' for c in input()] for _ in range(H)]
    seen = [[False]*W for _ in range(H)]
    E = sorted(dfs(X,Y))
    print(len(E))
    for (x,y) in E:
        print(x,y)

main()
