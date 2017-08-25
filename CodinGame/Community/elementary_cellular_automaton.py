#!/usr/bin/env python3

R = int(input())
N = int(input())
C = [[int(c=='@') for c in input()]]
S = len(C[0])
for _ in range(N-1):
    C.append([(R>>((C[-1][(i-1)%S]<<2)|(C[-1][i]<<1)|C[-1][(i+1)%S]))&1 for i in range(S)])
for L in C:
    print(''.join('@' if c else '.' for c in L))
