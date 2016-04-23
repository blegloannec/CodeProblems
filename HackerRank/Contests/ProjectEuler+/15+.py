#!/usr/bin/env python

import sys

# Un tel chemin est parfaitement defini par un multi-ensemble
# a N elements choisis parmi les M+1 bordures verticales de la
# grille, definissant les N emplacements ou l'on descend.
# Il s'agit du nb de combinaisons avec repetitions de taille N
# d'un ensemble de taille M+1, soit N parmi N+M.

def binom(n,k):
    res = 1
    for i in xrange(k):
        res = ((res*(n-i))/(i+1))
    return res

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N,M = map(int,sys.stdin.readline().split())
        print binom(M+N,N)%1000000007

main()
