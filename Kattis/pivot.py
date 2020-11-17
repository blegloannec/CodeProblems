#!/usr/bin/env python3

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
MaxPref = A.copy()
for i in range(1, N):
    MaxPref[i] = max(MaxPref[i-1], A[i])
MinSuff = A.copy()
for i in range(N-2, -1, -1):
    MinSuff[i] = min(A[i], MinSuff[i+1])
print(sum(1 for l,r in zip(MaxPref, MinSuff) if l==r))
