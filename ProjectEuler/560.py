#!/usr/bin/env python

# runs in 1.5s with pypy

from math import sqrt
from fractions import gcd

# Code pour intuiter la fonction de Grundy
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(101)]
G[0] = 0
G[1] = 1
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in xrange(1,n):
        if gcd(k,n)==1:
            succ.add(grundy(n-k))
    g = mex(succ)
    G[n] = g
    return g

# Fonction de Grundy decouverte :
# - si n est pair, grundy(n) = 0
# - si p est premier impair, grundy(p) est le numero de p en dans la liste des
# nb premiers, en commencant la numerotation a 2 (pour 3)
# P 2 3 5 7 11 13
# G 0 2 3 4 5  6
# - si n est impair non premier, grundy(n) = grundy(p) pour p le plus petit
# facteur premier de n
# Cette fonction de Grundy se calcule donc plutot bien avec un crible !

def sieve(N):
    G = [0 for _ in xrange(N)]
    G[1] = 1
    cpt = 2
    s = int(sqrt(N))+1
    for i in xrange(3,N,2):
        if G[i]<=0:
            G[i] = cpt
            if i<s:
                for k in xrange(3*i,N,2*i):
                    if G[k]<=0:
                        G[k] = cpt
            cpt += 1
    return G,cpt

# Les piles sont de tailles comprises entre 1 et n-1.
# Soit N(k,x) = nb de configurations a k piles dont le xor des
#               fonctions de grundy des piles vaut x
# On cherche a calculer N(k,0).
# En particulier N(1,x) = nb de 1 <= i < n tels que Grundy(i) = x
# On a clairement N(k+1,x) = sum_{a xor b = x} N(1,a)*N(k,b)
# i.e. une convolution en utilisant le xor sur les indices (et non le +).
# Calcul naif en O(n^2), mais O(n log n) par Fast Walsh-Hadamard Transform
# (pour n une puissance de 2).
# Si l'on note @ cette convolution, on a N(k+1,.) = N(1,.) @ N(k,.)
# et donc N(k,.) = N(1,.) ^@ k  (pour ^@ l'exponentiation associee a @).
# Il suffit donc d'appliquer la WHT a N(1,.), d'elever les valeurs
# a la puissance k, puis d'appliquer la transformation inverse pour
# obtenir N(k,.).

# Fast Walsh-Hadamard Transform
# see https://csacademy.com/blog/fast-fourier-transform-and-variations-of-it
def FWHT(P,MOD,inv=False):
    N = len(P)  # power of 2
    l = 1
    while l<<1 <= N:
        for i in xrange(0,N,l<<1):
            for j in xrange(l):
                u = P[i+j]
                v = P[i+l+j]
                P[i+j] = (u+v) % MOD
                P[i+l+j] = (u-v) % MOD
        l <<= 1
    if inv:
        #Ninv = inv_mod(N,MOD)
        Ninv = pow(N,MOD-2,MOD)  # for prime MOD
        for i in xrange(N):
            P[i] = (P[i]*Ninv) % MOD

def L(N,K,P=10**9+7):
    G,Gsup = sieve(N)
    L = 1
    while L<Gsup:
        L <<= 1
    Gval = [0]*L
    for i in xrange(1,N):
        Gval[G[i]] += 1
    FWHT(Gval,P)
    for i in xrange(L):
        Gval[i] = pow(Gval[i],K,P)
    FWHT(Gval,P,True)
    return Gval[0]

print L(10**7,10**7,10**9+7)
