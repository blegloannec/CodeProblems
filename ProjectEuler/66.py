#!/usr/bin/env python

from math import sqrt
from decimal import *
getcontext().prec = 200

def pell(D):
    d = Decimal(D).sqrt()
    a = [] # continued fraction
    h = [0,1] # convergents
    k = [1,0]
    while True:
        a.append(int(d))
        d = 1/(d-a[-1])
        h.append(a[-1]*h[-1]+h[-2])
        k.append(a[-1]*k[-1]+k[-2])
        if h[-1]*h[-1]-D*k[-1]*k[-1]==1:
            return(h[-1],k[-1])

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
