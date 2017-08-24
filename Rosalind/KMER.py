#!/usr/bin/env python3

from itertools import product
import rosalib

k = 4
D = {''.join(P):i for (P,i) in zip(product('ACGT',repeat=k),range(4**k))}
_,DNA = rosalib.parse_fasta()[0]
C = [0]*(4**k)
for i in range(len(DNA)-k+1):
    C[D[DNA[i:i+k]]] += 1
print(' '.join(map(str,C)))
