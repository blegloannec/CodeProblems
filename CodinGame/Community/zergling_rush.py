#!/usr/bin/env python3

w,h = [int(i) for i in input().split()]
grid = []
for i in range(h):
    grid.append(list(input()))

access = [[False for _ in range(w)] for _ in range(h)]

def dfs(x,y):
    if not access[x][y]:
        access[x][y] = True
        if x>0 and grid[x-1][y]=='.':
            dfs(x-1,y)
        if x<h-1 and grid[x+1][y]=='.':
            dfs(x+1,y)
        if y>0 and grid[x][y-1]=='.':
            dfs(x,y-1)
        if y<w-1 and grid[x][y+1]=='.':
            dfs(x,y+1)

for x in range(h):
    for y in [0,w-1]:
        if grid[x][y]=='.' and not access[x][y]:
            dfs(x,y)
for y in range(w):
    for x in [0,h-1]:
        if grid[x][y]=='.' and not access[x][y]:
            dfs(x,y)

for x in range(h):
    for y in range(w):
        if grid[x][y]=='B':
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if 0<=x+dx<h and 0<=y+dy<w and access[x+dx][y+dy]:
                        grid[x+dx][y+dy] = 'z'

for l in grid:
    print(''.join(l))
