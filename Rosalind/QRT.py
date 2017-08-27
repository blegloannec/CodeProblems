#!/usr/bin/env python3

import sys
from itertools import combinations

L = sys.stdin.readlines()
S = L[0].split()  # species
T = [L[i].strip() for i in range(1,len(L))]  # char table
Q = set()
for C in T:
    L = [[],[]]  # 0s and 1s for partial character C
    for i in range(len(C)):
        if C[i]!='x':
            L[int(C[i])].append(i)
    if len(L[0])>=2 and len(L[1])>=2:  # quartet
        for A in combinations(L[0],2):
            for B in combinations(L[1],2):
                # the split A | B is a quartet
                Q.add((A,B) if A<=B else (B,A))
for (A,B) in Q:
    print('{%s} {%s}' % (', '.join(S[i] for i in A),', '.join(S[i] for i in B)))
