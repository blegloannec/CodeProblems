#!/usr/bin/env python

import sys

memo = {1:1, 2:1}
def fib(n,k):
    if n in memo:
        return memo[n]
    res = fib(n-1,k)+k*fib(n-2,k)
    memo[n] = res
    return res

def main():
    n,k = map(int,sys.stdin.readline().split())
    print fib(n,k)

main()
