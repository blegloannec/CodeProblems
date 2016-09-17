#!/usr/bin/env python

from math import sqrt

# kinda naive approach as for pb 129, runs in 0.2s

def A(k):
    r = 1
    a = 1
    while r!=0:
        r = (10*r+1)%k
        a += 1
    return a

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
    P = sieve(100000)
    cpt = 0
    s = 0
    i = 91
    while cpt<25:
        if not P[i] and i%5!=0 and (i-1)%A(i)==0:
            s += i
            cpt += 1
        i += 2
    print s

main()
