#!/usr/bin/env python3

import sys
from collections import *

I = sys.stdin.readlines()  # Input

# Part 1
cpt = 0
for L in I:
    C = Counter(L.split())
    cpt += int(all(C[x]==1 for x in C))
print(cpt)


# Part 2
cpt = 0
for L in I:
    C = defaultdict(int)
    for w in L.split():
        C[''.join(sorted(w))] += 1
    cpt += int(all(C[x]==1 for x in C))
print(cpt)
