#!/usr/bin/env python

import sys
from math import *

# Trouver les solutions x^k = n [p], p premier >=3, n=/=0
# (Zp)* monogene d'ordre p-1
# On commence par trouver un generateur g de (Zp)*
# On pre-calcule le log discret du meme coup
# L'equation en x = g^a devient g^(ak) = g^m [p]
# Soit ak = m [p-1]
# 1. Cela admet une solution ssi d = pgcd(k,p-1) divise m = dm'
#    Bezout : uk + v(p-1) = d
#    D'ou (um')k = m [p-1]  (um' solution particuliere)
# 2. Si a,b sont solutions (a-b)k = 0 [p-1]
#    On deduit la solution generale en resolvant ak = 0 [p-1]
#    Solutions a = t(p-1)/d pour t=0..(d-1)
# Solution generale : um' + t(p-1)/d pour t=0..(d-1)

def generator(p):
    for i in xrange(2,p):
        o = 1
        x = i
        while x!=1:
            x = (x*i)%p
            o += 1
        if o>(p-1)/2: # ordre>(p-1)/2 => ordre p-1
            return i

def dlog_precomp(g,p):
    LOG = {}
    LOG[1] = 0
    LOG[g] = 1
    x = g*g
    o = 2
    while x!=1:
        LOG[x] = o
        x = (x*g)%p
        o += 1
    return LOG

# inversion modulo par euclide etendu
# (coeff de bezout)
def bezout(a,b):
    if b==0:
        return (a,1,0)
    gcd,u,v = bezout(b,a%b)
    return (gcd,v,u-(a/b)*v)

def expmod(x,n,p):
    if n==0:
        return 1
    if n%2==0:
        return expmod((x*x)%p,n/2,p)
    return (x*expmod((x*x)%p,n/2,p))%p


def main():
    p,Q = map(int,sys.stdin.readline().split())
    if p==2: # cas particulier de p=2
        for t in xrange(Q):
            k,n = map(int,sys.stdin.readline().split())
            print n%2
        return
    g = generator(p)
    LOG = dlog_precomp(g,p)
    for t in xrange(Q):
        k,n = map(int,sys.stdin.readline().split())
        if n%p==0: # cas particulier de n=0
            print '0'
            continue
        m = LOG[n%p]
        d,u,v = bezout(k,p-1)
        if m%d!=0:
            print 'NONE'
            continue
        a = (u*m/d)%(p-1)
        ga = expmod(g,a+t*(p-1)/d,p)
        s0 = expmod(g,(p-1)/d,p)
        sol = [ga]
        for t in range(1,d):
            sol.append((sol[-1]*s0)%p)
        print ' '.join(map(str,sorted(sol)))

main()
