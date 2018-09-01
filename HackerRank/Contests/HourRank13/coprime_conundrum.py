#!/usr/bin/env python

import sys
from math import sqrt

# Methode 1 : f(k) = 2^(a(k)-1) - 1 pour a(k) le nb de facteurs premiers
# distincts de k. On crible pour calculer les a(k) jusqu'a 10^9...
# Un petit peu trop lent et demande trop de memoire (il faudrait cribler
# par intervalles).

# Methode 2 : couples (p < q) avec gcd(p,q) = 1 et pq <= n <= 10^9
# donc p <= sqrt(n) et p+1 <= q <= n/p
# on crible pour decomposer les p <= sqrt(n) et pour chaque p, on calcule
# le nb de q dans [p+1,n/p] par inclusion-exclusion.

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def parmi(n,p,F):
    if p==0:
        yield 1
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1,F):
                yield S*F[i]

# inclusion-exclusion pour compter les A<=q<=B
# premiers avec p dont les facteurs premiers sont F
def coprime(F,A,B):
    if A>B:
        return 0
    cpt = B-A+1
    for k in xrange(1,len(F)+1):
        cpt0 = 0
        for x in parmi(len(F),k,F):
            cpt0 += B/x-(A-1)/x
        cpt += -cpt0 if k%2==1 else cpt0
    return cpt

def main():
    n = int(sys.stdin.readline())
    s = int(sqrt(n))+1
    _,F = sieve_factors(s)
    cpt = 0
    for p in xrange(2,s):
        cpt += coprime(F[p],p+1,n/p)
    print cpt

main()
