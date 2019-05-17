#!/usr/bin/env python3

N = int(input())
F = 0
while N&1==0:
    F += 1
    N >>= 1
d = 3
while d*d<=N:
    while N%d==0:
        F += 1
        N //= d
    d += 2
if N>1:
    F += 1
print(F)
