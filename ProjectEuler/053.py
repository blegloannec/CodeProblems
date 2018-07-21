#!/usr/bin/env python

memo = {}
def C(n,p):
    if p==0 or p==n:
        return 1
    if (n,p) in memo:
        return memo[n,p]
    res = n*C(n-1,p-1)/p
    memo[n,p] = res
    return res

def problem53():
    cpt = 0
    for n in range(1,101):
        for p in range(1,n-1):
            if C(n,p)>1000000:
                cpt += 1
    print cpt

problem53()
