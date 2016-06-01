#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def expmod(x,n,p):
    if n==0:
        return 1
    elif n%2==0:
        return expmod((x*x)%p,n/2,p)
    return (x*expmod((x*x)%p,(n-1)/2,p))%p

def main():
    P = eratosthene(1000000)
    seuil = 10**10
    for i in xrange(len(P)):
        p2 = P[i]*P[i]
        if (expmod(P[i]-1,i+1,p2)+expmod(P[i]+1,i+1,p2))%p2>seuil:
            print i+1
            return

main()
