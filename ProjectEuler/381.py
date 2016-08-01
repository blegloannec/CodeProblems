#!/usr/bin/env python

from math import sqrt

# Wilson's theorem:
# (n-1)! = -1 mod p <=> p is prime
# donc pour p premier, (n-k)! = (-1)(n-1)^(-1)...(n-k+1)^(-1) mod p

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u

def main():
    N = 10**8
    P = sieve(N)
    S = 0
    for p in xrange(5,N):
        if P[p]:
            f = p-1
            s = f
            for k in xrange(1,5):
                f = (f*inv_mod(p-k,p))%p
                s = (s+f)%p
            S += s
    print S

main()
