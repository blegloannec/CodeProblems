#!/usr/bin/env python3

N = int(input())
A = [input() for _ in range(N)]
H = len(A)
W = max(len(L) for L in A)
O = [[' ']*(W+2) for _ in range(H+2)]
for i in range(H):
    for j in range(len(A[i])):
        if A[i][j]!=' ':
            O[i][j] = A[i][j]
            O[i+1][j+1] = '-'
            O[i+2][j+2] = '`'
print('\n'.join(''.join(L).rstrip() for L in O))
