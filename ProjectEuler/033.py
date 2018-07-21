#!/usr/bin/env python

from fractions import Fraction

def problem33():
    l = []
    for p in range(1,9):
        for q in range(p+1,10):
            for a in range(1,10):
                pp = 10*a+p
                qq = 10*q+a
                if pp*q==qq*p:
                    l.append((pp,qq))
                pp = 10*p+a
                qq = 10*a+q
                if pp*q==qq*p:
                    l.append((pp,qq))
    print l
    r = 1
    for c in l:
        r *= Fraction(c[0],c[1])
    print r

problem33()
