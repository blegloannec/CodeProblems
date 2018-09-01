#!/usr/bin/env python

import sys

# PLSSC classique
def LCS(A,B):
    T = [[0 for _ in xrange(len(B)+1)] for _ in xrange(len(A)+1)]
    for i in xrange(1,len(A)+1):
        for j in xrange(1,len(B)+1):
            if A[i-1]==B[j-1]:
                T[i][j] = 1+T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])
    return T

# remontee dans le DAG des solutions optimales
def remontee():
    Q = [(len(A),len(B))]
    while Q:
        i,j = Q.pop()
        visited[i][j] = True
        if i>0 and j>0 and A[i-1]==B[j-1] and not visited[i-1][j-1]:
            Q.append((i-1,j-1))
        if i>0 and T[i][j]==T[i-1][j] and not visited[i-1][j]:
            Q.append((i-1,j))
        if j>0 and T[i][j]==T[i][j-1]:
            # cas ou une lettre de B est sautee dans une solution
            # optimale, on peut donc inserer en i dans A la lettre
            # en j dans B
            # on utilise un ensemble car l'insertion est caracterisee par
            # la lettre elle-meme et non sa position dans B (plusieurs indices
            # de B portant la meme lettre peuvent conduire a une meme insertion
            # dans A, qui doit etre comptee une seule fois)
            insert[i].add(B[j-1])
            if not visited[i][j-1]:
                Q.append((i,j-1))

def main():
    global A,B,T,visited,insert
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    T = LCS(A,B)
    l = T[len(A)][len(B)]
    visited = [[False for _ in xrange(len(B)+1)] for _ in xrange(len(A)+1)]
    insert = [set() for _ in xrange(len(A)+1)]
    remontee()
    print sum(map(len,insert))

main()
