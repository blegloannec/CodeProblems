#!/usr/bin/env python

from math import *

# Prenons l'exemple de 19,23
# on cherche n tel que n = 19 mod 100
# et n = 0 mod 23
# comme 100 et 23 sont p-e-e, on peut calculer la solution
# (unique modulo 2300) par inversion du thm chinois
# (et on pourra toujours sauf pour 3 et 5 car 5 et 10
#  ne sont pas p-e-e)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def main():
    P = eratosthene(1000005)
    S = 0
    for i in xrange(2,len(P)-1):
        S += rev_chinois(P[i],10**(int(log(P[i],10))+1),0,P[i+1])
    print S

main()
