#!/usr/bin/env python

import sys
from math import *

def S(n,P):
    s = 0
    while n>0:
        s += P[n%10]
        n /= 10
    return s

def main():
    N = int(sys.stdin.readline())
    # S(n) <= 9^N log10(n)
    P = [i**N for i in xrange(10)]
    K = P[9]
    s = 0
    i = 2
    while i<K*ceil(log10(i)):
        if S(i,N)==i:
            s += i
        i += 1
    print s

main()
