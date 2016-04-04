#!/usr/bin/env python

from math import sqrt

def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

NMAX = 1000
cpt = {}
pmax,cmax = 0,0
for a in xrange(1,NMAX/3):
    for b in xrange(a,NMAX):
        if a+2*b>NMAX:
            break
        c2 = a*a+b*b
        if is_sqr(c2):
            c = int(sqrt(c2))
            p = a+b+c
            if p>NMAX:
                break
            if p in cpt:
                cpt[p] += 1
                if cpt[p]>cmax:
                    pmax = p
                    cmax = cpt[p]
            else:
                cpt[p] = 1
     
print pmax
