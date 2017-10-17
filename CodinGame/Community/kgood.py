#!/usr/bin/env python3

S = [ord(c)-ord('a') for c in input()]
K = int(input())

C = [0]*26
k = L = 0
l = -1
for r in range(len(S)):
    if C[S[r]]==0:
        k += 1
    C[S[r]] += 1
    while k>K:
        l += 1
        C[S[l]] -= 1
        if C[S[l]]==0:
            k -= 1
    L = max(L,r-l)
print(L)
