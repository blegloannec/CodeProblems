#!/usr/bin/env python

from math import sqrt

# runs in almost 9 min with pypy :/
# must have missed something here...

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# crible pour decomposer les nb L <= n <= R
def decomp_int(P,L,R):
    D = [[] for _ in xrange(R-L+1)]
    for p in xrange(2,R+1):
        if P[p]:
            if p>=L:
                D[p-L].append(p)
            for n in xrange(max(2,(L+p-1)/p)*p,R+1,p):
                D[n-L].append(p)
    return D

def parmi(n,p,F):
    if p==0:
        yield 1
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1,F):
                yield S*F[i]

# inclusion-exclusion pour compter les 1<=q<=B
# premiers avec p dont les facteurs premiers sont F
def coprime(F,B):
    cpt = B
    for k in xrange(1,len(F)+1):
        cpt0 = 0
        for x in parmi(len(F),k,F):
            cpt0 += B/x
        cpt += -cpt0 if k%2==1 else cpt0
    return cpt

# meme chose mais en comptant seulement les nb pairs
# (pour p impair de facteurs F)
def even_coprime(F,B):
    cpt = B/2
    for k in xrange(1,len(F)+1):
        cpt0 = 0
        for x in parmi(len(F),k,F):
            cpt0 += B/(2*x)
        cpt += -cpt0 if k%2==1 else cpt0
    return cpt

def main():
    N = 3141592653589793
    S = int(sqrt(N))+1
    I = 10**6
    P = sieve(S+I)
    # m > n > 0, n coprime with m and not both odd
    # a = m^2 - n^2, b = 2mn, c = m^2 + n^2 <= N
    # so n^2 <= N - m^2
    D = decomp_int(P,0,I-1)
    m0 = 0
    res = 0
    for m in xrange(2,S):
        if m%I==0:
            # decomposition par intervalles de taille I
            # pour limiter l'utilisation memoire
            m0 = m
            D = decomp_int(P,m0,m0+I-1)
        nmax = min(m-1,int(sqrt(N-m*m)))
        if m%2==1:
            res += even_coprime(D[m-m0],nmax)
        else:
            res += coprime(D[m-m0],nmax)
    print res

main()
