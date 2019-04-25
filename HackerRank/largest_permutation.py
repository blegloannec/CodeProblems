#!/usr/bin/env python3

N,K = map(int,input().split())
A = list(map(int,input().split()))

Idx = [0]*(N+1)
for i in range(N):
    Idx[A[i]] = i

for i in range(N):
    v = N-i
    if A[i]!=v:
        j = Idx[v]
        A[i],A[j] = A[j],A[i]
        Idx[A[j]] = j
        K -= 1
        if K==0:
            break
print(*A)
