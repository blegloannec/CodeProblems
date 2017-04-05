#!/usr/bin/env python3

from math import sqrt,ceil

n = int(input())

# DP
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

#print(wc(n))


# Closed formula
# x(x+1) = n
# x^2 + x - 2n = 0
# -1+sqrt(1+8n) / 2

def formula(n):
    return int(ceil((-1+sqrt(1+8*n))/2))

print(formula(n))
