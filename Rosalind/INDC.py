#!/usr/bin/env python3

from math import log10

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

n = int(input())
P = [binom(2*n,k)/2**(2*n) for k in range(1,2*n+1)]
for i in range(len(P)-2,-1,-1):
    P[i] += P[i+1]
print(' '.join(str(log10(p)) for p in P))
