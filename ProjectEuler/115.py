#!/usr/bin/env python

m = 50

memo = {}
def N(n):
    if n==0:
        return 1
    if n in memo:
        return memo[n]
    res = N(n-1)
    if n>=m:
        res += 1
    for k in range(n-m-1,-1,-1):
        res += N(k)
    memo[n] = res
    return res

def main():
    n = 1
    while N(n)<=1000000:
        n += 1
    print n

main()
