#!/usr/bin/env python3

N = int(input())
H = [int(input()) for _ in range(N)]
DP = H[:]
if N>1:
    DP[1] = max(0,H[0],H[1])
    for i in range(2,N):
        DP[i] = max(H[i]+DP[i-2], DP[i-1])
print(DP[N-1])
