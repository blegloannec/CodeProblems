#!/usr/bin/env python3

# prefixSum(i) + suffixSum(i) = sum(A) + A[i]

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    print(A.index(min(A))+1)
