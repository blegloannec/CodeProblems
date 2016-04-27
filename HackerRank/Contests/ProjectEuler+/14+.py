#!/usr/bin/env python

import sys

def syracuse(n):
    return n/2 if n%2==0 else 3*n+1

Nmax = 5000001
S = [-1 for i in xrange(Nmax)]
M = [-1 for i in xrange(Nmax)]

def aux(s):
    if s>=Nmax:
        return 1+aux(syracuse(s))
    if S[s]<0:
        S[s] = 1+aux(syracuse(s))
    return S[s]
    
def precomp():
    S[1] = 1
    for s in xrange(2,Nmax):
        c = aux(s)
    M[1] = 1
    for s in xrange(2,Nmax):
        M[s] = s if S[s]>=S[M[s-1]] else M[s-1]

def main():
    precomp()
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print M[N]

main()
