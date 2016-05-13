#!/usr/bin/env python

import sys
from math import sqrt

# This is basically pb 31+ with prime numbers as coin values

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

V = eratosthene(1000)
NMAX = 1000

C = [[0 for k in xrange(len(V))] for n in xrange(NMAX+1)]
def progdyn():
    for k in xrange(len(V)):
        C[0][k] = 1
    for n in xrange(NMAX+1):
        for k in xrange(len(V)):
            C[n][k] = C[n][k-1]
            if n>=V[k]:
                C[n][k] = C[n][k]+C[n-V[k]][k]

def main():
    progdyn()
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print C[N][len(V)-1]

main()
