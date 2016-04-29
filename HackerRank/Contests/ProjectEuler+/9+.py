#!/usr/bin/env python

import sys
from math import sqrt

def precomp(N):
    M = [-1 for _ in xrange(N+1)]
    for a in xrange(1,N/3):
        for b in xrange(a,(N-1-a)/2):
            c = sqrt(a*a+b*b)
            ic = int(c)
            if ic==c and a+b+ic<=N:
                M[a+b+ic] = max(M[a+b+ic],a*b*ic)
    return M

def main():
    M = precomp(3000)
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print M[N]

main()
