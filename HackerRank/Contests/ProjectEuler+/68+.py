#!/usr/bin/env python

import sys
from collections import defaultdict

# On resout ce pb par un backtracking un peu malin.
# On commence par calculer tous les triplets (a,b,c) pour lesquels
# a+b+c = S (avec 1 <= a,b,c <= 2N), ce qui fait assez peu de triplets.
# Dans chaque triplet (a,b,c) :
#  - a representera la valeur exterieure
#  - b et c les valeurs interieures consecutives
# Une solution est constituee de N triplets
# avec le c d'un triplet egal au b du triplet suivant.
# On stockera donc nos triplets selon b dans une table de hashage
# (pour obtenir facilement les triplets suivants possibles a
#  partir du triplet precedent).
# On commence toute solution par un triplet pour lequel a0 := a <= N+1
# et tous les triplets de la solution verifieront a > a0.
# On backtrack sur les triplets de la solution en cours de construction dans l'ordre en utilisant
# un masque binaire pour chaque triplet et un masque courant representant les
# nombres deja utilises afin de filtrer les triplets encore utilisables rapidement.

def mask(a,b,c):
    m = 0
    m |= 1<<a
    #m |= 1<<b
    m |= 1<<c
    return m

# On genere (naivement) les triplets (a,b,c)
# tels que a+b+c = S.
# On les indexe dans un dico selon b.
# Les triplets pour lesquels a<=N+1 sont de plus
# eligibles pour servir de point de depart.
def triplets(N,S):
    start = []
    suiv = defaultdict(list)
    for a in xrange(1,2*N+1):
        for b in xrange(1,2*N+1):
            if b==a:
                continue
            for c in xrange(1,2*N+1):
                if c==a or c==b:
                    continue
                if a+b+c==S:
                    m = mask(a,b,c)
                    suiv[b].append((m,a,b,c))
                    if a<=N+1:
                        m |= 1<<b
                        start.append((m,a,b,c))
    return start,suiv

def to_str(sol):
    return ''.join(map((lambda (a,b,c): '%d%d%d'%(a,b,c)),sol))

Sols = []
def start_backtrack(N,S,start,suiv):
    sol = []
    for (m,a,b,c) in start:
        sol.append((a,b,c))
        backtrack(N,S,suiv,1,a,c,m,sol)
        sol.pop()

def backtrack(N,S,suiv,i,a0,c0,M,sol):
    if i==N-1:
        c,b = sol[0][1],sol[-1][2]
        a = S-b-c
        if a>a0 and a<=2*N and (M>>a)&1==0:
            sol.append((a,b,c))
            Sols.append(to_str(sol))
            sol.pop()
    else:
        for (m,a,b,c) in suiv[c0]:
            if a>a0 and m&M==0:
                sol.append((a,b,c))
                backtrack(N,S,suiv,i+1,a0,c,M|m,sol)
                sol.pop()

def main():
    N,S = map(int,sys.stdin.readline().split())
    start,suiv = triplets(N,S)
    start_backtrack(N,S,start,suiv)
    Sols.sort()
    for s in Sols:
        print s

main()
