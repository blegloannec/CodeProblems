#!/usr/bin/env python3

n,x = map(int,input().split())
A = list(map(int,input().split()))
print('YES' if sum(A)+len(A)-1==x else 'NO')
