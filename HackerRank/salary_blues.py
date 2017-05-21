#!/usr/bin/env python3

from fractions import gcd

# on peut interpreter 1 pas de normalisation comme
# 1 premiere etape "naive" du modulo (A%B calcule naivement par
# soustractions iterees de B a A) de l'algorithme d'euclide
# (puisqu'on recommence jusqu'a egalite)
# la normalisation converge donc vers le PGCD des nombres
# il s'agit de calculer rapidement pour chaque K le PGCD des Ai+K
# or si A>=B, PGCD(A+K,B+K) = PGCD(A+K-(B+K),B+K) = PGCD(A-B,B+K)
# ainsi si A0 = min(A), on a
# PGCD(A0+K,A1+K,...,An+K) = PGCD(A0+K,A1-A0,...,An-A0)
#                          = PGCD(A0+K,PGCD(A1-A0,...,An-A0))

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    # on cherche le min
    imin = 0
    for i in range(1,N):
        if A[i]<A[imin]:
            imin = i
    # on pre-calcule le PGCD des differences au min
    # (en imin cela donne 0, sans impact sur le resultat)
    G = 0
    for i in range(N):
        G = gcd(G,A[i]-A[imin])
    # on traite les requetes
    for _ in range(Q):
        K = int(input())
        print(gcd(G,A[imin]+K))

main()
