#!/usr/bin/env python

from math import sqrt

def somme_diviseurs(n):
    if n==1:
        return 1
    s = 1
    r = int(sqrt(n))
    if r*r==n:
        s += r
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += i+n/i
    return s

def problem21():
    n = 10000
    sumdivs = map(somme_diviseurs,range(3*n))
    s = 0
    for a in xrange(2,n+1):
        if a!=sumdivs[a] and sumdivs[sumdivs[a]]==a:
            s += a
    print s

problem21()
