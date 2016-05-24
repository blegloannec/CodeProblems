#!/usr/bin/env python

import sys

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    #P[0] = False
    #P[1] = False
    for i in xrange(2,N):
        if P[i]:
            #Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def main():
    N,M = map(int,sys.stdin.readline().split())
    _,F = sieve_factors(N+M+1)
    for i in xrange(2,N+1):
        sol = True
        for k in xrange(M):
            if len(F[i+k])!=M:
                sol = False
                break
        if sol:
            print i

main()
