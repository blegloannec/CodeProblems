#!/usr/bin/env python

import sys
from math import sqrt
from collections import defaultdict

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def sgn(n):
    c = [0 for _ in xrange(10)]
    i = 0
    while n>0:
        c[n%10] += 1
        n /= 10
        i += 1
    return (i,tuple(c))

def main():
    NMAX = 1000000
    N,K = map(int,sys.stdin.readline().split())
    P = sieve(NMAX)
    D = defaultdict(list)
    for i in xrange(1001,NMAX,2):
        if P[i]:
            D[sgn(i)].append(i)
    Sol = []
    for s in D:
        L = D[s]
        if len(L)<K:
            continue
        if K==3:
            for a in xrange(len(L)):
                if L[a]>=N:
                    break
                for b in xrange(a+1,len(L)):
                    c = 2*L[b]-L[a]
                    if c in L:
                        Sol.append(int('%d%d%d' % (L[a],L[b],c)))
        else:
            for a in xrange(len(L)):
                if L[a]>=N:
                    break
                for b in xrange(a+1,len(L)):
                    c = 2*L[b]-L[a]
                    d = 3*L[b]-2*L[a]
                    if c in L and d in L:
                        Sol.append(int('%d%d%d%d' % (L[a],L[b],c,d)))
    Sol.sort()
    for x in Sol:
        print x

main()
