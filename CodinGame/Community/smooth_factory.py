#!/usr/bin/env python3

from itertools import product
from heapq import *

# classic generation problem of 5-smooth / ugly / Hamming numbers
# http://oeis.org/A051037
# http://oeis.org/A250089
# http://rosettacode.org/wiki/Hamming_numbers

# good enough brutal generation
W = sorted(2**a * 3**b * 5**c for a,b,c in product(range(45), repeat=3))

# heap-based generation
def gen_smooth(n):
    H = [1]
    Seen = {1}  # to avoid duplicates
    for _ in range(n):
        x = heappop(H)
        yield x
        for d in (2,3,5):
            y = x*d
            if y not in Seen:
                heappush(H,y)
                Seen.add(y)

V = int(input())
print(sum(W[:V]))
