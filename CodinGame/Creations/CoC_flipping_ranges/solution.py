#!/usr/bin/env python3

# O(N+Q) approach, O(N) space
N,Q = map(int,input().split())
A = [0]*N
for _ in range(Q):
    L,R = map(int,input().split())
    A[L] += 1
    if R+1<N:
        A[R+1] -= 1

x = res = 0
for i in range(N):
    x += A[i]
    res += x%2
print(res)
