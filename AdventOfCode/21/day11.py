#!/usr/bin/env python3

import sys

G = [list(map(int, L.strip())) for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])

t = part1 = part2 = 0
while t<=100 or part2==0:
    t += 1
    F = []
    for i in range(H):
        for j in range(W):
            G[i][j] += 1
            if G[i][j]>9:
                G[i][j] = 0
                F.append((i,j))
    fcnt = 0
    while F:
        fcnt += len(F)
        F1 = []
        for i,j in F:
            for vi in range(max(0,i-1), min(i+2,H)):
                for vj in range(max(0,j-1), min(j+2,W)):
                    if G[vi][vj]!=0:
                        G[vi][vj] += 1
                        if G[vi][vj]>9:
                            G[vi][vj] = 0
                            F1.append((vi,vj))
        F = F1
    if t<=100:
        part1 += fcnt
    if fcnt==H*W:
        part2 = t
print(part1)
print(part2)
