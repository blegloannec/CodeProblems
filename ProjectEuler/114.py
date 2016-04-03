#!/usr/bin/env python

memo = {}
def N(n):
    if n==0:
        return 1
    if n in memo:
        return memo[n]
    res = N(n-1)
    if n>=3:
        res += 1
    for m in range(n-4,-1,-1):
        res += N(m)
    memo[n] = res
    return res

print N(50)
