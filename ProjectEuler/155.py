#!/usr/bin/env python

import sys
from fractions import *

# https://oeis.org/A153588
# related to https://oeis.org/A048211 (seq for exactly n)

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
                #R.add(1/(1/a+1/b))
                R.add(Fraction(a.numerator*b.numerator,a.denominator*b.numerator+b.denominator*a.numerator))
    memo[n] = R
    return R

# takes slightly more than a minute
S = set()
for i in xrange(1,19):
    S |= capa(i)
    print i,len(S)
