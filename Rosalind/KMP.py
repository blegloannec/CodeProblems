#!/usr/bin/env python3

import rosalib

def prefs(B): # fonction prefixe de KMP
    P = [0]*(len(B)+1)
    P[0] = -1
    k = -1
    for i in range(1,len(B)+1):
        while k>=0 and B[i-1]!=B[k]:
            k = P[k]
        k += 1
        P[i] = k
    return P

L = rosalib.parse_fasta()
_,S = L[0]
P = prefs(S)
print(' '.join(map(str,P[1:])))
