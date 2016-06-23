#!/usr/bin/env python

from decimal import *
getcontext().prec = 15

P = 10**9

r5 = Decimal(5).sqrt()
phi1 = (1+r5)/2
phi2 = (1-r5)/2
def F(n):
    return (phi1**n - phi2**n)/r5

def digits(n,b=10):
    c = []
    while n>0:
        c.append(int(n%b))
        n /= b
    return c

def pandigital(A):
    seen = [False for _ in xrange(10)]
    seen[0] = True
    cpt = 0
    for a in A:
        if seen[a]:
            return False
        seen[a] = True
        cpt += 1
    return cpt==9

def main():
    f1,f2 = 1,1
    k = 2
    while True:
        k += 1
        f2,f1 = (f2+f1)%P,f2
        D = digits(f2)
        if pandigital(D):
            if pandigital(F(k).as_tuple().digits[:9]):
                print k
                break

main()
