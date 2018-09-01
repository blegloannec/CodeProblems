#!/usr/bin/env python

import sys

def main():
    n,d = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    Cdeb = [0 for _ in xrange(n)]
    Cfin = [0 for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(i+1,n):
            if A[j]-A[i]==d:
                Cdeb[i] += 1
                Cfin[j] += 1
    res = 0
    for i in xrange(n):
        res += Cdeb[i]*Cfin[i]
    print res

main()
