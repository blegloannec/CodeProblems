#!/usr/bin/env python

import sys
from math import sqrt

def sieve(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Factors[k].append((i,j))
    return P,Factors

def nbdiv(l1,l2):
    nb = 1
    i1,i2 = 0,0
    while i1<len(l1) or i2<len(l2):
        if i2==len(l2) or (i1<len(l1) and l2[i2][0]>l1[i1][0]):
            nb *= l1[i1][1]+1
            i1 += 1
        elif i1==len(l1) or (i2<len(l2) and l2[i2][0]<l1[i1][0]):
            nb *= l2[i2][1]+1
            i2 += 1
        else:
            nb *= l1[i1][1]+l2[i2][1]+1
            i1 += 1
            i2 += 1
    return nb
        
def main():
    _,Factors = sieve(42000)
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        if N==1:
            print 3
            continue
        i = 2
        nb = 2
        while nb<=N:
            i += 1
            if i%2==0:
                nb = nbdiv(Factors[i/2],Factors[i+1])
            else:
                nb = nbdiv(Factors[i],Factors[(i+1)/2])
        print i*(i+1)/2

main()
