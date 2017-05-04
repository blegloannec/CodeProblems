#!/usr/bin/env python

from math import sqrt
from collections import defaultdict

# runs in 35s with pypy

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
    N = 5000
    M = 10**16
    P = sieve(N*N)
    S = defaultdict(int)
    S[0] = 1
    for p in xrange(2,N):
        if P[p]:
            S0 = S.copy()
            for s in S0:
                S[s+p] = (S[s+p]+S0[s])%M
    cpt = 0
    for s in S:
        if P[s]:
            cpt = (cpt+S[s])%M
    print(cpt)

main()
