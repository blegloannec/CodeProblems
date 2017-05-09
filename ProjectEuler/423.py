#!/usr/bin/env python

from math import sqrt

# pour C(n,c) = nb de conf. de taille n avec au plus
#               c paires consecutives de meme valeur
# on a C(n,c) = 5*C(n-1,c) + C(n-1,c-1) et C(1,_) = 6
# mais cela n'est pas suffisant en soi
# pour C0(n,k) = nb de conf. de taille n avec exactement
#                c paires consecutives de meme valeur
# on a C0(n,k) = binom(n-1,k) * 6*5^(n-1-k)
# (choix des k paires * choix des valeurs)
# et C(n,c) = sum(C0(n,k), k=0..c)
# combiner ces deux formules conduit a l'algo ci-apres

# runs in 75s with pypy, but the algo is actually ok and
# most of the time is spent pre-computing the inverses of
# the factorials, so it's ok-ish (and this would definitely
# be ok in C++)...

def sieve(N):
    P = [True]*N
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# crible
N = 50*10**6
P = sieve(N+1)

M = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=M):
    _,u,_ = bezout(a,n)
    return u

# pre-calcul des factorielles et leurs inverses
F,Finv = [1],[1]
for n in xrange(1,N+1):
    F.append((F[-1]*n)%M)
    Finv.append(inv_mod(F[-1]))

def binom(n,p):
    return (F[n]*(Finv[p]*Finv[n-p])%M)%M


def C0(n,c):
    return 0 if c>n-1 else (binom(n-1,c)*6*pow(5,n-1-c,M))%M

def S(L):
    Pi = 0
    Cm1,C = 6,6  # C(n,pi(n)-1) et C(n,pi(n)) courants
    res = 6
    for n in xrange(2,L+1):
        if P[n]: # +1
            Pi += 1
            # on decale de 1 les valeurs du rang precedent
            C,Cm1 = (C + C0(n-1,Pi))%M,C
        C = (Cm1 + 5*C)%M
        res = (res + C)%M
        Cm1 = (C - C0(n,Pi))%M
    return res

print(S(N))
