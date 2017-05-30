#!/usr/bin/env python3

n = int(input())
A = list(map(int,input().split()))
print(abs(sum(A[:n//2])-sum(A[n//2:])))
