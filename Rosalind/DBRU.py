#!/usr/bin/env python3

import sys, rosalib

S = set()
for L in sys.stdin.readlines():
    DNA = L.strip()
    S.add(DNA)
    S.add(rosalib.revc(DNA))
for DNA in S:
    print('(%s, %s)' % (DNA[:-1],DNA[1:]))
