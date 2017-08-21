#!/usr/bin/env python3

n = int(input())
A = set(map(int,input()[1:-1].split(',')))
B = set(map(int,input()[1:-1].split(',')))
E = set(range(1,n+1))
print(A|B)
print(A&B)
print(A-B)
print(B-A)
print(E-A)
print(E-B)
