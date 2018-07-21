#!/usr/bin/env python

from math import sqrt

# each term is of the form a_i + (sqrt(x)-p_i)/q_i
# a_(i+1) = int( q_i/(sqrt(x)-p_i) ) = int( (sqrt(x)+p_i) / ((x-p_i^2)/q_i) )
# then for q_(i+1) = (x-p_i^2)/q_i the next term is
# a_(i+1) + (sqrt(x)+p_i-a_(i+1)*q_(i+1))/q_(i+1)
# so p_(i+1) = a_(i+1)*q_(i+1)-p_i
def step(x,p,q):
    a = int(q/(sqrt(x)-p))
    q = (x-p*p)/q
    p = q*a-p
    return (a,p,q)
    
def period(D):
    T = {}
    p = int(sqrt(D))
    q = 1
    T[(p,q)] = 0
    _,p,q = step(D,p,q)
    t = 1
    while (p,q) not in T:
        T[(p,q)] = t
        _,p,q = step(D,p,q)
        t += 1
    return t-T[(p,q)]

def is_square(D):
    d = int(sqrt(D))
    return d*d==D
        
def problem64():
    cpt = 0
    for D in xrange(2,10001):
        if not is_square(D) and period(D)%2==1:
            cpt += 1
    print cpt

problem64()
