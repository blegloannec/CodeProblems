#!/usr/bin/env python3

A = '.O'

H,W, N = map(int, input().split())
R = [list(map(int, input())) for _ in range(2)]
R.reverse()
G = [[A.index(c) for c in input()] for _ in range(H)]
for _ in range(N):
    O = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if G[i][j]:
                for di in (-1,0,1):
                    for dj in (-1,0,1):
                        if not di==dj==0 and 0<=i+di<H and 0<=j+dj<W:
                            O[i+di][j+dj] += 1
    for i in range(H):
        for j in range(W):
            G[i][j] = R[G[i][j]][O[i][j]]
print('\n'.join(''.join(A[c] for c in L) for L in G))
