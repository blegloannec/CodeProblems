#!/usr/bin/env python

import sys

def main():
    N,K = map(int,sys.stdin.readline().split())
    T = []
    for i in xrange(N):
        T.append(map(int,sys.stdin.readline().split()))
        while len(T[-1])<N:
            T[-1].append(0)
    # propagation des sommes
    for i in xrange(1,N):
        for j in xrange(N):
            T[i][j] += T[i-1][j]
    S = []
    # algo en O(N^3)
    for i in xrange(N):
        for j in xrange(i+1):
            # on examine les triangles de bord inferieur droit (i,j)
            # pour toute largeur k<=j<=i
            # comme on a precalcule les sommes sur les colonnes
            # rajouter 1 a la largeur necessite de rajouter
            # une valeur T[i][j-k]-T[i-k-1][j-k] obtenue en O(1)
            s = 0
            # iterations k<j
            for k in xrange(j):
                s += T[i][j-k]-T[i-k-1][j-k]
                S.append(s)
            # + iteration k=j
            if i>j:
                s += T[i][0]-T[i-j-1][0]
            else:
                s += T[i][0]
            S.append(s)
    S.sort()
    for k in xrange(K):
        print S[k]

main()
