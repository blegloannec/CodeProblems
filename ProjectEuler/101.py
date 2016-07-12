#!/usr/bin/env python

from fractions import *

# Interpolation de Lagrange
# les calculs sont faits en rationnels pour la precision
def lagrange(P,x0):
    y0 = Fraction(0)
    for (xi,yi) in P:
        pi = Fraction(yi)
        for (xj,_) in P:
            if xj!=xi:
                pi *= Fraction(x0-xj,xi-xj)
        y0 += pi
    return y0

def U(n):
    return sum((-n)**i for i in xrange(11))

def main():
    P = []
    s = 0
    for i in xrange(1,11):
        P.append((i,U(i)))
        s += int(lagrange(P,i+1))
    print s

main()
