#!/usr/bin/env python

import sys

def main():
    g = int(sys.stdin.readline())
    for _ in xrange(g):
        n = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        I = [0 for _ in xrange(n)]
        for i in xrange(1,n):
            if A[i]>A[I[i-1]]:
                I[i] = i
            else:
                I[i] = I[i-1]
        p = n-1
        cpt = 0
        while p>=0:
            p = I[p]-1
            cpt += 1
        print 'ANDY' if cpt%2==0 else 'BOB'

main()
