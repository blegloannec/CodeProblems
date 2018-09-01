#!/usr/bin/env python

import sys
from collections import defaultdict

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def main():
    N = int(sys.stdin.readline())
    P = map(int,sys.stdin.readline().split())
    if sorted(P)==P:
        print '%.6f' % 0
        return
    D = defaultdict(int)
    for p in P:
        D[p] += 1
    f = 1
    for d in D:
        f *= fact(D[d])
    print '%.6f' % (float(fact(N))/f)

main()
