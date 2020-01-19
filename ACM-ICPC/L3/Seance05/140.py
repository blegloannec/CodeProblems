#!/usr/bin/env python3

# raw brute-force search, good enough considering the input size
# (a significantly more efficient backtracking should be possible)

from itertools import permutations

def min_bandwidth():
    bmin = 1000
    for P in permutations(U):
        b = max(abs(P.index(u)-P.index(v)) for u,v in E)
        if b<bmin:
            bmin, Pmin = b, P[:]
            if b==1:
                break
    return bmin, Pmin

if __name__=='__main__':
    L = input()
    while L!='#':
        U = set()
        E = []
        for R in L.split(';'):
            u,V = R.split(':')
            U.add(u)
            for v in V:
                U.add(v)
                E.append((u,v))
        U = sorted(U)
        b,P = min_bandwidth()
        print('{} -> {}'.format(' '.join(map(str,P)),b))
        L = input()
