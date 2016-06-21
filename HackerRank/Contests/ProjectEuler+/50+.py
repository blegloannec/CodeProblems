#!/usr/bin/env python

import sys, random
from math import sqrt
from bisect import *
random.seed()

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=30):
    for _ in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

NMAX = 10000000
P = sieve(NMAX)
L = [0,2]

def prime(p):
    return P[p] if p<NMAX else miller_rabin(p)

def main():
    # propagation des sommes des nb premiers
    for i in xrange(3,NMAX,2):
        if P[i]:
            L.append(L[-1]+i)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        # borne sup sur la longeur de la sequence
        l = bisect_left(L,N)
        notfound = True
        while notfound:
            # test de tous les points de depart
            # pour la longueur l
            for i in xrange(len(L)-l):
                if L[i+l]-L[i]>N:
                    break
                if prime(L[i+l]-L[i]):
                    print L[i+l]-L[i],l
                    notfound = False
                    break
            l -= 1

main()
