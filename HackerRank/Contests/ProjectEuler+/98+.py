#!/usr/bin/env python

import sys
from math import sqrt

def main():
    N = int(sys.stdin.readline())
    D = {}
    maxcpt = 0
    maxn = 0
    for a in xrange(int(sqrt(10**(N-1))),int(sqrt(10**N))+1):
        k = tuple(sorted(str(a*a)))
        if k in D:
            c,n = D[k]
            n = max(n,a*a)
            if c+1==maxcpt and n>maxn:
                maxn = n
            elif c+1>maxcpt:
                maxcpt = c+1
                maxn = n
            D[k] = (c+1,n)
        else:
            D[k] = (1,a*a)
    print maxn

main()
