#!/usr/bin/env python3

N = int(input())
G = [[c if c in 'ABH' else int(c) for c in input()] for _ in range(N)]

B = []
for i in range(N):
    for j in range(N):
        if G[i][j]=='A':
            for vi in range(max(i-3, 0), min(i+4, N)):
                for vj in range(max(j-3, 0), min(j+4, N)):
                    if isinstance(G[vi][vj], int):
                        d = 4-max(abs(vi-i), abs(vj-j))
                        G[vi][vj] = max(G[vi][vj], d)
                    elif G[vi][vj]=='B' and (vi,vj) not in B:
                        B.append((vi,vj))
        elif G[i][j]=='H':
            for vi in range(max(i-3, 0), min(i+4, N)):
                for vj in range(max(j-3, 0), min(j+4, N)):
                    if isinstance(G[vi][vj], int):
                        G[vi][vj] = max(G[vi][vj], 5)
                    elif G[vi][vj]=='B' and (vi,vj) not in B:
                        B.append((vi,vj))

b = 0
while b < len(B):
    i,j = B[b]
    b += 1
    for vi in range(max(i-3, 0), min(i+4, N)):
        if isinstance(G[vi][j], int):
            d = 4-abs(vi-i)
            G[vi][j] = max(G[vi][j], d)
        elif G[vi][j]=='B' and (vi,j) not in B:
            B.append((vi,j))
    for vj in range(max(j-3, 0), min(j+4, N)):
        if isinstance(G[i][vj], int):
            d = 4-abs(vj-j)
            G[i][vj] = max(G[i][vj], d)
        elif G[i][vj]=='B' and (i,vj) not in B:
            B.append((i,vj))

for L in G:
    print(*L, sep='')
