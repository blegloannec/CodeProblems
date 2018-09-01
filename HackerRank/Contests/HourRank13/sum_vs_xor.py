#!/usr/bin/env python

import sys

# il faut interdire les retenues dans la somme
# on doit donc choisir 0 pour chaque 1 du nb d'origine
# le choix est libre pour chaque 0, 2^#0 solutions

n = int(sys.stdin.readline())
nb0 = 0
while n:
    nb0 += 1-n&1
    n >>= 1
print 1<<nb0
