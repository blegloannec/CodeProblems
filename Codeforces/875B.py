#!/usr/bin/env python3

n = int(input())
P = [int(p)-1 for p in input().split()]
O = [False]*n
X = n-1
H = [1]
for i in range(len(P)-1):
    O[P[i]] = True
    while X>0 and O[X]:
        X -= 1
    H.append(1 + i+1 - (n-1-X))
H.append(1)
print(' '.join(map(str,H)))
