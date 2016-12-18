#!/usr/bin/env python

import sys
from math import *

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

# crible pour marquer les nb composes L <= n <= R <= 10^12
def prime_int(L,R):
    S = int(sqrt(R))
    D = [True for _ in xrange(R-L+1)]
    for p in P:
        if p>S:
            break
        for n in xrange(max(2,(L+p-1)/p)*p,R+1,p):
            D[n-L] = False
    return D

def main():
    global P
    P = sieve_list(int(sqrt(10**9))+1000)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        L,R = map(int,sys.stdin.readline().split())
        PI = prime_int(L,R+500)
        S = 0
        p0,p1 = None,None
        i = L
        while p1<=R:
            if PI[i-L]:
                p0,p1 = p1,i
                if p0!=None:
                    S += rev_chinois(p0,10**(int(log(p0,10))+1),0,p1)
            i += 1
        print S

main()
