#!/usr/bin/env python3

R = int(input())
C = {a: f'{i}{j}' for i in range(R) for j,a in enumerate(input().split())}
print(''.join(C[a] for a in input()))
