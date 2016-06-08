#!/usr/bin/env python

# NB: le +1 si n>=3
# pourrait etre remplace par la convention 0:2

memo = {0:1}
def N(n):
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
