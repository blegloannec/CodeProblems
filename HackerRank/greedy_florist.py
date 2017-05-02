#!/usr/bin/env python3

N,K = map(int,input().split())
C = list(map(int,input().split()))
C.sort(reverse=True)
res = 0
for i in range(N):
    res += C[i]*(1+i//K)
print(res)
