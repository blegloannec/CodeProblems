#!/usr/bin/env python

from fractions import gcd
from math import sqrt

# https://en.wikipedia.org/wiki/Pick%27s_theorem
# 2*i = 2*A + 2 - b
# calcul du nombre de points sur la bordure :
# droite y = b(a-x)/a, 0<=x<=a
# valeurs entieres pour X = a-x, 0<=X<=a, multiple de a/gcd(a,b)
# soit a/(a/gcd(a,b)) + 1 = gcd(a,b) + 1 points sur la droite

def pick(a,b,c,d):
    A2 = a*b+b*c+c*d+d*a
    b = gcd(a,b)+gcd(b,c)+gcd(c,d)+gcd(d,a)
    return (A2+2-b)/2

def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

def main():
    m = 100
    cpt = 0
    for a in xrange(1,m+1):
        for b in xrange(1,m+1):
            for c in xrange(1,m+1):
                for d in xrange(1,m+1):
                    if is_sqr(pick(a,b,c,d)):
                        cpt += 1
    print cpt

main()
