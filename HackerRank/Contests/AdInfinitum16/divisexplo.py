#!/usr/bin/env python

import sys

M = 10**9 + 7

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
    D = int(sys.stdin.readline())
    Fact = [1,1]
    InvFact = [1,1]
    for i in xrange(2,200003):
        Fact.append((Fact[-1]*i)%M)
        InvFact.append(inv_mod(Fact[-1],M))
    for _ in xrange(D):
        m,a = map(int,sys.stdin.readline().split())
        inv2m = pow(InvFact[2],m,M)
        print (Fact[a+m+1]*Fact[a+m+2]*InvFact[a+1]*InvFact[a+2]*inv2m)%M

main()
