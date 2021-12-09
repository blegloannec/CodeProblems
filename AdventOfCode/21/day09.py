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
print(part1)


## Part 2
# Actually basins are connected components of the map without 9s.
# It seems guaranteed that there is a unique low point for each
# and a "downward flow" path from each point in the component to
# the low point.
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
print(len(Basins[0])*len(Basins[1])*len(Basins[2]))
