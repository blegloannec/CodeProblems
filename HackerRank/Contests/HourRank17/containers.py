#!/usr/bin/env python

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n = int(sys.stdin.readline())
        M = []
        for _ in xrange(n):
            M.append(map(int,sys.stdin.readline().split()))
        SumL = [sum(L) for L in M]
        SumL.sort()
        SumC = [sum(M[i][j] for i in xrange(n)) for j in xrange(n)]
        SumC.sort()
        print 'Possible' if SumL==SumC else 'Impossible'

main()
