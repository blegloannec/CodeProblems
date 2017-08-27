#!/usr/bin/env python3

# Comme vu dans INOD, ajouter une feuille a un arbre binaire non-enracine,
# c'est choisir une arete, ajouter un nouveau noeud interne au milieu
# et y connecter la nouvelle feuille. On avait n-2 noeuds internes pour n>=3
# feuilles, donc 2n-2 sommets et donc 2n-3 aretes.
# Donc b(n+1) = (2*n-3) * b(n) et b(3) = 1

M = 10**6

def b(n):
    return 1 if n<=3 else ((2*n-5)*b(n-1))%M

print(b(int(input())))
