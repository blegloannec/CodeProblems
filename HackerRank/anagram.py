#!/usr/bin/env python3

from collections import Counter

T = int(input())
for _ in range(T):
    S = input()
    res = -1
    if len(S)%2==0:
        s = len(S)//2
        C = Counter(S[:s])
        C.subtract(S[s:])
        res = sum(C[i] for i in C if C[i]>0)
    print(res)
