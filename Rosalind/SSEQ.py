#!/usr/bin/env python3

import rosalib

def subseq(S,T):
    P = []
    i = j = 0
    while i<len(S) and j<len(T):
        if S[i]==T[j]:
            P.append(i+1)
            j += 1
        i += 1
    return P if j==len(T) else None

L = rosalib.parse_fasta()
S,T = L[0][1],L[1][1]
print(' '.join(map(str,subseq(S,T))))
