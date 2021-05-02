#!/usr/bin/env python3

W = int(input())
H = int(input())
G = [input() for _ in range(H)]
C = [[0]*W   for _ in range(H)]
for i in range(H):
    for j in range(W):
        if G[i][j]=='x':
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==dj==0: continue
                    vi = i+di; vj = j+dj
                    if 0<=vi<H and 0<=vj<W and G[vi][vj]!='x':
                        C[vi][vj] += 1
print('\n'.join(''.join('.' if c==0 else str(c) for c in L) for L in C))
