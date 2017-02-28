#!/usr/bin/env python3

from fractions import *

# Il s'agit de calculer la distribution limite
# de 2 chaines de Markov.
# La distribution limite est un vecteur positif et
# normalise (de somme 1) qui est point fixe de la
# matrice de la chaine, i.e. vecteur propre pour la
# valeur propre 1.
# Les matrices des 2 chaines sont faciles a construire,
# dans les 2 cas 1 est valeur propre et le sous-espace
# propre associe est de dimension 1 (donc vecteur normalise
# unique).
# On remarque avec Sage qu'un vecteur propre (non normalise) associe
# a toujours la forme suivante, avec toujours les memes coeffs
# (ici remis sous forme de matrice pour la taille 5)
# Calcul (i)
#[1, 4/3, 4/3, 4/3, 1]
#[4/3, 5/3, 5/3, 5/3, 4/3]
#[4/3, 5/3, 5/3, 5/3, 4/3]
#[4/3, 5/3, 5/3, 5/3, 4/3]
#[1, 4/3, 4/3, 4/3, 1]
# Calcul (ii)
#[1, 3/2, 3/2, 3/2, 1]
#[3/2, 2, 2, 2, 3/2]
#[3/2, 2, 2, 2, 3/2]
#[3/2, 2, 2, 2, 3/2]
#[1, 3/2, 3/2, 3/2, 1]
# (une fois qu'on a "intuite" cette distribution, il n'est pas difficile
#  de verifier par le calcul qu'elle est correcte)

C1 = [Fraction(5,3),Fraction(4,3),1]
C2 = [2,Fraction(3,2),1]

def P0(N,C):
    S = (N-2)*(N-2)*C[0] + 4*(N-2)*C[1] + 4*C[2]
    p = 0
    for x in range(1,N+1):
        x2 = x*x-1
        i,j = x2//N,x2%N
        if 0<i<N-1 and 0<j<N-1:
            p += C[0]
        elif 0<i<N-1 or 0<j<N-1:
            p += C[1]
        else:
            p += C[2]
    return p/S

def P(N):
    return (P0(N,C1)+P0(N,C2))/2

#print(float(P(5)))
print(float(P(1000)))
