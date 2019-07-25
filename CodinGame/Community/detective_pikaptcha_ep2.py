#!/usr/bin/env python3

Dir = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

W,H = [int(i) for i in input().split()]
G = [[0 if c=='0' else c for c in input()] for _ in range(H)]
side = input()

i0,j0 = next((i,j) for i in range(H) for j in range(W) if G[i][j] in Dir)
di,dj = Dir[G[i0][j0]]
G[i0][j0] = 0

i,j = i0,j0
first = True
while first or (i,j)!=(i0,j0):
    first = False
    if side=='L':
        DV = ((-dj,di), (di,dj), (dj,-di), (-di,-dj))
    else:
        DV = ((dj,-di), (di,dj), (-dj,di), (-di,-dj))
    for dx,dy in DV:
        x, y = i+dx, j+dy
        if 0<=x<H and 0<=y<W and G[x][y]!='#':
            i,j = x,y
            di,dj = dx,dy
            G[i][j] += 1
            break
print('\n'.join(''.join(map(str, L)) for L in G))
