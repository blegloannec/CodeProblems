#!/usr/bin/env python3

N = int(input())
R = int(input())
P = [int(input()) for _ in range(N)]

# O(N*R) DP, implemented here as O(N * R^2) as the sum(P[.:.])
#            could be computed iteratively
DP = [0]*(N+1)
Streak = [0]*(N+1)
for n in range(1,N+1):
    for r in range(min(n,R)+1):
        s = (DP[n-1-r] if n-1-r>=0 else 0) + sum(P[n-r:n])
        if s>DP[n]:
            DP[n] = s
            Streak[n] = r
n = N
O = []
while n>=0:
    O += list(range(n,n-Streak[n],-1))
    n -= Streak[n]+1
O.reverse()
print('>'.join(map(str,O)))
