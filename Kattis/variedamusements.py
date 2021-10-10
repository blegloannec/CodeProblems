#!/usr/bin/env python3

MOD = 10**9+7

n,a,b,c = map(int, input().split())
A,B,C = a,b,c
for _ in range(2, n+1):
    A,B,C = (a*(B+C))%MOD, (b*(A+C))%MOD, (c*(A+B))%MOD
print((A+B+C)%MOD)
