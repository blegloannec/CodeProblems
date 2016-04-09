#!/usr/bin/env python

from math import sqrt

# t = n(n+1)/2
# n^2 + n - 2t = 0
# Given t, D = 1+8t must be a square
# then n = (-1+sqrt(D))/2

def is_triang(t):
    D = 1+8*t
    d = int(sqrt(1+8*t))
    return d*d==D

# p = n(3n-1)/2
# 3n^2 - n - 2p = 0
# D = 1+24p
# et n = (1+sqrt(D))/6
# mais les solutions pour n<0 ont n = (1-sqrt(D))/6
# dans ce cas (1-sqrt(D))%6 == 0
# donc (1+sqrt(D))%6 == 2 != 0

def is_penta(p):
    D = 1+24*p
    d = int(sqrt(D))
    return (d*d==D and (1+d)%6==0)

def main():
    n = 144
    while True:
        h = n*(2*n-1)
        if is_triang(h) and is_penta(h):
            break
        n += 1
    print h

main()
