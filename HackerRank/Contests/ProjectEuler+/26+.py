#!/usr/bin/env python

import sys

# le developpement est soit periodique soit fini
# il est fini ssi n divise une puissance de 10
# i.e. n = 2^k * 5^l (auquel cas n | 10^max(k,l))
# sinon 1/n est ultimement periodique :
# pour la fraction p/q avec p<q, on considere
# la DE 10*p = a*q + r et on recommence avec
# la fraction r/q, jusqu'a retomber sur un r deja
# rencontre, alors on boucle...
     
def dev_fini(n):
    while n%2==0:
        n /= 2
    while n%5==0:
        n /= 5
    return n==1

def period(n):
    t = [-1 for i in range(n)]
    r = 1
    i = 0
    while t[r]<0:
        t[r] = i
        i += 1
        r = (10*r)%n
    return i-t[r]

def main():
    NMAX = 10001
    P = [0 for _ in xrange(NMAX)]
    Nmax = [0 for _ in xrange(NMAX)]
    for n in xrange(2,NMAX):
        Nmax[n] = Nmax[n-1]
        if not dev_fini(n):
            P[n] = period(n)
            if P[n]>P[Nmax[n]]:
                Nmax[n] = n
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print Nmax[N-1]

main()
