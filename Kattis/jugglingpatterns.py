#!/usr/bin/env python3

import sys

for L in sys.stdin.readlines():
    L = L.strip()
    P = list(map(int,L))
    N = len(P)
    S = sum(P)
    if S%N!=0:
        sys.stdout.write(f'{L}: invalid # of balls\n')
        continue
    C = [0]*N
    for i,t in enumerate(P):
        C[(i+t)%N] += 1
    if all(c==1 for c in C):
        sys.stdout.write(f'{L}: valid with {S//N} balls\n')
    else:
        sys.stdout.write(f'{L}: invalid pattern\n')
