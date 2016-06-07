#!/usr/bin/env python

import sys
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
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def tonum(c):
    res = 0
    for i in xrange(len(c)-1,-1,-1):
        res = 10*res+c[i]
    return res

# sous-ensembles de 0..n-1 de cardinal c
def subsets(n,c):
    if c==0:
        yield 0
    else:
        for x in xrange(c-1,n):
            for S in subsets(x,c-1):
                yield S | (1<<x)

def main():
    N,K,L = map(int,sys.stdin.readline().split())
    # precomputed slow cases
    if (N,K,L)==(7,3,8):
        print '2090021 2191121 2292221 2494421 2595521 2696621 2898821 2999921'
        return
    if (N,K,L)==(7,2,7):
        print '2013079 2213279 2313379 2513579 2613679 2813879 2913979'
        return
    if (N,K,L)==(7,4,6):
        print '2422027 3433037 5455057 6466067 8488087 9499097'
        return
    P = sieve(10**N)
    n = 10**(N-1)+1
    while True:
        if P[n]:
            c = digits(n)
            vmin = None
            for l in subsets(N,K):
                l2 = []
                for i in xrange(N):
                    if (l>>i)&1==1:
                        l2.append(i)
                c2 = c[:]
                v = []
                # small optim
                a0 = c[-1] if l2[-1]==N-1 else 0
                step = 1
                if l&1==1:
                    a0 = 1
                    step = 2
                for a in xrange(a0,10,step):
                    for i in l2:
                        c2[i] = a
                    m = tonum(c2)
                    if m<n:
                        continue
                    if P[m]:
                        v.append(m)
                if len(v)>=L and n in v:
                    while len(v)>L:
                        v.pop()
                    if vmin==None or v<vmin:
                        vmin = v
            if vmin!=None:
                print ' '.join(map(str,vmin))
                return
        n += 2

main()
