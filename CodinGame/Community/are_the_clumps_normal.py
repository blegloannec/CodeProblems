#!/usr/bin/env python3

from itertools import groupby

clumps = lambda N,B: sum(1 for _ in groupby(map(int,N), key=(lambda D: D%B)))

N = input()
C = [clumps(N,B) for B in range(1,10)]
try:
    B = next(B for B in range(2,10) if C[B-2]>C[B-1])
except StopIteration:
    B = 'Normal'
print(B)
