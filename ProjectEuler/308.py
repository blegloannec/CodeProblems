#!/usr/bin/env python

from math import *

def is_pow2(x):
    return (x>0) and not x&(x-1)

# Fast version: https://oeis.org/A007546
# donne une formule a adapter pour la slow version
# Slow version: https://oeis.org/A007547

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

N = 110000 # pour couvrir les 10001 premiers nb premiers
P,F = sieve_factors(110000)
primes = []
for p in xrange(N):
    if P[p]:
        primes.append(p)

def maxdiv(n):
    return n/F[n][0]

# temps de traitement du nb n
# le calcul de la sum(..) pourrait etre optimise
def f(n):
    if n<2:
        return 0
    b = maxdiv(n)
    # n-1 pour fast version, au lieu de n-b-2
    return n+b-2 + (6*n+2)*(n-b) + 2*sum([n/d for d in xrange(b,n)])

f_sums = [f(n) for n in xrange(N)]
for i in xrange(1,N):
    f_sums[i] += f_sums[i-1]

# temps total
def a(n):
    return f_sums[primes[n-1]]


# simulation pour verification
def simu(n):
    # Slow version:
    Prog = [(17,91),(78,85),(19,51),(23,38),(29,33),(77,29),(95,23),(77,19),(1,17),(11,13),(13,11),(15,2),(1,7),(55,1)]
    # Fast version:
    #Prog = [(17,91),(78,85),(19,51),(23,38),(29,33),(77,29),(95,23),(77,19),(1,17),(11,13),(13,11),(15,14),(15,2),(55,1)]
    Conf = 2
    cpt = 1
    for t in xrange(1,n+1):
        i = 0
        while Conf%Prog[i][1]!=0:
            i += 1
        Conf = Prog[i][0]*Conf/Prog[i][1]
        if is_pow2(Conf):
            p = int(round(log(Conf,2)))
            print t,p,a(cpt)
            cpt += 1

#simu(20000)
print a(10001)
