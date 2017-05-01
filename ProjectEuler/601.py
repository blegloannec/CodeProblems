#!/usr/bin/env python3

from fractions import gcd

# n a une streak(n) = s ssi
# n+1 = 0 mod 2, i.e. n = 1 mod 2
# n+2 = 0 mod 3, i.e. n = 1 mod 3
# ...
# n+s-1 = 0 mod s, i.e. n = 1 mod s
# n+s =/= 0 mod s+1, i.e. n =/= 1 mod s+1
# (s possibilites pour le reste)
# l'ensemble des solutions est donc l'union des solutions des
# s systemes de congruences pour lesquels on fixe une
# valeur =/= 1 pour la derniere equation
# une meilleure facon de le voir :
# Solutions({n+k = k, k=1..s}) - Solutions({n+k = 1 mod k, k=2..s+1})
# et l'on sait que Solutions({n+k = k, k=1..s}) = {1 + k*lcm(1,...,s), k>=0}
# (par les restes chinois et 1 est solution evidente)
# ce qui permet de les compter tres facilement

def lcm(a,b):
    return a*b//gcd(a,b)

def P(s,N):
    L = 1
    for j in range(2,s+1):
        L = lcm(L,j)
    return (N-2)//L - (N-2)//lcm(L,s+1)

print(sum(P(i,4**i) for i in range(1,32)))
