#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

P = eratosthene(1000000)

# comportement de la suite 10^n mod p
# attention: comportement special pour 2 et 5
def periode(p):
    T = [-1 for _ in xrange(p)]
    S = [0]
    n = 1
    t = 0
    while T[n]<0:
        T[n] = t
        S.append((S[-1]+n)%p)
        t += 1
        n = (10*n)%p
    #return T[n],t-T[n]
    return S

# R(n) = sum( 10^k, k<n )
# calcul de R(n)%p pour p =/= 2 ou 5
def repumod(n,p):
    S = periode(p)
    l = len(S)-1
    return ((n/l)*S[-1]+S[n%l])%p

def main():
    N = 10**9
    cpt = 0
    s = 0
    i = 3 # on commence a 7
    # le reste est 1 pour 2 et 5
    # et 10**9 n'est pas multiple de 3
    while cpt<40:
        if repumod(N,P[i])==0:
            s += P[i]
            cpt += 1
        i += 1
    print s

main()
