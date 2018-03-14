#!/usr/bin/env python3

W = int(input())
H = int(input())
G = [input() for _ in range(H)]

R = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W-2,-1,-1):
        R[i][j] = j+1 if G[i][j+1]=='0' else R[i][j+1]

B = [[-1]*W for _ in range(H)]
for j in range(W):
    for i in range(H-2,-1,-1):
        B[i][j] = i+1 if G[i+1][j]=='0' else B[i+1][j]

for i in range(H):
    for j in range(W):
        if G[i][j]=='0':
            i1,j1 = (i,R[i][j]) if R[i][j]>=0 else (-1,-1)
            i2,j2 = (B[i][j],j) if B[i][j]>=0 else (-1,-1)
            print(j,i,j1,i1,j2,i2)
