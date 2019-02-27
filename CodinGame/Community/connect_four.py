#!/usr/bin/env python3

H,W = 6,7
G = [input() for _ in range(H)]
C = [[],[]]
for j in range(W):
    if G[0][j]!='.': continue
    i = next(i for i in range(H-1,-1,-1) if G[i][j]=='.')
    V = []
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        x,y = i+dx,j+dy
        v,c = '0',0
        if 0<=x<H and 0<=y<W and G[x][y]!='.':
            v,c = G[x][y],1
            x,y = x+dx,y+dy
            while 0<=x<H and 0<=y<W and G[x][y]==v and c<3:
                c += 1
                x,y = x+dx,y+dy
        V.append((v,c))
    for p in [0,1]:
        if any(V[d][1]*(int(V[d][0])==p+1)+V[d+1][1]*(int(V[d+1][0])==p+1)>=3 for d in range(0,8,2)):
            C[p].append(j)
for Cp in C:
    if Cp: print(*Cp)
    else:  print('NONE')
