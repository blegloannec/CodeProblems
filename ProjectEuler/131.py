#!/usr/bin/env python

from math import sqrt

# p premier, on cherche n (et a) tel que n^3 + n^2p = a^3
# ie n^3 (1+p/n) = a^3 ou encore (n+p)/n = a^3/n^3
# Notons que si g = pgcd(n,n+p), alors g | n+p - n = p premier
# donc g = 1 ou p. Mais si g = p, posons n' = n/p entier, on
# a (n+p)/n = (n'+1)/n' = a^3/n^3 or le rapport de 2 cubes ne peut
# pas etre le rapport entre 2 entiers consecutifs. Donc g = 1 et
# n et n+p sont p-e-e donc la fraction (n+p)/n est irreductible.
# Mais alors si on pose g' = pgcd(a^3,n^3), en raisonnant sur les
# decompositions de a et n, on deduit aisement que g' est un cube
# (les multiplicites seront des multiples de 3). Et donc mise sous forme
# irreductible la fraction est encore un rapport de 2 cubes, autrement dit
# n+p et n sont des cubes !

# Donc p est l'ecart entre 2 cubes p = c^3 - d^3 = (c-d)*sum(c^i.d^j, i+j=2)
# Comme p est premier et que la somme sera >1, elle sera = p et c-d = 1.
# Donc p est l'ecart entre 2 cubes consecutifs.

def prime(n):
    if n%2==0:
        return False
    for i in xrange(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def main():
    p = 2**3 - 1
    i = 2
    cpt = 0
    while p<10**6:
        if prime(p):
            cpt += 1
        i += 1
        p = i**3 - (i-1)**3
    print cpt

main()
