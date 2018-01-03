#!/usr/bin/env python

# runs in <3s with pypy

from math import sqrt

# Code pour intuiter la fonction de Grundy
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

#G = [-1]*100001
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    D = []
    for d in range(2,int(sqrt(n))+1):
        if n%d==0:
            D.append(d)
            if d*d!=n:
                D.append(n/d)
    for i in xrange(len(D)):
        for j in xrange(i,len(D)):
            succ.add(grundy(D[i])^grundy(D[j]))
    g = mex(succ)
    G[n] = g
    return g

# Fonction de Grundy decouverte :
# F(n) = nb de facteurs premiers, comptes avec multiplicite, de n
# pour i>0, O(i) = le i-eme odious number (http://oeis.org/A000069)
# on pose O(0) = 0
# alors Grundy(n) = O(F(n)-1)

O = [0, 1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31, 32, 35, 37, 38, 41, 42, 44, 47, 49, 50]

def sieve_nb_factors_mult(N):
    P = [True]*N
    F = [0]*N
    for i in xrange(2,N):
        if P[i]:
            F[i] = 1
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k
                while l%i==0:
                    F[k] += 1
                    l /= i
    return F

# cf pb 560 pour le calcul du nb de conf.
# calcule ici naivement (convolution en O(g^2), pour g une
# puissance de 2 majorant les valeurs de la fonction de Grundy,
# iteree via exponentiation rapide) car g est tres petit
def convol(A,B,MOD):
    N = len(A)
    C = [0]*N
    for i in xrange(N):
        for j in xrange(N):
            C[i^j] = (C[i^j] + A[i]*B[j]) % MOD
    return C

def convol_exp(A,n,MOD):
    if n==0:
        U = [0]*len(A)
        U[0] = 1
        return U
    if n&1==0:
        return convol_exp(convol(A,A,MOD),n>>1,MOD)
    return convol(A,convol_exp(convol(A,A,MOD),n>>1,MOD),MOD)

def f(n,k,m=987654321):
    F = sieve_nb_factors_mult(n+1)
    Vmax = O[max(F)-1]
    L = 1
    while L<=Vmax:
        L <<= 1
    V = [0]*L
    for i in xrange(2,n+1):
        V[O[F[i]-1]] += 1
    W = convol_exp(V,k,m)
    res = 0
    for i in xrange(1,L):
        res = (res + W[i]) % m
    return res

print f(10**7,10**12)
