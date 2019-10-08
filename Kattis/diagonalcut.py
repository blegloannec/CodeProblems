#!/usr/bin/env python3

from math import gcd

# Un rectangle est coupe en 2 ssi la coupe passe en son centre.
# On peut simplement considerer les rectangles comme des carres unite
# traverses par la droite Y = p/q * X pour X dans [0,q].
# Les centres des carres sont les demi-entiers, on cherche donc
# le nb de solutions (x,y) a l'eq. y+1/2 = p/q * (x+1/2), x dans [[0,q-1]],
# i.e. les solutions (x,y) impaires à px = qy, x dans [[0,2q]].
# la solution generale est de la forme (m/q*k, m/p*k) pour m = ppcm(p,q),
# i.e. (p/g*k, q/g*k) pour g = pgcd(p,q).
# Soit, lorsque p/g et q/g sont impairs, g solutions dans l'intervalle
# (pour k = 1 à 2g-1 impair).

p,q = map(int,input().split())
g = gcd(p,q)
p //= g
q //= g
print(g if p%2==q%2==1 else 0)
