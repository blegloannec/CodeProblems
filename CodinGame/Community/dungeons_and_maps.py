#!/usr/bin/env python3

Dir = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

W,H = map(int, input().split())
start = tuple(map(int, input().split()))
dmin = float('inf')
res = 'TRAP'
N = int(input())
for m in range(N):
    Map = [input() for _ in range(H)]
    Visited = [[False]*W for _ in range(H)]
    i,j = start
    d = 0
    while 0<=i<H and 0<=j<W and Map[i][j] in Dir and not Visited[i][j]:
        Visited[i][j] = True
        di,dj = Dir[Map[i][j]]
        i += di; j += dj
        d += 1
    if 0<=i<H and 0<=j<W and Map[i][j]=='T' and d<dmin:
        dmin = d; res = m
print(res)
