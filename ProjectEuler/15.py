#!/usr/bin/env python

# Prog dyn naive implementee ici...
# Mais un tel chemin est parfaitement defini par un multi-ensemble
# a N elements choisis parmi les M+1 bordures verticales de la
# grille, definissant les N emplacements ou l'on descend.
# Il s'agit du nb de combinaisons avec repetitions de taille N
# d'un ensemble de taille M+1, soit N parmi N+M.

def problem15():
    n = 20+1
    M = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        for j in range(1,n):
            M[i][j] = M[i-1][j]+M[i][j-1]
    print M[n-1][n-1]

problem15()
