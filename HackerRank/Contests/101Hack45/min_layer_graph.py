#!/usr/bin/env python

import sys

# pretty naive dp in O(n^3 * k) works here
# the optimal for k>3 is actually to put only 1 vertex by layer
# except for one layer that contains the remaining n-(k-1)
# so that the solution is k-3 + 2*(n-(k-1))

inf = float('inf')

memo = {(1,1,1):0}
def dp(n,k,l=1):
    if (k==1 and n>1) or k-1+l>n:
        return inf
    if (n,k,l) in memo:
        return memo[n,k,l]
    memo[n,k,l] = min(dp(n-l,k-1,m)+m*l for m in xrange(1,n-l+1))
    return memo[n,k,l]

def main():
    n,k = map(int,sys.stdin.readline().split())
    res = dp(n,k)
    print -1 if res==inf else res

main()
