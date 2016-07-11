#!/usr/bin/env python

from math import sqrt
from bisect import *

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def main():
    M = 10**8
    P = sieve(M)
    L = [2]
    for p in xrange(3,M,2):
        if P[p]:
            L.append(p)
    cpt = 0
    i = 0
    while L[i]<=10000:
        j = bisect_right(L,M/L[i])
        cpt += j-i
        i += 1
    print cpt

main()
