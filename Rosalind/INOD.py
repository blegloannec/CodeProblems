#!/usr/bin/env python3

# Rajouter une feuille a un arbre binaire non-enracine, c'est
# choisir une arete, ajouter un nouveau noeud interne au milieu
# et y connecter la nouvelle feuille.
# On ajoute donc exactement 1 noeud interne par nouvelle feuille.
# Pour n = 1 ou 2 on a 0 noeud interne.
# Pour n = 3 on a exactement 1 noeud interne et a partir de la l'ecart
# entre le nombre de noeuds internes et de feuilles est constant, il y
# a donc n-2 noeud internes pour n>=3.

def internal(leaves):
    return max(0,leaves-2)

n = int(input())
print(internal(n))
