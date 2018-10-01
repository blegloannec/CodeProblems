#!/usr/bin/env python3

W = int(input())
H = int(input())
G = [[1]*(W+2)]
for _ in range(H):
    G.append([1]+list(map(int,input().split()))+[1])
G.append([1]*(W+2))

print(*next((j-1,i-1) for i in range(1,H+1) for j in range(1,W+1) if G[i][j]==0 and sum(sum(G[l][j-1:j+2]) for l in range(i-1,i+2))==8))
