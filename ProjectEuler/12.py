#!/usr/bin/env python

from math import sqrt

def nb_diviseurs(n): # for n>1
    s = 2
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += 1
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += 2
    return s

def problem12():
    n = 1
    nb = 3
    while nb_diviseurs(nb)<500:
        n += 1
        nb = n*(n+1)/2
    print nb

problem12()
