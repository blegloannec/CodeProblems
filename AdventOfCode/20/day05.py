#!/usr/bin/env python3

import sys

SID = lambda s: int(s.translate(str.maketrans('FBLR','0101')), 2)

I = sorted(SID(L.strip()) for L in sys.stdin.readlines())
print(I[-1])

for i in range(len(I)-1):
    if I[i+1] == I[i]+2:
        print(I[i]+1)
