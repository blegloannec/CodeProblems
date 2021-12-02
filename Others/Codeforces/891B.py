#!/usr/bin/env python3

# NB : Les elements de A sont uniques (sans doublon).
# Pour P une permutation qcq, si l'on a une solution B' de A' = P(A),
# alors on en deduit une solution B = P^(-1)(B') de A.
# On peut donc resoudre le probleme sur une permutation avantageuse de A.
# Supposons par exemple que A' est trie (P la permutation qui realise le tri).
# Soit B' obtenu en decalant cycliquement A' d'une case vers la droite.
# B' est une permutation solution de A' :
#  - pour un ensemble I d'indices ne contenant pas 0, on a, pour tout i dans I,
#    B'_i < A'_i, donc sum_I B'_i < sum_I A'_i ;
#  - pour un ensemble d'indices I contenant 0, alors, pour J l'ensemble
#    complementaire, on a sum_J B'_j < sum_J A'_j d'apres le premier cas,
#    et donc, pour S = sum A, on en deduit
#    sum_I B'_i = S - sum_J B'_j > S - sum_J A'_j = sum_I A'_i.

n = int(input())
A = list(map(int,input().split()))
S = sorted(A)
P = {S[i]:S[(i+1)%n] for i in range(n)}
B = [P[a] for a in A]
print(' '.join(map(str,B)))
