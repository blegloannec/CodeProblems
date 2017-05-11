#!/usr/bin/env python

from math import log10

# cf pb 567
# pour H(n) = sum(1/k, k=1..n)
# on a D(n) = JB(n) - JA(n) = H(n)/2^n

def D(n):
    H = sum(1./k for k in xrange(1,n+1))
    # on passe au log en base 10
    L = log10(H)-n*log10(2)
    # on repasse a l'exponentielle en ne gardant
    # que la partie fractionnelle de l'exposant
    return 10.**(L-int(L))

# NB: en faisant ce calcul avec des flottants 64 bits
#     seuls les 7 premiers chiffres (i.e. ceux demandes)
#     sont corrects
print D(123456789)
