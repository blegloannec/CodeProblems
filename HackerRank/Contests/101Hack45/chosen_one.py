#!/usr/bin/env python

import sys
from fractions import gcd

# clearly a solution is given by taking the gcd of
# all number except the chosen one
# to compute the gcd of all numbers except one for
# each chosen one, simply use associativity:
# gcd(A[:i]+A[i+1:]) = gcd(gcd(A[:i]),gcd(A[i+1:]))
# so we only need to pre-compute gcd for prefix/suffix

def main():
    n = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    if n==1:
        print A[0]+1 # e.g.
    else:
        P,S = A[:],A[:]
        for i in xrange(1,n):
            P[i] = gcd(P[i-1],A[i])
        for i in xrange(n-2,-1,-1):
            S[i] = gcd(S[i+1],A[i])
        for i in xrange(n):
            if i==0:
                g = S[i+1]
            elif i==n-1:
                g = P[i-1]
            else:
                g = gcd(P[i-1],S[i+1])
            if A[i]%g!=0:
                print g
                break

main()
