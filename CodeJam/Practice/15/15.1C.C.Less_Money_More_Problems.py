#!/usr/bin/env python

import sys

# L'ensemble de valeurs a couvrir est [0..V]
# mais il peut y avoir des trous dans les valeurs couvertes par
# les pieces fournies : e.g. {2} ne couvrira que des valeurs paires.
# On va donc chercher a boucher les trous dans l'ordre croissant
# et a completer si necessaire.
# 1. L'observation importante est que si l'on couvre [0..v] et qu'on ajoute
#    une piece de valeur w<=v+1, alors on couvre [0..v+C*w] sans trou :
#    union des intervalles [c*w..c*w+v] pour 0<=c<=C.
# 2. En revanche ajouter une piece de valeur w>=v+2 ne permet jamais
#    de couvrir v+1, donc il faut forcement une nouvelle piece de valeur
#    <=v+1 pour boucher le trou et donc au mieux v+1 pour maximiser
#    le nouvel ensemble couvert et ainsi minimiser le nb de nouvelles pieces.


def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        C,D,V = map(int,sys.stdin.readline().split())
        Pre = map(int,sys.stdin.readline().split()) # ordre croissant
        iPre = 0 # plus petit indice de Pre non encore utilise
        currV = 0 # on couvre [1..currV] avec la solution courante
        new = 0
        while currV<V: # on doit couvrir currV+1
            if iPre<len(Pre) and Pre[iPre]<=currV+1:
                # la plus petite piece existante convient pour couvrir currV+1
                currV += C*Pre[iPre]
                iPre += 1
            else:
                # il faut une nouvelle piece de valeur currV+1
                new += 1
                currV += C*(currV+1)
        print 'Case #%d: %d' % (t,new)

main()
