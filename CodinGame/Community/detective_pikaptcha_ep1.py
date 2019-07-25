#!/usr/bin/env python3

W,H = map(int,input().split())
G = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if G[i][j]!='#':
            G[i][j] = str(sum(1 for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) \
                              if 0<=x<H and 0<=y<W and G[x][y]!='#'))
print('\n'.join(''.join(L) for L in G))
