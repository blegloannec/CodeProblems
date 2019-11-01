#!/usr/bin/env python3

S = input()
L = len(S)
res = L
for l in range(2,L//2+1):
    for i in range(L-l):
        res = min(res, L+l-(l-1)*S.count(S[i:i+l]))
print(res)
