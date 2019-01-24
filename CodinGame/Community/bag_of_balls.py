#!/usr/bin/env python3

from fractions import gcd

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

N = int(input())
W = int(input())
s = int(input())
k = int(input())

A = binom(W,k)*binom(N-W,s-k)
B = binom(N,s)-A
g = gcd(A,B)
print('%d:%d' % (A//g,B//g))
