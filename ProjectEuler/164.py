#!/usr/bin/env python

S = 9

# DP for the number of such numbers of size n
# ending with the digits ab
memo = {}
def count(n,a,b):
    if n==2:
        return 1 if a>0 else 0
    if (n,a,b) in memo:
        return memo[n,a,b]
    res = 0
    for x in xrange(S-(a+b)+1):
        res += count(n-1,x,a)
    memo[n,a,b] = res
    return res

def main():
    res = 0
    for a in xrange(10):
        for b in xrange(10):
            res += count(20,a,b)
    print res

main()