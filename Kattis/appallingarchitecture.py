#!/usr/bin/env python3

H,W = map(int,input().split())
G = [input() for _ in range(H)]
tot = H*W - sum(L.count('.') for L in G)
xavg = sum(sum(j for j in range(W) if L[j]!='.') for L in G) / tot
xl = next(j for j in range(W) if G[-1][j]!='.')
xr = next(j for j in range(W-1,-1,-1) if G[-1][j]!='.')
print('left' if xavg<xl-0.5 else 'right' if xr+0.5<xavg else 'balanced')
