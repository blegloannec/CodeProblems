#!/usr/bin/env python

import sys

def main():
    N,K = map(int,sys.stdin.readline().split())
    P = [n*(3*n-1)/2 for n in xrange(1,N)]
    S = set(P)
    for n in xrange(K,N-1):
        if P[n]-P[n-K] in S or P[n]+P[n-K] in S:
            print P[n]

main()
