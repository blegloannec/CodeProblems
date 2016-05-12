#!/usr/bin/env python

import sys
from math import *
from decimal import *

# the square root of a non-square is always irrational

def main():
    N = int(sys.stdin.readline())
    P = int(sys.stdin.readline())
    getcontext().prec = P+10
    s = 0
    for n in xrange(2,N+1):
        r = int(sqrt(n))
        if r*r!=n:
            r = Decimal(n).sqrt()
            d = r.as_tuple().digits
            for i in xrange(P):
                s += d[i]
    print s

main()
