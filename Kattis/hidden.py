#!/usr/bin/env python3

from collections import Counter

def test(P,S):
    C = Counter(P)
    i = 0
    for b in S:
        if b==P[i]:
            C[b] -= 1
            i += 1
            if i==len(P):
                return True
        elif C[b]>0:
            return False
    return False

P,S = input().split()
print('PASS' if test(P,S) else 'FAIL')
