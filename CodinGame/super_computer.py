#!/usr/bin/env python3

N = int(input())
T = []
for _ in range(N):
    j,d = map(int,input().split())
    T.append((j+d-1,j))

T.sort()
cpt = 0
curr = 0
for (e,b) in T:
    if curr<b:
        curr = e
        cpt += 1
print(cpt)
