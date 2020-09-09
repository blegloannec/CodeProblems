#!/usr/bin/env python3

import sys
input = sys.stdin.readline

two = lambda n: n*(n-1)//2

N = int(input())
P,U = zip(*(map(int, input().split()) for _ in range(N)))
SP = sum(P)
M = two(SP) - sum(two(p) for p in P)
res = sum(U[i] * (M - P[i]*(SP-P[i])) for i in range(N))
print(res)
