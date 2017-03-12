#!/usr/bin/env python3

import numpy

# Pour N joueurs, on a fondamentalement une chaine de markov
# a binom(N,2) etats.
# On peut reduire a N etats par un "changement de referentiel" :
# le premier de est fixe en position 0, chaque etape combine un
# deplacement du second de avec une rotation des positions.

# runs in ~17s

def genM(N):
    M = [[0.]*N for _ in range(N)]
    # Petite astuce : quand on arrive dans l'etat 0 (position finale)
    # on y reste indefiniment, ainsi M^k[S][0] donne directement
    # la proba que le jeu soit termine (depuis la position de depart S)
    # en <= k etapes
    M[0][0] = 1.
    for i in range(1,N):
        # le referentiel ne change pas dans 4/6 des cas
        M[i][(i+1)%N] += 4/6 * 1/6
        M[i][i] += 4/6 * 4/6
        M[i][(i-1)%N] += 4/6 * 1/6
        # le referentiel tourne vers la droite dans 1/6 des cas
        M[i][(i+2)%N] += 1/6 * 1/6
        M[i][(i+1)%N] += 1/6 * 4/6
        M[i][i] += 1/6 * 1/6
        # le referentiel tourne vers la gauche dans 1/6 des cas
        M[i][i] += 1/6 * 1/6
        M[i][(i-1)%N] += 1/6 * 4/6
        M[i][(i-2)%N] += 1/6 * 1/6
    return numpy.matrix(M)

def main():
    N = 100
    S = N//2 # position de depart
    M0 = genM(N)
    M = M0.copy()
    E = 0.
    P0 = 0. # proba que le jeu termine en <= k-1 etapes
    for k in range(1,10**5):
        P = M[S,0] # proba que le jeu termine en <= k etapes
        E += k*(P-P0)
        M *= M0
        P0 = P
    print(E)

main()
