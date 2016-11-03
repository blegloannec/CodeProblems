#!/usr/bin/env python3

n = int(input())

P = [-1 for _ in range(n+1)]
P[0] = 0
P[1] = 0

def wc(n):
    if P[n]>=0:
        return P[n]
    res = float('inf')
    for i in range(2,n):
        res = min(res,max(i,1+wc(n-i)))
    P[n] = res
    return res

print(wc(n))
