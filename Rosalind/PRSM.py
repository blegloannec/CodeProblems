#!/usr/bin/env python3

import sys, rosalib
from collections import *

def arrondi(x):
    return round(x,5)

# on ne compte pas 0 et on ne compte la masse totale qu'une fois
# (il s'agit des masses que l'on peut mesurer en decoupant les molecules en 2)
def complete_spectrum(P):
    S = defaultdict(int)
    w = 0
    for i in range(len(P)-1):  # prefixes
        w += rosalib.W[P[i]]
        S[arrondi(w)] += 1
    w = 0
    for a in reversed(P):  # suffixes
        w += rosalib.W[a]
        S[arrondi(w)] += 1
    return S

def convolution_max_mult_shift(S1,S2):
    D = defaultdict(int)
    m = None
    for x in S1:
        for y in S2:
            d = arrondi(x-y)
            D[d] += S1[x]*S2[y]
            if m==None or D[d]>D[m]:
                m = d
    return (m,D[m])

def main():
    n = int(input())
    S = [input() for _ in range(n)]
    R = Counter(arrondi(float(L)) for L in sys.stdin.readlines())
    M = -1
    for P in S:
        _,m = convolution_max_mult_shift(R,complete_spectrum(P))
        if m>M:
            M = m
            best = P
    print(M)
    print(best)

main()
