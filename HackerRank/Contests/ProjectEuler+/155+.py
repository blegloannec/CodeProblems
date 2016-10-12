#!/usr/bin/env python

import sys
from fractions import *

memo = {0:set(), 1:set([Fraction(1)])}
def capa(n):
    if n in memo:
        return memo[n]
    R = set()
    for i in xrange(1,n/2+1):
        A = capa(i)
        B = capa(n-i)
        for a in A:
            for b in B:
                R.add(a+b)
                R.add(Fraction(a.numerator*b.numerator,a.denominator*b.numerator+b.denominator*a.numerator))
    memo[n] = R
    return R

def precomp():
    res = [0]
    S = set()
    for i in xrange(1,19):
        S |= capa(i)
        res.append(len(S))
    print res

def main():
    V = [0, 1, 3, 7, 15, 35, 77, 179, 429, 1039, 2525, 6235, 15463, 38513, 96231, 241519, 607339, 1529533, 3857447]
    n = int(sys.stdin.readline())
    print V[n]

main()
