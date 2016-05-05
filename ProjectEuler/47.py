#!/usr/bin/env python

from math import sqrt

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def main():
    N = 500000
    M = 4
    P,F = sieve_factors(N)
    for i in xrange(9,N):
        sol = True
        for k in xrange(M):
            if len(F[i-k])!=M:
                sol = False
                break
        if sol:
            print i-M+1
            break

main()
