#!/usr/bin/env python3

n = int(input())
y = int(input())
S,H = [0]*n,[0]*n
for i in range(n):
    S[i],H[i],_ = map(int,input().split())

A = sum(H)+sum(S)
for _ in range(y):
    for i in range(n):
        A -= S[i]
        S[i] = min(2*S[i],H[i])
        H[i] -= S[i]
    print(A)
    if not A:
        break
