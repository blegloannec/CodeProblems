#!/usr/bin/env python

import sys
from math import log10

# n = int(log10(x^n))+1 = int(n*log10(x))+1
# donc log10(x)<=1 donc x<=9

def main():
    n = int(sys.stdin.readline())
    for x in xrange(1,10):
        if int(n*log10(x))==n-1:
            print x**n

main()
