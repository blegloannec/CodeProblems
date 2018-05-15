#!/usr/bin/env python3

W,H = map(int,input().split())
N = int(input())
G = [input() for _ in range(H)]
C = [sum(int(G[i][j]=='#') for i in range(H)) for j in range(W)]
for _ in range(N):
    C = [sum(int(C[j]>=i) for j in range(W)) for i in range(H,0,-1)]
    W,H = H,W
for i in range(H,0,-1):
    print(''.join('#' if C[j]>=i else '.' for j in range(W)))
