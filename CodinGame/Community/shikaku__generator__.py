#!/usr/bin/env python3

# Shikaku testcases generator

import sys, random
random.seed()

BMAX = 15

H = W = int(sys.argv[1])
S = H*W
C = [[False]*W for _ in range(H)]
G = [[0]*W for _ in range(H)]
N = 0
for i in range(H):
    for j in range(W):
        if not C[i][j]:
            j1 = j+1
            while j1<W and not C[i][j1]:
                j1 += 1
            j1 = min(random.randint(j,j1-1), j+BMAX-1)
            i1 = min(random.randint(i,H-1), i+BMAX-1)
            for x in range(i,i1+1):
                for y in range(j,j1+1):
                    #assert not C[x][y]
                    C[x][y] = True
            i0 = random.randint(i,i1)
            j0 = random.randint(j,j1)
            G[i0][j0] = (i1-i+1)*(j1-j+1)
print(W,H)
for L in G:
    print(*L)
