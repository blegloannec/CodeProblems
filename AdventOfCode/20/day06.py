#!/usr/bin/env python3

import sys

Alpha = 'abcdefghijklmnopqrstuvwxyz'

I = [L.strip() for L in sys.stdin.readlines()]
I.append('')

part1 = part2 = 0
S1 = set()
S2 = set(Alpha)
for L in I:
    if L:
        S = set(L)
        S1 |= S
        S2 &= S
    else:
        part1 += len(S1)
        part2 += len(S2)
        S1 = set()
        S2 = set(Alpha)
print(part1)
print(part2)
