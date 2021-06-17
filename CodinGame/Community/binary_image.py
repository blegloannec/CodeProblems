#!/usr/bin/env python3

N = int(input())
O = []
for _ in range(N):
    L = list(map(int, input().split()))
    O.append(''.join('.O'[i&1]*l for i,l in enumerate(L)))
print('\n'.join(O) if all(len(L)==len(O[0]) for L in O) else 'INVALID')
