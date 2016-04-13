#!/usr/bin/env python

from decimal import *
getcontext().prec = 500

# Stupid solution
def period(D):
    d = Decimal(D).sqrt()
    a0 = int(d)
    if a0*a0==D:
        return 0
    d1 = 1/(d-int(d))
    d = 1/(d1-int(d1))
    p = 1
    while (d-d1).copy_abs()>Decimal('1e-250'):
        d = 1/(d-int(d))
        p += 1
    return p
        
def problem64():
    cpt = 0
    for D in xrange(2,10001):
        if period(D)%2==1:
            cpt += 1
    print cpt

problem64()
