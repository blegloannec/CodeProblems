#!/usr/bin/env python

from math import *
import random
random.seed()

# Quite slow (~2 min with pypy)...

N = 10000

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def size(n):
    return int(log(n,10))+1

def compat(x1,x2):
    return (prime(x1*10**size(x2)+x2) and prime(x2*10**size(x1)+x1))

def scompat(S1,S2):
    for x1 in S1:
        for x2 in S2:
            if not compat(x1,x2):
                return False
    return True

def next(Sets1,Sets2):
    Sets1 = sorted(Sets1,key=(lambda x: x[-1]))
    Sets2 = sorted(Sets2,key=(lambda x: x[0]),reverse=True)
    T = []
    for S1 in Sets1:
        for S2 in Sets2:
            if S1[-1]>=S2[0]:
                break
            if scompat(S1,S2):
                T.append(S1+S2)
    return T

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

def prime(p):
    return P[p] if p<N else miller_rabin(p)

def main():
    global P
    P = sieve(N)
    S1 = []
    for i in xrange(2,N):
        if P[i]:
            S1.append([i])
    S2 = next(S1,S1)
    S3 = next(S1,S2)
    S5 = next(S2,S3)
    m = float('inf')
    for s in S5:
        m = min(m,sum(s))
    print m

main()
