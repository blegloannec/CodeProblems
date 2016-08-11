#!/usr/bin/env python

import sys

# m pouvant etre tres grand, on va chercher une solution
# dependant le moins possible de m (donc en evitant la recurrence).
# On remarque qu'a m fixe, le nb de solutions de taille n
# contenant b blocs de taille >=m peut etre obtenu en "compressant"
# les blocs en retirant m-1 a leur taille (chaque bloc de taille m+k>=m,
# est ramene a une taille k+1>=1), ramenant l'espace a S = n-(m-1)b.
# Choisir les b blocs est alors choisir 2b barres parmi S+1 emplacements.

# Ce calcul direct de F est efficace pour obtenir une valeur donnee.
# On procede alors par recherche dichotomique.
# Pour obtenir une borne sup sur n pour cette recherche, on
# remarque que si n > k(m+1), alors clairement F(n,m) > 2^k

def binom(n, k):
    prod = 1
    for i in xrange(k):
        prod = (prod*(n-i))/(i+1)
    return prod

def F(m,n):
    if n<m:
        return 1
    return sum(binom(n+1-(m-1)*b,2*b) for b in xrange((n+1)/(m+1)+1))

def dicho(m,X,a,b):
    while b>a:
        n = (a+b)/2
        if F(m,n)<=X:
            a = n+1
        else:
            b = n
    return a

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        m,X = map(int,sys.stdin.readline().split())
        print dicho(m,X,m,61*m)

main()
