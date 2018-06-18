#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math

T = int(sys.stdin.readline())
for t in range(1,T+1):
    A,N = tuple(map(int,sys.stdin.readline().split()))
    V = map(int,sys.stdin.readline().split())
    if A==1:
        print 'Case #%d: %d' % (t,N)
        continue
    V.sort()
    nbmod = N
    minmod = nbmod
    curr = A
    for v in V:
        while curr <= v:
            curr = 2*curr-1
            nbmod += 1
        curr += v
        nbmod -= 1
        minmod = min(minmod,nbmod)
    print 'Case #%d: %d' % (t,minmod)
