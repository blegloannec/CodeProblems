#!/usr/bin/env python3

N,M = map(int,input().split())
S = {}
for _ in range(N):
    L,R = input().split(' -> ')
    S[L] = R
U = input()
for _ in range(M):
    U = ''.join(S[a] if a in S else a for a in U)
print(U)
