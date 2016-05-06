#!/usr/bin/env python

def pandigitprod(a,b):
    D = [False for _ in xrange(10)]
    D[0] = True
    C = 0
    n = a
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    n = b
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    n = a*b
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    return C==9

def main():
    S = set()
    s = 0
    for i in xrange(1,10):
        for j in xrange(1000,10000):
            if (i*j not in S) and pandigitprod(i,j):
                s += i*j
                S.add(i*j)
    for i in xrange(10,100):
        for j in xrange(100,1000):
            if (i*j not in S) and pandigitprod(i,j):
                s += i*j
                S.add(i*j)
    print s

main()
