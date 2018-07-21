#!/usr/bin/env python

from math import sqrt

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def main():
    P = sieve(10000)
    D = {}
    for i in xrange(1000,10000):
        if P[i]:
            sgn = tuple(sorted(list(str(i))))
            if sgn in D:
                D[sgn].append(i)
            else:
                D[sgn] = [i]
    for s in D:
        L = D[s]
        if len(L)<3:
            continue
        for a in xrange(len(L)):
            for b in xrange(a+1,len(L)):
                C = 2*L[b]-L[a]
                if C in L:
                    print L[a],L[b],C

main()
