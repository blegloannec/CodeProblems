#!/usr/bin/env python

from math import sqrt

def sieve_sqr_div_sum(N):
    P = [True for _ in xrange(N)]
    SqrDivSum = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            SqrDivSum[i] += i*i
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k
                S = SqrDivSum[k]
                while l%i==0:
                    l /= i
                    m *= i
                    SqrDivSum[k] += S*m*m
    return P,SqrDivSum

def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

def main():
    N = 64000000
    _,S = sieve_sqr_div_sum(64000000)
    res = 0
    for i in xrange(1,N):
        if is_sqr(S[i]):
            res += i
    print res

main()
