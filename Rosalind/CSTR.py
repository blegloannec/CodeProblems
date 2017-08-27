#!/usr/bin/env python3

import sys

DNAS = [L.strip() for L in sys.stdin.readlines()]
S,L = len(DNAS),len(DNAS[0])
CharTbl = []
for i in range(L):
    C = [int(DNAS[j][i]==DNAS[0][i]) for j in range(S)]
    if 1<sum(C)<S-1:  # nontrivial char
         CharTbl.append(C)
for C in CharTbl:
    print(''.join(map(str,C)))
