#!/usr/bin/env python

# pour ce (type de) code, pypy est ~40 fois
# plus rapide que python !

N = 1000
T = [[0 for _ in xrange(N)] for _ in xrange(N)]

def gen():
    t = 0
    M = 1<<20
    D = 1<<19
    for i in xrange(N):
        for j in xrange(i+1):
            t = (615949*t+797807)%M
            T[i][j] = t-D

def main():
    gen()
    # propagation des sommes
    for i in xrange(1,N):
        for j in xrange(N):
            T[i][j] += T[i-1][j]
    m = 0
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
                m = min(m,s)
            # + iteration k=j
            if i>j:
                s += T[i][0]-T[i-j-1][0]
            else:
                s += T[i][0]
            m = min(m,s)
    print m

main()
