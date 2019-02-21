#!/usr/bin/env python3

N = int(input())
L = int(input())
G = [input().split() for _ in range(N)]
H = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if G[i][j]=='C':
            for x in range(max(0,i-L+1),min(N,i+L)):
                for y in range(max(0,j-L+1),min(N,j+L)):
                    H[x][y] = False
print(sum(sum(R) for R in H))
