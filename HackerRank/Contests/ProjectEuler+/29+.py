#!/usr/bin/env python

import sys
from math import *

# Si x^a = y^b, alors x et y sont puissances d'un meme z
# En effet, on decompose (2 facteurs premiers pour simplifier)
# x = p^u.q^v et y = p^u'.q^v'
# alors ua = u'b et va = v'b
# soit u/u' = v/v' = b/a
# si on factorise u = u0.pgcd(u,u') et u' = u0'.pgcd(u,u')
# et v = v0.pgcd(v,v') et v' = v0'.pgcd(v,v')
# alors u0/u0' = v0/v0' et ces fractions sont irreductibles
# donc u0 = v0 et u0' = v0'
# des lors, pour z = p^pgcd(u,u').q^pgcd(v,v')
# on a x = z^u0 et y = z^u0'

# Ainsi pour chaque 2 <= a <= N, si a est une puissance d'un nb x
# deja considere, alors on l'ignorera car on aura deja tout calcule
# lors de l'examen de x.

# Lors de l'iteration sur un nombre 2 <= a <= N non encore pris en compte.
# Les puissances de a a considerer sont les a^i <= N, i.e. imax = int(log N / log a)
# pour chaque tel a^i, les puissances a considerer sont les a^(ij)
# pour tout 2 <= j <= N.
# Bilan, le nb total d'elements engendres par a et ses puissances est exactement
# le nb de produits *distincts* ij pour 1 <= i <= imax et 2 <= j <= N.
# La plus grande valeur pour imax est log N / log 2, on peut precalculer
# ces nb de produits distincts pour tout imax.

# Compte le nb de produits ab distincts
# pour 1 <= a < k et 2 <= b <= N
# et renvoie les resultats pour tous les k<n
def precalc(n,N):
    P = [0 for _ in xrange(n)]
    s = set()
    for i in xrange(1,n):
        for j in xrange(2,N+1):
            s.add(i*j)
        P[i] = len(s)
    return P

def main():
    N = int(sys.stdin.readline())
    P = precalc(int(log(N,2))+1,N)
    vu = [False for _ in xrange(N+1)]
    res = 0
    for a in xrange(2,N+1):
        if not vu[a]:
            # N+1 pour corriger les erreurs de type log(x^y,x) = y - epsilon
            res += P[int(log(N+1,a))]
            x = a*a
            while x<=N:
                vu[x] = True
                x *= a
    print res

main()
