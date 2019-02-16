#!/usr/bin/env python3

S = int(input())
A = ((int(input())-45)//90)%4
T = [input().split() for _ in range(S)]
O = [[' ']*(2*S-1) for _ in range(2*S-1)]
for i in range(S):
    for j in range(S):
        if   A==0: O[i-j+S-1][i+j]    = T[i][j]
        elif A==1: O[-i-j-1][i-j+S-1] = T[i][j]
        elif A==2: O[j-i+S-1][-i-j-1] = T[i][j]
        elif A==3: O[i+j][j-i+S-1]    = T[i][j]
print('\n'.join(''.join(L) for L in O))
