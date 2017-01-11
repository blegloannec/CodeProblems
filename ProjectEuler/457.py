#!/usr/bin/env python

from math import sqrt
import random
random.seed()

# p an odd prime
# P = X^2 - 3X - 1 has at most 2 roots mod p:
# (3 +/- sqrt(13)) / 2
# they exists iff legendre(13,p) = 1 and
# sqrt(13) can be computed by Shanks-Tonelli
# then roots modulo p^2 can be obtained via Hansel's lemma
# https://en.wikipedia.org/wiki/Hensel%27s_lemma
# if r is a root modulo p, the corresponding root modulo p^2
# is given by (r - P(r)*(modular inverse of P'(r) modulo p)) mod p^2

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

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def Q(x):
    return x*x-3*x-1

def Qp(x):
    return 2*x-3

def main():
    N = 10**7+1
    P = sieve(N)
    S = 0
    for p in xrange(3,N,2):
        if P[p] and legendre(13,p)==1:
            r = shanks_tonelli(13,p)
            i2 = inv_mod(2,p)
            a = ((3+r)*i2)%p
            #assert(Q(a)%p==0)
            b = ((3-r)*i2)%p
            #assert(Q(b)%p==0)
            # Hansel lifting of solutions from p to p^2
            p2 = p*p
            lifta = (a - Q(a)*inv_mod(Qp(a),p))%p2;
            #assert(Q(lifta)%p2==0);
            liftb = (b - Q(b)*inv_mod(Qp(b),p))%p2;
            #assert(Q(liftb)%p2==0);
            S += min(lifta,liftb);
    print S

main()
