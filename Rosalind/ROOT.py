#!/usr/bin/env python3

# Si l'on considere les arbres binaires non-enracines a n feuilles etiquetees,
# alors en retirant la n-ieme feuille et en choisissant son pere comme racine,
# on obtient, sans doublon, tous les arbres binaires enracines a n-1 feuilles
# etiquetees.
# Ou reciproquement, on obtient les arbres non-enracines en connectant
# une n-ieme feuille a la racine d'un arbre binaire non enracine.
# D'ou B(n) = b(n+1) pour b() la fonction du pb CUNR.

M = 10**6

def b(n):
    return 1 if n<=3 else ((2*n-5)*b(n-1))%M

def B(n):
    return b(n+1)

print(B(int(input())))
