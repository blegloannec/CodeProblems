#!/usr/bin/env python3

# Le plus dur est vraiment de comprendre l'enonce !
# Il s'agit de chaines de longueur 2 <= n <= 26 dont
# les caracteres sont {a..z}, soit {0..25}, et tous les
# caractere sont distincts.
# Fixons une taille n<=26 et les binom(26,n) lettres utilisees.
# Le nombre de chaines dont l'unique "fracture" est en position k>=1
# (i.e. u(k-1)<u(k)) est exactement binom(n,k)-1 : on choisit
# les k elements u(0),...,u(k-1) et l'on n'a d'autre choix que de les
# ranger par ordre decroissant, les elements u(k),...,u(n-1) sont les
# n-k elements restant ranges par ordre decroissant, on a une fracture
# u(k-1)<u(k) ssi les k elements choisis ne sont pas les k plus grandes
# lettres, d'ou le -1.
# Si on somme pour tout k=1,...,n-1 cela donne 2^n-2-(n-1) = 2^n-n-1
# On peut retrouver ce resultat plus directement : il s'agit de choisir
# un ensemble quelconque non vide de lettres d'avant fracture qui ne soit pas
# un ensemble constitue uniquement des plus grandes lettres, soit
# 2^n-1 - n choix possibles (les n ensembles retires sont les ensembles
# constitues des k plus grandes lettres pour k=1,...,n).

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

def p(n):
    return binom(26,n)*(2**n-n-1)

print(max(p(n) for n in range(2,27)))
