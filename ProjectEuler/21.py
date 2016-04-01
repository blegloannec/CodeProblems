#!/usr/bin/env python

from math import sqrt

def somme_diviseurs(n):
    s = 1
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            s += i+n/i
    return s

def problem21():
    n = 10000
    nbs = range(2,n+1)
    sumdivs = map(somme_diviseurs,range(3*n))
    s = 0
    for a in nbs:
        if a!=sumdivs[a] and sumdivs[sumdivs[a]]==a:
            s += a
    print s

problem21()
