#!/usr/bin/env python3

S = 10

def dfs_backtrack(G, x,y):
    res = 0
    for dx,dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
        bx, by = x+dx, y+dy
        vx, vy = bx+dx, by+dy
        if 0<=vx<S and 0<=vy<S and G[vx][vy]=='.' and G[bx][by]=='B':
            G[bx][by] = '.'
            res = max(res, 1+dfs_backtrack(G, vx,vy))
            G[bx][by] = 'B'
    return res

def main():
    T = int(input())
    for _ in range(T):
        input()
        G = [list(input().replace('#','.')) for _ in range(S)]
        res = 0
        for x in range(S):
            for y in range(S):
                if G[x][y]=='W':
                    G[x][y] = '.'
                    res = max(res, dfs_backtrack(G, x,y))
                    G[x][y] = 'W'
        print(res)

main()
