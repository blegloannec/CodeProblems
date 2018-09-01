#!/usr/bin/env python

import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    P = [[0 for _ in xrange(n)] for _ in xrange(m)]
    for i in xrange(n):
        P0 = map(int,sys.stdin.readline().split())
        for j in xrange(m):
            P[j][i] = P0[j]
    for j in xrange(m):
        P[j].sort()
    print ' '.join(map(str,[P[j][(n-1)/2] for j in xrange(m)]))

main()
