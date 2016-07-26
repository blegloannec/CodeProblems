#!/usr/bin/env python

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def main():
    N = 10**7+1
    _,Factors = sieve_factors(N)
    D = {}
    for n in xrange(2,N):
        if len(Factors[n])==2:
            D[tuple(Factors[n])] = n
    print sum(D[x] for x in D)

main()
