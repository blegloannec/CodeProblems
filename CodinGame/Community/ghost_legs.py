#!/usr/bin/env python3

W,H = map(int,input().split())
T = input().split()
N = len(T)

P = list(range(N))
for _ in range(H-2):
    L = input().split('|')
    for i in range(1,N):
        if L[i][0]=='-':
            P[i-1],P[i] = P[i],P[i-1]

Pinv = [None]*N
for i in range(N):
    Pinv[P[i]] = i

B = input().split()
for i in range(N):
    print(T[i]+B[Pinv[i]])
