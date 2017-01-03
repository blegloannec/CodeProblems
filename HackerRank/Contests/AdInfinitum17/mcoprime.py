#!/usr/bin/env python

import sys
from collections import defaultdict
from fractions import gcd
from math import sqrt
import random
random.seed()

# on ajoute iterativement les facteurs premiers pi^ai de m
# si l'on connait le nb de m-tableaux de taille n de m
# calculons le nb de m'-tableaux pour m' = m * pi^ai
# pour en fabriquer, on prend un m-tableau dans lequel on
# selectionne un sous-ensemble de cases jamais consecutives
# pour recevoir des p^b avec 1<=b<=a+i
# le nb de telles selections verifie Si(n) = Si(n-1) + ai*Si(n-2)
# (donc on peut calculer ce nb par exponentiation d'une matrice 2x2)
# et il suffit de multiplier le nb courant de m-tableaux par Si(n)
# pour obtenir le nb de m'-tableaux

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

# Miller-Rabin
def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

N = 10**6
Pr = sieve(N)

# version deterministe 64 bits
def miller_rabin(n):
    if n<N:
        return Pr[n]
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

def pollard_rho(n):
    l = set()
    c = random.randint(1,n-1)
    f = (lambda x: (x*x+c)%n)
    x = random.randint(0,n-1)
    y = x
    x = f(x)
    y = f(f(y))
    while x!=y:
        p = gcd(n,abs(x-y))
        if 1<p<n:
            return p
        x = f(x)
        y = f(f(y))
    return None

def factorisation(n,D):
    while n>1:
        if miller_rabin(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

# Retire les facteurs 2 avant (sinon ca boucle) :
def full_factorisation(n):
    D = defaultdict(int)
    while n%2==0:
        D[2] += 1
        n /= 2
    return factorisation(n,D)

P = 10**9+7

def matmult((A00,A01,A10,A11),(B00,B01,B10,B11)):
    return (((A00*B00)%P+(A01*B10)%P)%P,((A00*B01)%P+(A01*B11)%P)%P,((A10*B00)%P+(A11*B10)%P)%P,((A10*B01)%P+(A11*B11)%P)%P)

def matpow(A,n):
    if n==0:
        return (1,0,0,1)
    if n%2==0:
        return matpow(matmult(A,A),n/2)
    return matmult(A,matpow(matmult(A,A),n/2))

memo = {}
def coeff(a,n):
    if (a,n) in memo:
        return memo[a,n]
    M00,M01,_,_ = matpow((1,a,1,0),n-1)
    res = (((a+1)*M00)%P+M01)%P
    memo[a,n] = res
    return res

# MAIN
def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n,m = map(int,sys.stdin.readline().split())
        D = full_factorisation(m)
        D = [D[i] for i in D]
        res = 1
        for i in xrange(len(D)):
            res = (res*coeff(D[i],n))%P
        print res

main()
