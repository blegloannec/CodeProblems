#!/usr/bin/env python

import sys

def sumdiv(NMAX):
    S = [1 for i in xrange(NMAX)]
    for i in xrange(2,NMAX):
        for j in xrange(2*i,NMAX,i):
            S[j] += i
    return S

def main():
    Nmax = 100001
    D = sumdiv(5*Nmax) # marge indispensable
    # l'un des elements de la paire peut depasser Nmax
    S = [0 for i in xrange(Nmax)]
    for a in xrange(1,Nmax):
        S[a] = S[a-1]
        if a!=D[a] and D[D[a]]==a:
            S[a] += a
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print S[N]

main()
