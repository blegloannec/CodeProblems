#!/usr/bin/env python

import random
random.seed()

# 13! = 2^10 * 3^5 * 5^2 * 7 * 11 * 13
# On contruit n tel que phi(n) = 13!
# a partir de sa decomposition en nb premiers.
# Tout nb premier >13 apparait au plus 1 fois
# et dans ce cas p-1 ne doit etre forme que de nb
# premiers <=13 avec des multiplicites <= a celles
# de 13!.

# Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

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

def miller_rabin(n,s=15):
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

# Calcul (naif) des nb premiers utilisables
def init():
    primes = []
    for a2 in xrange(11):
        for a3 in xrange(6):
            for a5 in xrange(3):
                for a7 in xrange(2):
                    for a11 in xrange(2):
                        for a13 in xrange(2):
                            x = 2**a2 * 3**a3 * 5**a5 * 7**a7 * 11**a11 * 13**a13
                            if x>15 and miller_rabin(x+1):
                                primes.append((x+1,(a2,a3,a5,a7,a11,a13)))
    return primes

def diff(X,Y):
    Z = tuple(X[i]-Y[i] for i in xrange(6))
    return (min(Z)>=0, Z)

# prog dyn pour calculer les produits des nb premiers >13
# selectionnes dont l'indicatrice verifie une certaine
# combinaison de multiplicites
primes = init()
C0 = (0,0,0,0,0,0)
memo = {}
def dp(C,n):
    if n<0:
        return [1] if C==C0 else []
    if (C,n) in memo:
        return memo[C,n]
    res = dp(C,n-1)[:]
    b,C1 = diff(C,primes[n][1])
    if b:
        res += map((lambda x: x*primes[n][0]),dp(C1,n-1))
    memo[C,n] = res
    return res

# generateur pour completer une combinaison avec
# les nb premiers entre 2 et 13
Cible = (10,5,2,1,1,1)
pbase = [(2,(0,0,0,0,0,0)),(3,(1,0,0,0,0,0)),(5,(2,0,0,0,0,0)),(7,(1,1,0,0,0,0)),(11,(1,0,1,0,0,0)),(13,(2,1,0,0,0,0))]
def dp2(C,n=5):
    if n<0:
        if C==C0:
            yield 1
    else:
        if C[n]>0:
            # on est oblige de prendre l'element manquant
            # avec multiplicite >=2
            b,C1 = diff(C,pbase[n][1])
            if b:
                C1 = list(C1)
                C1[n] = 0
                C1 = tuple(C1)
                for x in dp2(C1,n-1):
                    yield x*pbase[n][0]**(C[n]+1)
        else:
            # on prend pas l'element
            for x in dp2(C,n-1):
                yield x
            b,C1 = diff(C,pbase[n][1])
            if b:
                # on prend l'element avec multiplicite 1
                for x in dp2(C1,n-1):
                    yield x*pbase[n][0]

def main():
    nbs = []
    for a2 in xrange(11):
        for a3 in xrange(6):
            for a5 in xrange(3):
                for a7 in xrange(2):
                    for a11 in xrange(2):
                        for a13 in xrange(2):
                            C = (a2,a3,a5,a7,a11,a13)
                            _,C0 = diff(Cible,C)
                            for f in dp2(C0):
                                nbs += map((lambda x: x*f),dp(C,len(primes)-1))
    nbs.sort()
    print nbs[150000-1]

main()
