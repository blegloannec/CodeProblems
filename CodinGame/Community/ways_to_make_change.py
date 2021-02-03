#!/usr/bin/env python3

N = int(input())
S = int(input())
DP = [0]*(N+1)
DP[0] = 1
for v in map(int, input().split()):
    for n in range(v, N+1):
        DP[n] += DP[n-v]
print(DP[N])
