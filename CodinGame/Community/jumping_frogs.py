#!/usr/bin/env python3

# Existence of a solution to a CRT system
# <=> equations are pairwise consistent: xi = xj mod gcd(ki,kj)

from math import gcd

X,Y,K = zip(*(tuple(map(int,input().split())) for _ in range(3)))
possible = all((C[i]-C[j])%gcd(K[i],K[j])==0 for C in (X,Y) for i in range(3) for j in range(i+1,3))
print(('Impossible','Possible')[possible])
