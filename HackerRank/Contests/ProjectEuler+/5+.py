#!/usr/bin/env python

import sys
from fractions import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

def problem5():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        l = 1
        for i in range(1,N+1):
            l = lcm(l,i)
        print l

problem5()
