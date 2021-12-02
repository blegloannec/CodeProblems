#!/usr/bin/env python3

n = int(input())
dmax = 1
k = 2
d = ((1<<k)-1)<<(k-1)
while d<=n:
    if n%d==0:
        dmax = d
    k += 1
    d = ((1<<k)-1)<<(k-1)
print(dmax)
