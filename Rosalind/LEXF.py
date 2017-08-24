#!/usr/bin/env python3

from itertools import product

A = input().split()
n = int(input())
for P in product(A,repeat=n):
    print(''.join(P))
