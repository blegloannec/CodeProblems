#!/usr/bin/env python3

import sys

# NB: "all k-mers from this strand of the chromosome are present,
# and their de Bruijn graph consists of exactly one simple cycle."

DNAS = [L.strip() for L in sys.stdin.readlines()]
DBG = {DNA[:-1]:DNA[1:] for DNA in DNAS}
X0,X = DNAS[0][:-1],DNAS[0][1:]
res = [X0[-1]]
while X!=X0:
    res.append(X[-1])
    X = DBG[X]
print(''.join(res))
