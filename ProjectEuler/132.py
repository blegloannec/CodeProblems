#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def main():
    P = eratosthene(1000000)
    N = 10**9
    cpt = 0
    s = 0
    i = 0
    while cpt<40:
        # R(n) = (10^n-1)/9
        # p | R(n) <=> p | (10^n-1)/9 <=> 9p | 10^n-1 <=> 10^n = 1 mod 9p
        if pow(10,N,9*P[i])==1:
            s += P[i]
            cpt += 1
        i += 1
    print s

main()
