#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def gen(N,P,i=0,n=1):
    if i==len(P):
        yield n
    else:
        while n<=N:
            for m in gen(N,P,i+1,n):
                yield m
            n *= P[i]

def main():
    N = 10**9
    T = 100
    P = eratosthene(T)
    print len(list(gen(N,P)))

main()
