#!/usr/bin/env python3

L = int(input())
N = int(input())
R = []
P0 = None
for _ in range(N):
    P,D,T = input().split()
    D,T = int(D),int(T)
    if P==P0 and 3600*(D-D0)/(T-T0)>L:
        R.append((P,D))
    P0,D0,T0 = P,D,T
if R:
    for (P,D) in R:
        print(P,D)
else:
    print('OK')
