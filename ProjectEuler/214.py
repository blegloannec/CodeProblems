#!/usr/bin/env python

def sieve_totient(N):
    P = [True for _ in xrange(N)]
    Totient = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Totient[i] = i-1
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m *= i
                Totient[k] *= (i-1)*m
    return P,Totient

def chain(T,p):
    l = 1
    while T[p]!=1:
        p = T[p]
        l += 1
    return l+1

def main():
    N = 4*10**7
    P,T = sieve_totient(N)
    s = 0
    for i in xrange(3,N,2):
        if P[i]:
            if chain(T,i)==25:
                s += i
    print s
    
main()
