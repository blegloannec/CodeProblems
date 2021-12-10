#!/usr/bin/env python3

import sys

LC = '([{<'
RC = ')]}>'
Scr = [3,57,1197,25137]

I = [L.strip() for L in sys.stdin.readlines()]

part1 = 0
Part2 = []
for L in I:
    S = []
    corrupt = False
    for c in L:
        i = RC.find(c)
        if i<0:
            S.append(c)
        elif not (S and S.pop()==LC[i]):
            part1 += Scr[i]
            corrupt = True
            break
    if not corrupt:
        comp = 0
        for c in reversed(S):
            comp = 5*comp + LC.index(c)+1
        Part2.append(comp)
print(part1)
Part2.sort()
print(Part2[len(Part2)//2])
