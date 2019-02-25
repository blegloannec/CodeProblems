#!/usr/bin/env python3

D = { 1: {'_':-1, '/':-10, '\\':  9},
     -1: {'_':-1, '/':  9, '\\':-10}}

I = int(input())
W,H = map(int,input().split())
G = [input() for _ in range(H)]
G = [next(G[i][j] for i in range(H) if G[i][j]!='.') for j in range(W)]

i,d = 0,1
while 0<=i<W and not (I==0 and G[i]=='_'):
    I += D[d][G[i]]
    if I<0:  I,d = -I,-d
    if I!=0: i += d
print(max(0,min(i,W-1)))
