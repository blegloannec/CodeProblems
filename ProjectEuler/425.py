#!/usr/bin/env python

from math import sqrt,log10

# really easy for a 400+ problem
# runs in 2s with pypy

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

N = 10**7
P = sieve(N)
T = [-1 for _ in xrange(N)]

def find(x):
    if T[x]<0:
        return x
    x0 = find(T[x])
    T[x] = x0
    return x0

def union(x,y):
    x0,y0 = find(x),find(y)
    T[y0] = x0

# numbers < x connected to x
def pred(x):
    p = 1
    while p<=x:
        d = (x/p)%10
        for i in xrange(1,d+1):
            y = x-i*p
            if 10*y>=p:
                yield y
        p *= 10

def nb_digits10(n):
    return int(log10(n))+1

def main():
    s = 0
    for p in xrange(3,N):
        if P[p]:
            for q in pred(p):
                if P[q]:
                    if find(q)!=find(p):
                        union(p,q)
            if find(p)!=find(2):
                s += p
    print s

main()
