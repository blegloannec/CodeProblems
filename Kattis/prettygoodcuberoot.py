#!/usr/bin/env python3

import sys

for L in sys.stdin.readlines():
    N = int(L)
    l, r = 0, 10**167
    while r-l>1:
        m = (l+r)//2
        if m*m*m<N:
            l = m
        else:
            r = m
    print(l if N-l*l*l < r*r*r-N else r)
