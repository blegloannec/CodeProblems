#!/usr/bin/env python3

# this DP passes part 1 and part 2 of the problem "The hungry duck"

W,H = map(int,input().split())
F = [list(map(int,input().split())) for _ in range(H)]
for i in range(1,H):
    F[i][0] += F[i-1][0]
for j in range(1,W):
    F[0][j] += F[0][j-1]
for i in range(1,H):
    for j in range(1,W):
        F[i][j] += max(F[i-1][j],F[i][j-1])
print(F[H-1][W-1])
