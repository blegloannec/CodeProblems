#!/usr/bin/env python

import sys
from math import log10

# continued fraction of sqrt(2):
# a = [1;2,2,2,2,...]

def nb_digits10(n):
    return int(log10(n))+1

def main():
    N = int(sys.stdin.readline())
    h0,h1 = 1,1 # convergents
    k0,k1 = 0,1 # at rank 1 with a_0 = 1
    for i in xrange(N):
        h2 = 2*h1+h0
        k2 = 2*k1+k0
        if nb_digits10(h2)>nb_digits10(k2):
            print i+1
        h1,h0 = h2,h1
        k1,k0 = k2,k1

main()
