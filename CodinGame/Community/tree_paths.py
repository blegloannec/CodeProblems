#!/usr/bin/env python3

N = int(input())
v = int(input())
M = int(input())
P = [None]*(N+1)
for _ in range(M):
    p,l,r = map(int, input().split())
    P[l] = (p, True)
    P[r] = (p, False)

Path = []
while P[v] is not None:
    v,l = P[v]
    Path.append('Left' if l else 'Right')
Path.reverse()

print(' '.join(Path) if Path else 'Root')
