#!/usr/bin/env python3

n = int(input())
A = list(map(int,input().split()))
cpt = sum(int(A[i-1]>A[i]<A[i+1] or A[i-1]<A[i]>A[i+1]) for i in range(1,n-1))
print(cpt)
