#!/usr/bin/env python

import sys

def precomp():
    N = 8*10**6+1
    cpt = [0 for _ in xrange(N)]
    for y in xrange(1,N):
        z4 = (3*y-1) - ((3*y-1)%4)
        n = y*(3*y-z4)
        while z4>0 and n<N:
            cpt[n] += 1
            z4 -= 4
            n = y*(3*y-z4)
    return cpt

def main():
    S = precomp()
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        print S[n]

main()
