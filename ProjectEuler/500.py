#!/usr/bin/env python

from math import sqrt
from heapq import *

# si n = p1^a1 ... pk^ak (prime decomposition)
# alors nb_div(n) = prod( ai+1, i=1..k )
# evidemment k <= 500500
# comme on veut la solution la plus petite possible
# on prendra les k premiers nb premiers pour les pi

# on veut nb_div = 2^500500, donc ai = 2^bi-1
# et b1+...+bk = 500500

# mais 2^bi-1 = sum( 2^j, j=0..bi-1 )
# donc on peut decomposer chaque facteur :
# pi^ai = pi^(2^bi-1) = prod( pi^(2^j), j<bi )

# ce qui permet de redecomposer n sous la forme d'un produit
# d'exactement 500500 facteurs de la forme p^(2^c) :
# n = prod( pj^(2^cj), pj premiers non distincts )
# avec la propriete suivante : si p^(2^c) est dans le produit
# alors tous les p^(2^d) avec d < c y sont aussi

# comme on veut le plus petit n possible, on en deduit
# un algo glouton simple :
# tant qu'on n'a pas 500500 facteurs, prendre le plus
# petit facteur de la forme p^(2^c) non encore utilise

# Implementation :
# Initialiser un tas-min avec les 500500 premiers nb premiers
# ie les facteurs de la forme p^(2^0)
# Repeter les etapes suivantes 500500 fois : 
# - depiler le plus petit (disons f=p^(2^c)) et l'ajouter au produit
# - inserer le "successeur" (ie le carre, car p^(2^(c+1)) = f^2) de ce facteur
#   dans le tas

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def main():
    M = 500500507
    N = 7400000
    # pour avoir les 500500 premiers premiers
    P0 = sieve(N)
    P = []
    for i in xrange(N):
        if P0[i]:
            P.append(i)
    sol = 1
    for k in xrange(500500):
        minfac = heappop(P)
        sol = (sol*minfac)%M
        heappush(P,minfac*minfac)
    print sol

main()
