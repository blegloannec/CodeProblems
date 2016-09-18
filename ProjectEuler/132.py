#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u

# R(n) = (10^n-1)/9
# calcul de R(n)%p pour p =/= 2,3,5
def repumod(n,p):
    return ((pow(10,n,p)-1)*inv_mod(9,p))%p

def main():
    P = eratosthene(1000000)
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
