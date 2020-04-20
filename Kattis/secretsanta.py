#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !n = number of permutations on n elements without fixed points (derangements)
# If p is such a permutation such that p(n) = i < n (n-1 possible i),
# then consider j such that p(j) = n:
#  - If i = j, then removing i and n leaves us with an arbitrary
#    derangement over n-2 elements;
#  - Otherwise i ≠ j, then removing n and "rebranching" p(i) = j leaves us
#    with an arbitrary (j is chosen freely) derangement over n-1 elements.
# Hence !n = (n-1) (!(n-2) + !(n-1))

# https://en.wikipedia.org/wiki/Derangement
# https://oeis.org/A000166
# !n/n! --> 1/e very fast

NMAX = 20
F = [1,1]*(NMAX+1)
D = [1,0]*(NMAX+1)
for n in range(2,NMAX+1):
    F[n] = n*F[n-1]
    D[n] = (n-1)*(D[n-1]+D[n-2])

N = min(int(input()), NMAX)
print(1.-D[N]/F[N])
