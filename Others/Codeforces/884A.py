#!/usr/bin/env python3

n,t = map(int,input().split())
A = list(map(int,input().split()))
d = 0
while t>0:
    t -= 86400-A[d]
    d += 1
print(d)
