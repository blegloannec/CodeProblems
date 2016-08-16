#!/usr/bin/env python

from math import sqrt

N,K = 20000000,15000000
L = []

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# multiplicite de p premier dans n!
def fact_multi(n,p):
    cpt = 0
    m = p
    while m<=n:
        cpt += n/m
        m *= p
    return cpt

def decomp(n):
    D = [0 for _ in xrange(len(L))]
    for i in xrange(len(L)):
        if L[i]>n:
            break
        D[i] = fact_multi(n,L[i])
    return D

def main():
    P = sieve(N)
    for i in xrange(N):
        if P[i]:
            L.append(i)
    D1 = decomp(N)
    D2 = decomp(K)
    D3 = decomp(N-K)
    s = 0
    for i in xrange(len(L)):
        s += (D1[i]-D2[i]-D3[i])*L[i]
    print s

main()
