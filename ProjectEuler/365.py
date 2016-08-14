#!/usr/bin/env python

from math import sqrt

# On utilise le thm de Lucas pour calculer la valeur
# du coeff modulo chaque nb premier entre 1000 et 5000
# Puis pour chaque triplet de premiers p<q<r on reconstruit
# la valeur modulo p*q*r par thm chinois

N,K = 10**18,10**9

def binom(n,p):
    if p>n:
        return 0
    return 1 if p==0 else n*binom(n-1,p-1)/p

# Thm de Lucas
def lucas_binom(n,k,p):
    res = 1
    while n>0:
        res = (res*binom(n%p,k%p))%p
        n /= p
        k /= p
    return res

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>1000),l)

P = eratosthene(5000)
B = map((lambda p: lucas_binom(N,K,p)),P)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def M(ip,iq,ir):
    x = rev_chinois(B[ip],P[ip],B[iq],P[iq])
    return rev_chinois(x,P[ip]*P[iq],B[ir],P[ir])

def main():
    s = 0
    for ip in xrange(len(P)):
        for iq in xrange(ip+1,len(P)):
            for ir in xrange(iq+1,len(P)):
                s += M(ip,iq,ir)
    print s

main()
