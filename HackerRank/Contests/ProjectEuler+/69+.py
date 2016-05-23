#!/usr/bin/env python

import sys
from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

# n/phi(n) = Prod( p/(p-1), p facteur premier de n)
# est maximise lorsqu'il y a un maximum de facteurs premiers distincts
# (la multiplicite ne joue pas) et qu'ils sont les plus petits possibles
# (ainsi les p/(p-1) sont les plus grands possibles)
# la solution est donc le plus grand produit 2*3*5*7*11*... inferieur a N

def main():
    P = eratosthene(100)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        n = 1
        for p in P:
            n *= p
            if n>=N:
                n /= p
                break
        print n

main()
