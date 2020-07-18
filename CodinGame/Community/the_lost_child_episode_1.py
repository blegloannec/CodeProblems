#!/usr/bin/env python3

from collections import deque

S = 10
G = [input() for _ in range(S)]
x0,y0 = next((x,y) for x in range(S) for y in range(S) if G[x][y]=='C')
D = [[None]*S for _ in range(S)]
D[x0][y0] = 0
Q = deque([(x0,y0)])
while Q:
    x,y = Q.popleft()
    if G[x][y]=='M':
        break
    for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0<=vx<S and 0<=vy<S and G[vx][vy]!='#' and D[vx][vy] is None:
            D[vx][vy] = D[x][y] + 1
            Q.append((vx,vy))
print(f'{10*D[x][y]}km')
