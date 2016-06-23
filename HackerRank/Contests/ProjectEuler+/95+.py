#!/usr/bin/env python

import sys

def sieve(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Factors[k].append((i,j))
    return P,Factors

# generateur des diviseurs (inutile ici)
def divisors(F,i=0):
    if i==len(F):
        yield 1
    else:
        p,m = F[i]
        f = 1
        for _ in xrange(m+1):
            for d in divisors(F,i+1):
                yield f*d
            f *= p

# si s est la somme des diviseurs de n
# la somme des diviseurs de m = n*p^a
# est sum( s*p^k, k=0..a ) = s * (p^(a+1)-1)/(p-1)
def sum_divisors(F,i=0):
    if i==len(F):
        return 1
    p,a = F[i]
    return sum_divisors(F,i+1)*(p**(a+1)-1)/(p-1)

def visit(n,t=0):
    if n>=NMAX or L[n]!=None:
        return t+1,0
    if Time[n]>=0:
        return Time[n],t-Time[n]
    Time[n] = t
    t0,l0 = visit(Succ[n],t+1)
    if t>=t0:
        L[n] = l0
    else:
        L[n] = 0
    return t0,l0
    
def main():
    global NMAX,Succ,Time,L
    NMAX = int(sys.stdin.readline())+1
    _,Factor = sieve(NMAX)
    Succ = [0 for _ in xrange(NMAX)]
    Time = [-1 for _ in xrange(NMAX)]
    L = [None for _ in xrange(NMAX)]
    for n in xrange(2,NMAX):
        Succ[n] = sum_divisors(Factor[n])-n
    maxl = 0
    for n in xrange(2,NMAX):
        if L[n]==None:
            visit(n)
        if L[n]>maxl:
            maxl = L[n]
            maxn = n
    print maxn

main()
