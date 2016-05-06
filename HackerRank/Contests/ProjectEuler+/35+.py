#!/usr/bin/env python

import sys
from math import *

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def rotate(n):
    l = int(log10(n))
    c = n%10
    return n/10+c*(10**l)
                
def main():
    N = int(sys.stdin.readline())
    # marge pour que les rotations soient couvertes
    P = sieve(10**int(ceil(log10(N))))
    cpt = 0
    for p in xrange(2,N):
        if P[p]:
            P[p] = False
            pcpt = p
            q = rotate(p)
            while q!=p:
                if not P[q]:
                    break
                pcpt += q
                P[q] = False
                q = rotate(q)
            if q==p:
                cpt += pcpt
    print cpt

main()
