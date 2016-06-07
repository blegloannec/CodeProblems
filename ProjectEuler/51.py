#!/usr/bin/env python

from math import *

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def digits(n):
    c = []
    p = [[] for _ in xrange(10)]
    i = 0
    while n>0:
        a = n%10
        c.append(a)
        p[a].append(i)
        n /= 10
        i += 1
    return c,filter((lambda x: x!=[]),p)

def tonum(c):
    res = 0
    for i in xrange(len(c)-1,-1,-1):
        res = 10*res+c[i]
    return res

def main():
    P = sieve(1000000)
    n = 56000
    while True:
        if P[n]:
            c,p = digits(n)
            for l in p:
                c2 = c[:]
                S = set()
                for a in xrange(10):
                    for i in l:
                        c2[i] = a
                    m = tonum(c2)
                    if m<n:
                        continue
                    if P[m]:
                        S.add(m)
                if len(S)>=8:
                    print n
                    return
        n += 1

main()
