#!/usr/bin/env python3

from itertools import groupby

def encode(M):
    B = []
    for a,g in groupby(M):
        B.append('0'*(2-int(a)))
        B.append('0'*len(list(g)))
    return ' '.join(B)

M = ''.join('{:07b}'.format(ord(c)) for c in input())
print(encode(M))
