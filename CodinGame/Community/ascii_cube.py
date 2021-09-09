#!/usr/bin/env python3

w = int(input())*2
h = int(input())
d = int(input())

G = [[' ']*(w+h+d) for _ in range(h+d+1)]
for j in range(w):
    if not (j>=w-2 and (h==1 or d==1)):
        G[h][h+d+j] = '.'
    G[h+d][h+j] = G[0][d+j] = G[d][j] = '_'

for i in range(1,d+1):
    if not (i==d and (w==2 or h==1)):
        G[h+i][h+d-i] = '⠌'
    G[i][d-i] = G[i][d+w-i] = G[h+i][h+d+w-i] = '/'

for k in range(h-1,-1,-1):
    if not (k==0 and (w==2 or d==1)):
        G[1+k][d+k] = '⠡'
    G[1+k][d+w+k] = G[1+d+k][k] = G[1+d+k][w+k] = '\\'

print('\n'.join(''.join(L).rstrip() for L in G))
