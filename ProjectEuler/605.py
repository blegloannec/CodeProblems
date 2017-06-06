#!/usr/bin/env python3

from fractions import *

# chaque joueur n'a qu'une occasion de gagner par cycle
# soit P(n,k,i) = proba que k gagne au bout de i cycles
# si on note 0/1 la perte/gain d'un tour par le "premier" joueur
# de ce tour (dans l'ordre naturel, celui de l'enonce), le joueur k
# gagne si la sequence de jeu est de la forme u01 avec u un mot
# de taille in+k-2 ne contenant pas le motif 01
# donc u = 1^a.0^b avec a+b = in+k-2 et a,b>=0
# il y a donc in+k-1 tels mots parmi 2^(in+k-2) mots equiprobables
# d'ou P(n,k,i) = 1/4 * (in+k-1) / 2^(in+k-2)
# (1/4 la proba d'avoir 01 a la fin)
# P(n,k) = sum( P(n,k,i), i>=0 )
#        = 1/4 * sum( (in+k-1) (1/2)^(i*n+k-2), i>=0)
# sum( (in+k-1) x^(i*n+k-2), i>=0) = d/dx(sum( x^(i*n+k-1), i>=0))
#                                  = d/dx(x^(k-1) / (1-x^n))
#                                  = (k-1)*x^(k-2) / (1-x^n) + n*x^(k+n-2) / (1-x^n)^2
# ce qui, evalue en 1/2 et simplifie, donne
# P(n,k) = 2^(n-k)*((k-1)*2^n-k+n+1) / (2^n-1)^2
# on a besoin de la forme irreductible mais (sans preuve) le PGCD ne depend que de n
# et pour n impair il vaut toujours 1

def P(n,k):
    return Fraction(2**(n-k)*((k-1)*2**n-k+n+1),(2**n-1)**2)

#print(P(6,2),P(3,1))

def M(n,k,m): # pour numerateur et denominateur p-e-e, e.g. n impair
    return (pow(2,n-k,m)*((k-1)*pow(2,n,m)-k+n+1)*pow(pow(2,n,m)-1,2,m))%m

print(M(10**8+7,10**4+7,10**8))
