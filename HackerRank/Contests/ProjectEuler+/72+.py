#!/usr/bin/env python

import sys
from math import sqrt

# https://en.wikipedia.org/wiki/Farey_sequence
# la taille de la sequence est la somme des indicatrices
# d'Euler

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    S = int(sqrt(N))+1 # pour accelerer
    for i in xrange(2,S):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

def expo(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return expo(x*x,n/2)
    return x*expo(x*x,(n-1)/2)

def eulerphi(n,decomp): # decomp potentiellement partielle
    res = 1
    for (p,m) in decomp:
        f = expo(p,m-1)
        n /= f*p
        res *= (p-1)*f
    if n>1: # dernier facteur manquant
        res *= n-1
    return res

def main():
    NMAX = 1000001
    _,D = sieve_decomp(NMAX)
    S = [0 for _ in xrange(NMAX)]
    for n in xrange(1,NMAX):
        S[n] = S[n-1]+eulerphi(n,D[n])
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print S[N]-1 # -1 car la fraction 0 ne compte pas

main()
