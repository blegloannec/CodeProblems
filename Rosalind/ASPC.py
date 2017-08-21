#!/usr/bin/env python3

M = 10**6

n,m = map(int,input().split())
C = [[0]*(n+1),[0]*(n+1)]
C[0][0] = C[1][0] = 1
for i in range(1,n+1):
    for k in range(1,i+1):
        C[i%2][k] = (C[(i-1)%2][k-1] + C[(i-1)%2][k]) % M
res = 0
for k in range(m,n+1):
    res = (res + C[n%2][k])%M
print(res)
