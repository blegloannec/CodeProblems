#!/usr/bin/env python3

C = list(map(int,input().split()))
K = int(input())
T = [0]*(K+1)
T[0] = 1
for i in range(10):
    for k in range(K,0,-1):
        T[k] += T[k-1]*C[i]
print(T[K])
