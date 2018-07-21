#!/usr/bin/env python

from math import sqrt

# see pb 64 for details on the continued fraction of
# square roots
def step(x,p,q):
    a = int(q/(sqrt(x)-p))
    q = (x-p*p)/q
    p = q*a-p
    return (a,p,q)

def pell(D):
    p,q = int(sqrt(D)), 1
    a = [p] # continued fraction
    h = [0,1] # convergents
    k = [1,0]
    while True:
        h.append(a[-1]*h[-1]+h[-2])
        k.append(a[-1]*k[-1]+k[-2])
        if h[-1]*h[-1]-D*k[-1]*k[-1]==1:
            return(h[-1],k[-1])
        a0,p,q = step(D,p,q)
        a.append(a0)

def is_square(D):
    d = int(sqrt(D))
    return d*d==D
        
def problem66():
    maxx = 0
    maxD = 0
    for D in xrange(2,1001):
        if not is_square(D):
            x,_ = pell(D)
            if x>maxx:
                maxx = x
                maxD = D
    print maxD

problem66()
