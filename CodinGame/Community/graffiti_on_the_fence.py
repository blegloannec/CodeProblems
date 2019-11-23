#!/usr/bin/env python3

L = int(input())
N = int(input())
I = sorted(tuple(map(int,input().split())) for _ in range(N)) + [(L,L)]
x = 0
C = []
for l,r in I:
    if x<l: C.append((x,l))
    if x<r: x = r
if not C:
    print('All painted')
else:
    for itv in C:
        print(*itv)
