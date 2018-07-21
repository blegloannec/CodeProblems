#!/usr/bin/env python

from math import *
from decimal import *
getcontext().prec = 110

# the square root of a non-square is always irrational

def main():
    s = 0
    for n in xrange(2,100):
        r = int(sqrt(n))
        if r*r!=n:
            r = Decimal(n).sqrt()
            d = r.as_tuple().digits
            for i in xrange(100):
                s += d[i]
    print s

main()
