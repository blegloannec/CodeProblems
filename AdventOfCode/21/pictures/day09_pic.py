#!/usr/bin/env python3

import sys

Map = [list(map(int, L.strip())) for L in sys.stdin.readlines()]
H,W = len(Map), len(Map[0])


## Part 1
Lows = []
part1 = 0
for i in range(H):
    for j in range(W):
        low = True
        for vi,vj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0<=vi<H and 0<=vj<W and Map[i][j]>=Map[vi][vj]:
                low = False
                break
        if low:
            part1 += 1+Map[i][j]
            Lows.append((i,j))
#print(part1)


## Part 2
Seen = [[Map[i][j]==9 for j in range(W)] for i in range(H)]
Basins = []
for li,lj in Lows:
    assert not Seen[li][lj]
    Seen[li][lj] = True
    S = [(li,lj)]
    B = []
    while S:  # DFS
        i,j = S.pop()
        B.append((i,j))
        for vi,vj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0<=vi<H and 0<=vj<W and not Seen[vi][vj]:
                Seen[vi][vj] = True
                S.append((vi,vj))
    Basins.append(B)
Basins.sort(key=len, reverse=True)
#print(len(Basins[0])*len(Basins[1])*len(Basins[2]))


## Picture
from PIL import Image

Img = Image.new('RGB', (W,H))
Pix = Img.load()
for i in range(H):
    for j in range(W):
        c = 25*(10-Map[i][j])
        Pix[j,i] = (c, c, c)

for i,j in Lows:
    Pix[j,i] = (25, 25, Pix[j,i][0])

for B in Basins[:3]:
    for i,j in B:
        Pix[j,i] = (25, 25, Pix[j,i][2])

Img.resize((5*W,5*H), Image.NEAREST).save('pic09.png')
