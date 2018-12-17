#!/usr/bin/env python3

G = [input().split() for _ in range(9)]
R = lambda l,r: range(max(0,l),min(7,r+1))
Sol = []
for i in range(9):
    for j in range(9):
        if j<8:
            G[i][j],G[i][j+1] = G[i][j+1],G[i][j]
            if any(G[i][c]==G[i][c+1]==G[i][c+2] for c in R(j-2,j+1)) or any(G[r][c]==G[r+1][c]==G[r+2][c] for r in R(i-2,i) for c in [j,j+1]):
                Sol.append((i,j,i,j+1))
            G[i][j],G[i][j+1] = G[i][j+1],G[i][j]
        if i<8:
            G[i][j],G[i+1][j] = G[i+1][j],G[i][j]
            if any(G[r][c]==G[r][c+1]==G[r][c+2] for r in [i,i+1] for c in R(j-2,j)) or any(G[r][j]==G[r+1][j]==G[r+2][j] for r in R(i-2,i+1)):
                Sol.append((i,j,i+1,j))
            G[i][j],G[i+1][j] = G[i+1][j],G[i][j]
print(len(Sol))
for P in Sol:
    print(*P)
