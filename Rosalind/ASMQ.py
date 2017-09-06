#!/usr/bin/env python3

import sys
from collections import defaultdict

def N(XX,DNAS):
    assert(0<XX<100)
    S = 0
    Cpt = defaultdict(int)
    for DNA in DNAS:
        S += len(DNA)
        Cpt[len(DNA)] += 1
    l = 0
    for L in sorted(Cpt,reverse=True):
        l += L*Cpt[L]
        if 100*l>=XX*S:
            return L

DNAS = [L.strip() for L in sys.stdin.readlines()]
print(N(50,DNAS),N(75,DNAS))
