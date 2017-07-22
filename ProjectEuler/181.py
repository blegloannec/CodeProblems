#!/usr/bin/env python

# runs in <2s with pypy

memo = {}
# number of partitions of B blacks + W whites where
# all components are of size <= M and the components
# of size exactly M have at most MB blacks
def dp(B,W,M,MB):
    if B==W==0:
        return 1
    if M==0:
        return 0
    if (B,W,M,MB) in memo:
        return memo[B,W,M,MB]
    res = dp(B,W,M-1,min(B,M-1))
    for b in xrange(max(0,M-W),MB+1):
        w = M-b
        res += dp(B-b,W-w,M,min(B-b,b))
    memo[B,W,M,MB] = res
    return res

B,W = 60,40
print dp(B,W,B+W,B)
