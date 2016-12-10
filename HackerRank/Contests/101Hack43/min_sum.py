#!/usr/bin/env python

import sys

# si on developpe les carres dans la somme,
# on obtient ans = 2*k*S2 - 2*S^2
# pour S la somme des bi
# et S2 la somme des bi^2
# il est evident que l'on prendra k elements consecutifs
# de A trie pour minimiser la somme, donc on balaye A avec
# une fenetre de taille k, on met a jour S, S2 et le ans
# minimal en O(1)

def main():
    n,k = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    A.sort()
    ans = float('inf')
    S,S2 = 0,0
    for i in xrange(k):
        S += A[i]
        S2 += A[i]**2
    ans = 2*k*S2 - 2*S**2
    for i in xrange(k,len(A)):
        S += A[i] - A[i-k]
        S2 += A[i]**2 - A[i-k]**2
        ans = min(ans,2*k*S2-2*S**2)
    print ans

main()
