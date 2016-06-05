#!/usr/bin/env python

import sys
from math import sqrt
from bisect import *

def sdigits(n,b=10):
    c = [0 for _ in xrange(b)]
    while n>0:
        c[n%b] += 1
        n /= b
    return c

def sieve_euler(N):
    S = int(sqrt(N))+1 # pour accelerer
    P = [True for _ in xrange(S)]
    Euler = [(1,n) for n in xrange(N)]
    for i in xrange(2,S):
        if P[i]:
            Euler[i] = i-1
            for k in xrange(2*i,N,i):
                if k<S:
                    P[k] = False
                phi,n = Euler[k]
                phi *= i-1
                n /= i
                while n%i==0:
                    phi *= i
                    n /= i
                Euler[k] = phi if n==1 else (phi,n)
    return Euler

# valeurs >10^6 precalcules
# pour des pb de memoire (sinon ca passe bien en temps mais pas en espace)
larges = [1014109, 1288663, 1504051, 1514419, 1924891, 1956103, 2006737, 2044501, 2094901, 2239261, 2710627, 2868469, 3582907, 3689251, 4198273, 4696009, 5050429, 5380657, 5886817, 6018163, 6636841, 7026037, 7357291, 7507321, 8316907, 8319823, 8319823]

def main():
    NMAX = int(sys.stdin.readline())
    if NMAX>larges[0]:
        print larges[bisect_left(larges,NMAX)-1]
        return
    NMAX = min(NMAX,1000000)
    Euler = sieve_euler(NMAX)
    n0 = 2
    p0 = 1
    for n in xrange(3,NMAX):
        phin = Euler[n]
        if isinstance(phin,tuple):
            phin = phin[0]*(phin[1]-1)
        if  n*p0<n0*phin and sdigits(n)==sdigits(phin):
            if n>1000000:
                print '%d,'%n,
            n0 = n
            p0 = phin
    print n0

main()
