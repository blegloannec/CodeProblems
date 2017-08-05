#!/usr/bin/env python3

N = int(input())
K = int(input())
A = sorted(int(input()) for _ in range(N))
print(min(A[i+K-1]-A[i] for i in range(N-K+1)))
