#!/usr/bin/env python3

W,H = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(H)]
for j in range(W):
    for i in range(1,H):
        G[i][j] += G[i-1][j]

# O(H^2 W) -- O(n^3) for n = max(H,W) -- approach
best = float('-inf')
for i1 in range(H):
    for i2 in range(i1,H):
        # O(W) Kadane's algo. on the block of lines i1 to i2
        curr = 0
        for j in range(W):
            curr = G[i2][j] - (G[i1-1][j] if i1>0 else 0) + max(0,curr)
            best = max(best, curr)

print(best)
