#!/usr/bin/env python3

from fractions import Fraction

# Lors d'un croisement avec Aa, un individu
#  - Aa donne aa et AA avec proba 1/4, Aa avec proba 1/2
#  - aa donne aa et Aa avec proba 1/2
#  - AA donne AA et Aa avec proba 1/2
# Initialement (Tom seul) on a P(aa) = P(AA) = 0 et P(Aa) = 1.
# A k = 1, les probas individuelles sont P(aa) = P(AA) = 1/4 et P(Aa) = 1/2.
# Cette distribution est stable pour les probas de croisement donnees ci-dessus :
# elle reste la meme pour tout k>=1.
# Idem pour Bb donc, par independance, la proba un pour individu de generation k>=1
# est P(AaBb) = P(Aa)*P(Bb) = 1/4

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

k,N = map(int,input().split())
P = 1/4
print(sum(binom(2**k,n) * P**n * (1-P)**(2**k-n) for n in range(N,2**k+1)))
