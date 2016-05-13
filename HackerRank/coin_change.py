#!/usr/bin/env python

import sys

V = []

memo = {}
def C(s,k):
    if s==0:
        return 1
    if k<0:
        return 0
    if (s,k) in memo:
        return memo[(s,k)]
    res = C(s,k-1)
    if s>=V[k]:
        res += C(s-V[k],k)
    memo[(s,k)] = res
    return res

def main():
    global V
    N,M = map(int,sys.stdin.readline().split())
    V = map(int,sys.stdin.readline().split())
    print C(N,M-1)

main()
