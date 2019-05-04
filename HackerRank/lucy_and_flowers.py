#!/usr/bin/env pypy2

# O(N^2) approach

P = 10**9+9
inv = lambda x: pow(x,P-2,P)
NMAX = 5001

Binom = [[1]*(n+1) for n in xrange(2*NMAX)]
for n in xrange(1,2*NMAX):
    for k in xrange(1,n):
        Binom[n][k] = (Binom[n-1][k-1] + Binom[n-1][k]) % P

# Catalan numbers for the nb of BST
BST = [(Binom[2*n][n]*inv(n+1)) % P for n in xrange(NMAX)]

if __name__=='__main__':
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        res = 0
        for k in xrange(1,N+1):
            res = (res + Binom[N][k]*BST[k]) % P
        print res
