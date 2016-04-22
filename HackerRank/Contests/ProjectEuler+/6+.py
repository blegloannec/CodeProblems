#!/usr/bin/env python

import sys

def problem6():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        d = (n*(n+1)/2)**2-n*(n+1)*(2*n+1)/6
        print d

problem6()
