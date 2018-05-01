#!/usr/bin/env python3

M = 10000
P = 10**9+7

# PRECOMP
# N(n) = N(n-1) + N(n-2)
#       (..0    + ..01    -> fibonacci)
N = [1,2]
for i in range(2,M+1):
    N.append((N[-2]+N[-1])%P)

# MAIN
T = int(input())
for _ in range(T):
    print(N[int(input())])
