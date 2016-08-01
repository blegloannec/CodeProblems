#!/usr/bin/env python

from math import sqrt

# si n = p1^a1...pk^ak (prime decomposition)
# alors s(n) = max( s(pi^ai), i=1..k )
# on crible pour le resultat
# lent (~60s avec pypy) et gourmand en memoire

# NB (non utilise) : si p premier <=n, p apparait dans la decomp de n!
# a la puissance sum( int(n/p^i), i>0 )

def s(M):
    f = 1
    i = 1
    while f!=0:
        f = (f*i)%M
        i += 1
    return i-1

def sieve_div_fact(N):
    P = [True for _ in xrange(N)]
    S = [0 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            S[i] = i
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                m = i
                while l%i==0:
                    l /= i
                    m *= i
                if l==1: # k puissance de i
                    S[k] = s(m) # alors calcul naif
                else:
                    S[k] = max(S[k],S[m])
    return P,S

def main():
    _,S = sieve_div_fact(10**8+1)
    print sum(S)

main()
