#!/usr/bin/env python3

import sys

for L in sys.stdin.readlines():
    a,b,c = map(int,L.split())
    D = ['0.']
    for _ in range(c):
        q,a = divmod(10*a,b)
        D.append(str(q))
    print(''.join(D))
