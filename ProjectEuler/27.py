#!/usr/bin/env python

from math import sqrt

def premier(n):
    if n<0 or n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        k = 2
        while k*i<=n:
            l[k*i-2] = -1
            k += 1
    return filter((lambda(x):x>0),l)

def problem27():
    nmax = 0
    B = eratosthene(999)
    for a in range(-999,1000):
        for b in B:
            n = 1
            while premier(n*n+a*n+b):
                n += 1
            if n>nmax:
                nmax = n
                amax,bmax = a,b
    print nmax, amax, bmax, amax*bmax

problem27()
