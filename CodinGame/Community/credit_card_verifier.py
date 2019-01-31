#!/usr/bin/env python3

N = int(input())
for _ in range(N):
    C = list(map(int,input().replace(' ','')))
    valid = (sum(2*c-9 if c>=5 else 2*c for c in C[::2]) + sum(C[1::2]))%10==0
    print('YES' if valid else 'NO')
