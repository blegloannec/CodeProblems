#!/usr/bin/env python3

N = int(input())
A = list(map(int,input().split()))
print(sum(int(A[i-1]>A[i]>A[i+1] or A[i-1]<A[i]<A[i+1]) for i in range(1,N-1)))
