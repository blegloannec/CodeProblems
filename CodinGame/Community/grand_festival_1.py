#!/usr/bin/env python3

N = int(input())
R = int(input())
P = [int(input()) for _ in range(N)]

# O(N*R) DP, implemented here as O(N * R^2) as the sum(P[.:.])
#            could be computed iteratively
DP = [0]*(N+1)
for n in range(1,N+1):
    DP[n] = max((DP[n-1-r] if n-1-r>=0 else 0) + sum(P[n-r:n]) for r in range(min(n,R)+1))
print(DP[N])
