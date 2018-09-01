#!/usr/bin/env python3

n = int(input())
A = list(map(int,input().split()))
m,i = 0,0
while i<len(A):
    i += A[i]+1
    m += 1
print(m)
