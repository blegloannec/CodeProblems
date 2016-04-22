#!/usr/bin/env python

import sys

V = [1,2,5,10,20,50,100,200]
NMAX = 100000
M = 1000000007

C = [[0 for k in xrange(len(V))] for n in xrange(NMAX+1)]
def progdyn():
    for k in xrange(len(V)):
        C[0][k] = 1
    for n in xrange(NMAX):
        for k in xrange(len(V)):
            C[n][k] = C[n][k-1]
            if n>=V[k]:
                C[n][k] = (C[n][k]+C[n-V[k]][k])%M

def main():
    progdyn()
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print C[N][len(V)-1]

main()
