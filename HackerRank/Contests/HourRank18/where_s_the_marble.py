#!/usr/bin/env python3

m,n = map(int,input().split())
for _ in range(n):
    a,b = map(int,input().split())
    if a==m:
        m = b
    elif b==m:
        m = a
print(m)
