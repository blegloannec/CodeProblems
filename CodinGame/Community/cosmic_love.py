#!/usr/bin/env python3

from math import pi

N = int(input())
Planets = []
for _ in range(N):
    name, *rmc = input().split()
    r,m,c = map(float, rmc)
    # NB: because we only care about the ratio dA/dP, we could
    # throw away the dimensionless multiplicative constant 4π/3
    d = m / (4./3.*pi*r**3)
    if name == 'Alice':
        assert c == 0.
        rA = r; dA = d
    else:
        Planets.append((name, d, c))
cmin = float('inf')
for name, d, c in Planets:
    if c < cmin:
        rlim = rA*(2.*dA/d)**(1./3.)
        if c > rlim:
            cmin = c
            nmin = name
print(nmin)
