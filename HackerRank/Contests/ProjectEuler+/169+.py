#!/usr/bin/env python

import sys

memo = {0:1,1:1}
def f(n):
    if n in memo:
        return memo[n]
    if n%2==0:
        res = f(n/2)+f((n-2)/2)
    else:
        res = f((n-1)/2)
    memo[n] = res
    return res

print f(int(sys.stdin.readline()))
