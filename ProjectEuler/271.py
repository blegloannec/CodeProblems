#!/usr/bin/env python

import itertools
import random
random.seed()

# x^3 = 1 mod n
# x^3-1 = (x-1)(x^2+x+1) = 0 mod n
# if n is prime, there is at most 3 solutions:
# 1 and (-1 +/- sqrt(-3))/2
# sqrt(-3) exists when legendre(n-3,n) = 1
# and can be computed by Shanks-Tonelli
# when n is not prime, use the Chinese Remainder Thm
# here n = 13082761331670030 = 2*3*5*7*11*...*43

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

def legendre(a,p): # p odd prime
    l = pow(a,(p-1)/2,p)
    return -1 if l==p-1 else l

def random_non_residue(p):
    a = random.randint(0,p)
    while legendre(a,p)!=-1:
        a = random.randint(0,p)
    return a

def shanks_tonelli(a,p):
    # p and odd prime, a a quadratic residue
    # we assume legendre(a,p) == 1
    # returns a solution R, the other one will be -R mod p
    # factor p-1 = s*2^e with s odd
    s,e = p-1,0
    while s%2==0:
        s /= 2
        e += 1
    # if e = 1, ie n = p mod 3, the solutions are +/- n^((p+1)/4)
    if e==1:
        return pow(a,(p+1)/4,p)
    # pick a non-residue (randomly, but could start with 2 and try incrementally)
    n = random_non_residue(p)
    x = pow(a,(s+1)/2,p)
    b = pow(a,s,p)
    g = pow(n,s,p)
    r = e
    while True:
        t,m = b,0
        while t!=1:
            t = (t*t)%p
            m += 1
        if m==0:
            return x
        gs = pow(g,1<<(r-m-1),p)
        g = (gs*gs)%p
        x = (x*gs)%p
        b = (b*g)%p
        r = m

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def main():
    Sol = [[1] for _ in xrange(len(P))]
    # on calcule les solutions pour chaque p
    for i in xrange(len(P)):
        p = P[i]
        if legendre(p-3,p)==1:
            r = shanks_tonelli(p-3,p)
            Sol[i].append(((-1+r)*inv_mod(2,p))%p)
            Sol[i].append(((-1-r)*inv_mod(2,p))%p)
    # on recombine par th. chinois pour n
    S = 0
    for X in itertools.product(*Sol):
        a,n = 0,1
        for i in xrange(len(P)):
            a = rev_chinois(a,n,X[i],P[i])
            n *= P[i]
        S += a
    print S-1 # pour retirer la solution 1

main()
