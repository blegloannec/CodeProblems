#!/usr/bin/env python

# a simple DP does well enough, runs in 37s with pypy
# surprisingly overrated (difficulty 70%)!

memo = {}
# number of partitions of B black + W white where
# all components are <= M (lexicographical order)
def dp(B,W,M):
    if B==W==0:
        return 1
    if (B,W,M) in memo:
        return memo[B,W,M]
    res = 0
    for b in xrange(min(B,M[0])+1):
        for w in xrange(W+1):
            if (0,0)<(b,w)<=M:
                res += dp(B-b,W-w,(b,w))
    memo[B,W,M] = res
    return res

print dp(60,40,(60,40))
