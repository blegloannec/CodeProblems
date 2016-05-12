#!/usr/bin/env python

import sys

def pandigital(m,n,k):
    t = [False for _ in xrange(k+1)]
    t[0] = True
    cpt = 0
    for i in xrange(1,n+1):
        mi = m*i
        while mi>0:
            c = mi%10
            if c>k or t[c]:
                return False
            t[c] = True
            cpt += 1
            mi /= 10
    return cpt==k

def main():
    N,K = map(int,sys.stdin.readline().split())
    for m in xrange(2,N):
        for n in xrange(2,K+1):
            if pandigital(m,n,K):
                print m

main()
