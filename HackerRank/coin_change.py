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
    res = 0
    for ss in range(s,-1,-V[k]):
        res += C(ss,k-1)
    memo[(s,k)] = res
    return res

def main():
    global V
    N,M = map(int,sys.stdin.readline().split())
    V = map(int,sys.stdin.readline().split())
    print C(N,M-1)

main()
