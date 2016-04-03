#!/usr/bin/env python

memo = {}
def N(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n in memo:
        return memo[n]
    res = N(n-1)
    for m in range(2,5):
        res += N(n-m)
    memo[n] = res
    return res

print N(50)
