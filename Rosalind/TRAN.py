#!/usr/bin/env python3

import rosalib

Transi = set([('A','G'),('G','A'),('C','T'),('T','C')])

def ratio(A,B):
    assert(len(A)==len(B))
    tri = trv = 0
    for i in range(len(A)):
        if (A[i],B[i]) in Transi:
            tri += 1
        elif A[i]!=B[i]:
            trv += 1
    return tri/trv

L = rosalib.parse_fasta()
print(ratio(L[0][1],L[1][1]))
