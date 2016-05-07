#!/usr/bin/env python

import sys
from math import sqrt

# t = n(n+1)/2
# n^2 + n - 2t = 0
# Given t, D = 1+8t must be a square
# then n = (-1+sqrt(D))/2

def triangular(t):
    D = 1+8*t
    d = int(sqrt(1+8*t))
    if d*d==D:
        return (d-1)/2
    return -1

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        t = int(sys.stdin.readline())
        print triangular(t)

main()
