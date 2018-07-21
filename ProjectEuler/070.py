#!/usr/bin/env python

from math import sqrt

def sdigits(n,b=10):
    c = [0 for _ in xrange(10)]
    while n>0:
        c[n%b] += 1
        n /= b
    return c

def sieve_euler(N):
    P = [True for _ in xrange(N)]
    Euler = [[1,n] for n in xrange(N)]
    P[0] = False
    P[1] = False
    S = int(sqrt(N))+1 # pour accelerer
    for i in xrange(2,S):
        if P[i]:
            Euler[i][0] = i-1
            Euler[i][1] = 1
            for k in xrange(2*i,N,i):
                P[k] = False
                Euler[k][0] *= i-1
                Euler[k][1] /= i
                while Euler[k][1]%i==0:
                    Euler[k][0] *= i
                    Euler[k][1] /= i
    return P,Euler

def main():
    NMAX = 10000000
    _,Euler = sieve_euler(NMAX)
    n0 = 2
    p0 = 1
    for n in xrange(3,NMAX):
        phin = Euler[n][0]
        if Euler[n][1]>1:
            phin *= Euler[n][1]-1
        if  n*p0<n0*phin and sdigits(n)==sdigits(phin):
            n0 = n
            p0 = phin
    print n0

main()
