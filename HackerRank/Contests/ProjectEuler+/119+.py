#!/usr/bin/env python

import sys
from math import *

def digits_sum(n,b):
    s = 0
    while n>0:
        s += n%b
        n /= b
    return s

def main():
    B = int(sys.stdin.readline())
    G = 10**100
    S = (B-1)*(int(log(G,B))+1)
    L = []
    for a in xrange(2,S+1):
        x = a*a
        while x<G:
            if digits_sum(x,B)==a:
                L.append(x)
            x *= a
    L.sort()
    print ' '.join(map(str,L))

main()
