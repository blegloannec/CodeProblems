#!/usr/bin/env python

import sys
from math import sqrt

def premier(n):
    if n<2 or n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def eratosthene(n):
    l = range(2,n+1)
    for i in xrange(2,int(sqrt(n))+1):
        k = 2
        while k*i<=n:
            l[k*i-2] = -1
            k += 1
    return filter((lambda(x):x>0),l)

def main():
    N = int(sys.stdin.readline())
    nmax = 0
    B = eratosthene(N)
    for a in range(-N,N+1):
        for b in B:
            n = 1
            while premier(n*n+a*n+b):
                n += 1
            if n>nmax:
                nmax = n
                amax,bmax = a,b
    print amax,bmax

main()
