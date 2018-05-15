#!/usr/bin/env python3

W,H = map(int,input().split())
G = [input() for _ in range(H)]
C = [sum(int(G[i][j]=='#') for i in range(H)) for j in range(W)]
for i in range(H,0,-1):
    print(''.join('#' if C[j]>=i else '.' for j in range(W)))
