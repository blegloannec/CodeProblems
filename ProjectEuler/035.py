#!/usr/bin/env python

from math import sqrt,log10

N = 1000000
P = [True for _ in xrange(N)]

def sieve(N):
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False

def rotate(n):
    l = int(log10(n))
    c = n%10
    return n/10+c*(10**l)
                
def main():
    sieve(N)
    cpt = 0
    for p in xrange(2,N):
        if P[p]:
            P[p] = False
            pcpt = 1
            q = rotate(p)
            while q!=p:
                if not P[q]:
                    break
                pcpt += 1
                P[q] = False
                q = rotate(q)
            if q==p:
                cpt += pcpt
    print cpt

main()
