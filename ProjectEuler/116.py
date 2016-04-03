#!/usr/bin/env python

memo = {}
def N(m,n):
    if n==0:
        return 1
    if (m,n) in memo:
        return memo[(m,n)]
    res = N(m,n-1)
    if n==m:
        res +=1
    if n>m:
        res += N(m,n-m)
    memo[(m,n)] = res
    return res

def F(n):
    # full black are forbidden
    return N(2,n)+N(3,n)+N(4,n)-3

print F(50)
