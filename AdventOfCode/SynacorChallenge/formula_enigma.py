#!/usr/bin/env python

# _ + _ * _^2 + _^3 - _ = 399
A = [2,3,5,7,9]

from itertools import permutations

for P in permutations(A):
    if P[0] + P[1] * P[2]**2 + P[3]**3 - P[4] == 399:
        print(*P)
