#!/usr/bin/env python3

L = int(input())
N = int(input())
B = sorted(map(int, input().split()), reverse=True)

INF = float('inf')
DP = [[INF]*(L+1)]
DP[0][0] = 0
for n in range(1, N+1):
    b = B[n-1]
    DP.append(DP[n-1].copy())
    for l in range(b, L+1):
        DP[n][l] = min(DP[n][l], DP[n-1][l-b]+1)

l = next(l for l in range(L, -1, -1) if DP[N][l] < INF)
n = N
Sol = []
while l > 0:
    b = B[n-1]
    if l >= b and DP[n-1][l-b] < DP[n][l]:
        Sol.append(b)
        l -= b
    n -= 1
print(*Sol)
