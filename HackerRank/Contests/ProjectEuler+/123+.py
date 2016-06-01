#!/usr/bin/env python

import sys
from math import sqrt
from bisect import *

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def expmod(x,n,p):
    if n==0:
        return 1
    elif n%2==0:
        return expmod((x*x)%p,n/2,p)
    return (x*expmod((x*x)%p,(n-1)/2,p))%p

def main():
    P = sieve(3000000)
    R = [-1]
    n = 1
    for i in xrange(len(P)):
        if P[i]:
            p2 = i*i
            R.append((expmod(i-1,n,p2)+expmod(i+1,n,p2))%p2)
            R[-1] = max(R[-1],R[-2])
            n += 1
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        seuil = int(sys.stdin.readline())
        print bisect_right(R,seuil)

main()
