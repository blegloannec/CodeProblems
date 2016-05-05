#!/usr/bin/env python

import sys
from math import sqrt

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
    Nmax = 1000001
    P = sieve(Nmax)
    S = [0 for _ in xrange(Nmax)]
    for i in xrange(1,Nmax):
        S[i] = S[i-1]
        if P[i]:
            S[i] += i
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print S[N]

main()
