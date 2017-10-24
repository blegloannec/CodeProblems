#!/usr/bin/env python3

S = input()
N = len(S)
T = [[0]*(N+1) for _ in range(3)]
for i in range(1,N+1):
    T[0][i] = T[0][i-1] + int(S[i-1]=='a')
    T[1][i] = max(T[1][i-1] + int(S[i-1]=='b'), T[0][i])
    T[2][i] = max(T[2][i-1] + int(S[i-1]=='a'), T[1][i], T[0][i])
print(T[2][N])
