#!/usr/bin/env python

import sys
from math import sqrt
from bisect import *

# si p | R(10^n) alors p | R(10^l) pour tout l>=k
# pour les donnees du pb, il suffit de tester 10^17
# Pre-calculer les nb pour le dernier testcase prend ~4.5s en python
# (pour les autres ca passe en <1s), ce qui, combine au pre-calcul des sommes
# donne pile 10s ! On pourrait sans doute optimiser un peu pour que ca passe
# mais comme ils sont tres peu nombreux, on les stocke en dur pour economiser
# ces 4s...

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def precomp():
    N = 3*10**7
    P = sieve(N)
    k = 10**17
    cpt = 2
    D = []
    for p in xrange(3,N,2):
        if P[p]:
            if pow(10,k,9*p)==1:
                D.append(p)
    return D

#print precomp()
D = set([11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 65537, 69857, 76001, 76801, 160001, 162251, 163841, 307201, 453377, 524801, 544001, 670001, 952001, 976193, 980801, 1146881, 1378001, 1514497, 1610501, 1634881, 1676321, 1920001, 2800001, 3072001, 5070721, 5767169, 5882353, 6144001, 6187457, 6576001, 6600001, 7019801, 8253953, 8257537, 9011201, 12600001, 16384001, 18453761, 18750001, 21408001, 26214401])

def main():
    N = 3*10**7
    P = sieve(N)
    k = 10**17
    T = int(sys.stdin.readline())
    S = [(0,0),(2,2)]
    for p in xrange(3,N,2):
        if P[p] and p not in D:
            S.append((p,S[-1][1]+p))
    for _ in xrange(T):
        L = int(sys.stdin.readline())
        print S[bisect_left(S,(L,0))-1][1]
        
main()
