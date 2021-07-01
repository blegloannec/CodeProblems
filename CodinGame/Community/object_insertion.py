#!/usr/bin/env python3

import numpy as np

h,w = map(int, input().split())
O = np.array([[c=='*' for c in input()] for _ in range(h)])
H,W = map(int, input().split())
G = [list(input()) for _ in range(H)]

M = np.array([[c=='#' for c in L] for L in G])
Pos = []
for i in range(H-h+1):
    for j in range(W-w+1):
        if not np.any(M[i:i+h,j:j+w] & O):
            Pos.append((i,j))

print(len(Pos))
if len(Pos)==1:
    i,j = Pos[0]
    for di in range(h):
        for dj in range(w):
            if O[di,dj]:
                G[i+di][j+dj] = '*'
    print('\n'.join(''.join(L) for L in G))
