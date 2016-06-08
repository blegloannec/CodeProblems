#!/usr/bin/env python

import sys

def main():
    N,K = map(int,sys.stdin.readline().split())
    cpt = 0
    C = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]
    C[1][0] = 1
    C[1][1] = 1
    for n in range(2,N+1):
        C[n][0] = 1
        for p in range(1,n+1):
            C[n][p] = C[n-1][p-1]+C[n-1][p]
            if C[n][p]>K:
                cpt += 1
    print cpt

main()
