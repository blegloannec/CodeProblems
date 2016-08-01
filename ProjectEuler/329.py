#!/usr/bin/env python

from math import sqrt
from fractions import Fraction

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

P = sieve(501)
S = 'PPPPNNPPPNPPNPN'
s = len(S)
Pr = [[-1 for _ in xrange(s)] for _ in xrange(501)]

# Probabilite d'entendre la sequence S[i:] partant
# de la case c
def DP(c,i=0):
    if i==s:
        return 1
    if Pr[c][i]>=0:
        return Pr[c][i]
    if P[c]:
        suiv = Fraction(1,2)*DP(c-1,i+1)+Fraction(1,2)*DP(c+1,i+1)
        res = Fraction(2 if S[i]=='P' else 1,3)*suiv
    else:
        if c==1:
            suiv = DP(c+1,i+1)
        elif c==500:
            suiv = DP(c-1,i+1)
        else:
            suiv = Fraction(1,2)*DP(c-1,i+1)+Fraction(1,2)*DP(c+1,i+1)
        res = Fraction(1 if S[i]=='P' else 2,3)*suiv
    Pr[c][i] = res
    return res

print Fraction(1,500)*sum(DP(c) for c in xrange(1,501))
