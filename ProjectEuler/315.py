#!/usr/bin/env python

from math import sqrt

def nb1(n):
    cpt = 0
    while n:
        if n&1:
            cpt += 1
        n >>= 1
    return cpt

D = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x27,0x7f,0x6f]
T = [nb1(D[i]) for i in xrange(10)]
mask = (1<<7)-1
D2D = [[nb1(D[i]^D[j]) for j in xrange(10)] for i in xrange(10)]

def root(n):
    r = 0
    while n>0:
        r += n%10
        n /= 10
    return r

def sam_trans(n):
    cpt = 0
    while n>0:
        cpt += T[n%10]
        n /= 10
    return cpt

def Sam(n):
    res = 2*sam_trans(n)
    n,n0 = root(n),n
    while n!=n0:
        res += 2*sam_trans(n)
        n,n0 = root(n),n
    return res

def max_trans(a,b):
    cpt = 0
    while a>0:
        cpt += D2D[a%10][b%10] if b>0 else T[a%10]
        a /= 10
        b /= 10
    return cpt

def Max(n):
    res = sam_trans(n)
    n,n0 = root(n),n
    while n!=n0:
        res += max_trans(n0,n)
        n,n0 = root(n),n
    res += T[n]
    return res

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def main():
    P = sieve(2*10**7)
    cpt = 0
    for i in xrange(10**7+1,2*10**7,2):
        if P[i]:
            cpt += Sam(i)-Max(i)
    print cpt

main()
