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
    N = 1000000
    P = sieve(N)
    L = []
    maxl = 0
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
    for i in xrange(len(L)):
        j = 1
        s = L[i]
        while i+j<len(L):
            s += L[i+j]
            if s>=N:
                break
            if P[s] and j+1>maxl:
                maxl = j+1
                maxs = s
            j += 1
    print maxs

main()
