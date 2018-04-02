#!/usr/bin/env python3

from math import *

D = {1:1, 2:2, 6:3, 24:4, 120:5, 720:6}

n = input()

if len(n)<4:
    print(D[int(n)])
else:
    lf = 0.
    i = 0
    while ceil(lf)<len(n):
        i += 1
        lf += log10(i)
    print(i)
