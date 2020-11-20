#!/usr/bin/env python3

# Simple DP for the (easy) 1D version of:
# https://en.wikipedia.org/wiki/Cutting_stock_problem

L = int(input())
N = int(input())
DP = [0]*(L+1)
for _ in range(N):
    p,v = map(int, input().split())
    for l in range(p, L+1):
        DP[l] = max(DP[l], v+DP[l-p])
print(DP[L])
