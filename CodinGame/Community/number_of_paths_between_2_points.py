#!/usr/bin/env python3

M = int(input())
N = int(input())
G = [input() for _ in range(M)]
DP = [[0]*N for _ in range(M)]
DP[0][0] = int(G[0][0]=='0')
for i in range(M):
    for j in range(N):
        if i==j==0:
            continue
        if G[i][j]=='0':
            DP[i][j] = (DP[i-1][j] if i>0 else 0) + (DP[i][j-1] if j>0 else 0)
print(DP[M-1][N-1])
