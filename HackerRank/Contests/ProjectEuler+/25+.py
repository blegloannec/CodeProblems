#!/usr/bin/env python

import sys
from math import *

def main():
    phi = (1+sqrt(5))/2
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print int(ceil((N-1+log10(sqrt(5)))/log10(phi)))

main()
