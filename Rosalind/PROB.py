#!/usr/bin/env python3

from math import log10

S = input()
A = list(map(float,input().split()))
B = [1.]*len(A)
for i in range(len(A)):
    for c in S:
        if c=='C' or c=='G':
            B[i] *= A[i]/2
        else:
            B[i] *= (1-A[i])/2
    B[i] = log10(B[i])
print(' '.join(map(str,B)))
