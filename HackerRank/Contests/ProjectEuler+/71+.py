#!/usr/bin/env python

import sys

# https://en.wikipedia.org/wiki/Farey_sequence
# c/d < a/b sont voisins dans la sequence de rang max(b,d)
# ssi ad - bc = 1

# NB : on peut utiliser la formule du median de Farey pour calculer
# des termes successifs, mais on n'utilisera pas cette technique
# ici...

# via Bezout ua + vb = 1
# 1. si v<0 (et u>0) alors -v/u est un predecesseur de a/b dans
# la sequence de rang max(b,-v)
# 2. sinon u<0 (et v>0), alors (u+kb)a + (v-ka)b = 1 (pour tout k)
# permet d'inverser les signes de u et v pour se ramener au premier cas
# comme l'algo d'Euclide etendu renvoie toujours une paire "minimale"
# ie abs(u)<abs(b) et abs(v)<abs(a)
# alors (u+b)a + (v-a)b = 1 (k=1) convient pour avoir u>0

# Strategie :
# - trouver un predecesseur "minimal" de a/b avec bezout
# - optimiser ce predecesseur (trouver le bon k ci-dessus)
#   jusqu'a atteindre le rang requis

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        a,b,N = map(int,sys.stdin.readline().split())
        _,u,v = bezout(a,b)
        # coeff correction
        if u<0:
            u += b
            v -= a
        # coeff optim
        k = N/b-1
        u += k*b
        v -= k*a
        if u+b<=N:
            u += b
            v -= a
        print -v,u

main()
