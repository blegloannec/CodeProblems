#!/usr/bin/env python3

import rosalib
from collections import Counter

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

_,RNA = rosalib.parse_fasta()[0]
C = Counter(RNA)
minAU,maxAU = (C['A'],C['U']) if C['A']<=C['U'] else (C['U'],C['A'])
minCG,maxCG = (C['C'],C['G']) if C['C']<=C['G'] else (C['G'],C['C'])
nbmatch = binom(maxAU,minAU)*fact(minAU) * binom(maxCG,minCG)*fact(minCG)
print(nbmatch)
