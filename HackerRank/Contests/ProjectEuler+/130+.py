#!/usr/bin/env python

import sys
from math import sqrt

# A(n) | n-1 <=> n | R(n-1) <=> n | (10^(n-1)-1)/9
#            <=> 9n | 10^(n-1)-1 <=> 10^(n-1) = 1 mod 9n

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
    P = sieve_list(int(sqrt(R))+1)
    D = [True for _ in xrange(R-L+1)]
    for p in P:
        for n in xrange(max(2,(L+p-1)/p)*p,R+1,p):
            D[n-L] = False
    return D

def main():
    L,R = map(int,sys.stdin.readline().split())
    P = prime_int(L,R)
    i = L+int(L%2==0)
    while i<=R:
        if i%5!=0 and not P[i-L] and pow(10,i-1,9*i)==1:
            print i
        i += 2

main()
