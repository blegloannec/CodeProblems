#!/usr/bin/env python

from math import *

# raisonnement dans le coin superieur droit
# (au lieu de l'inferieur gauche)
# droite y = (x-1+n)/n
# arc f(x) = sqrt(1-x^2)
# primitive F(x) = (x*f(x)+arcsin(x))/2

F = lambda x: (x*sqrt(1-x**2)+asin(x))/2
L = 1-(F(1)-F(0))

# on pourrait faire une recherche dicho., mais pas
# la peine, le resultat est petit
n = 1
while True:
    # intersection
    a,b,c = n**2+1,2*(n-1),(n-1)**2-n**2
    x0 = (-b+sqrt(b**2-4*a*c))/(2*a)
    # aire (triangle + arc)
    A = (1-x0)*(1-(x0-1+n)/n)/2 + x0-(F(x0)-F(0))
    if A/L<0.001:
        break
    n += 1
print n
