#!/usr/bin/env python

import sys
from fractions import gcd
from math import sqrt

# consider g = gcd(A) > 1 (by "awesome" hyp)
# for any d | g, d>1, let l = d*(k/d) the largest multiple
# of d to be <= k, then A + l is awesome
# to maximize l, simply minimize d

def main():
    n,k = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    g = reduce(gcd,A)
    if g%2==0:
        print 2*(k/2)
        return
    s = 0
    for d in xrange(3,int(sqrt(g))+1,2):
        if g%d==0:
            s = d*(k/d)
            print s
            return
    # g is prime
    print g*(k/g)

main()
