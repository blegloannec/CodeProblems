#!/usr/bin/env python3

import sys

S1 = S2 = 0
for L in sys.stdin.readlines():
    S = int(L)//3-2
    S1 += S
    while S>0:
        S2 += S
        S = S//3-2
print(S1)
print(S2)
