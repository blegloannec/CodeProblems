#!/usr/bin/env python3

# On peut imaginer une prog. dyn. en O(n^2) qui partant de chaque
# feuille prise pour racine calcule le nb de quadruplets impliquant
# cette feuille par un parcours en profondeur...
# Mais l'astuce est de remarquer que le degre etant borne par 3,
# choisir 4 feuilles quelconques identifie exactement un quadruplet.
# Trois feuilles A,B,C ont un unique noeud interne de bifurcation X duquel
# partent 3 branches distinctes menant vers A, B et C.
# Comme X est de degre 3, une quatrieme feuille D doit se connecter a
# ce sous-arbre en un point strictement interieur a l'une de ces branches.
# Si par exemple D se connecte en un point Y interieur a la branche X--C, alors
# les aretes du chemin X--Y non vide engendrent le quadruplet {A,B} | {C,D}.
# Toute autre arete du sous-arbre ne separe qu'une feuille des 3 autres et
# toute autre arete de l'arbre (exterieure au sous-arbre) ne separe aucune
# des 4 feuilles.

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

n = int(input())
print(binom(n,4) % 10**6)
