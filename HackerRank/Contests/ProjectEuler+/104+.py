#!/usr/bin/env python

import sys
from decimal import *
getcontext().prec = 50

r5 = Decimal(5).sqrt()
phi1 = (1+r5)/2
phi2 = (1-r5)/2
def F(n):
    return Lambda*(phi1**n) + Mu*(phi2**n)

def digits(n,b=10):
    c = []
    while n>0:
        c.append(int(n%b))
        n /= b
    return c

def pandigital(A,p):
    seen = [(x==0 or x>p) for x in xrange(10)]
    cpt = 0
    for a in A:
        if seen[a]:
            return False
        seen[a] = True
        cpt += 1
    return cpt==p

def main():
    global Lambda,Mu
    f1 = int(sys.stdin.readline())
    f2 = int(sys.stdin.readline())
    f0 = f2-f1
    Lambda = (f1-f0*phi2)/r5
    Mu = f0-Lambda
    p = int(sys.stdin.readline())
    if p==1:
        if f1==1:
            print 1
            return
        if f2==1:
            print 2
            return
    P = 10**p
    k = 2
    while k<=2000000:
        k += 1
        f2,f1 = (f2+f1)%P,f2
        D = digits(f2)
        if pandigital(D,p):
            if pandigital(F(k).as_tuple().digits[:p],p):
                print k
                return
    print 'no solution'

main()
