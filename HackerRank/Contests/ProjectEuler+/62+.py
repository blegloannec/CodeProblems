#!/usr/bin/env python

import sys
from collections import *

def sig(n):
    d = []
    while n>0:
        d.append(n%10)
        n /= 10
    d.sort(reverse=True)
    s = 0
    for x in d:
        s = 10*s+x
    return s

def main():
    N,K = map(int,sys.stdin.readline().split())
    D = defaultdict(list)
    for n in xrange(1,N):
        c = n*n*n
        s = sig(c)
        D[s].append(n)
    S = []
    for s in D:
        if len(D[s])==K:
            S.append(min(D[s]))
    S.sort()
    for s in S:
        print s*s*s

main()
