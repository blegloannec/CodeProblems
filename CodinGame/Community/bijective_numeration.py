#!/usr/bin/env python3

A = '123456789A'
B = len(A)

def bij2int(s):
    n = 0
    for c in s:
        n = B*n + A.index(c)+1
    return n

def int2bij(n):
    S = []
    while n:
        n -= 1
        n,x = divmod(n,B)
        S.append(A[x])
    return ''.join(reversed(S))

N = int(input())
print(int2bij(sum(bij2int(s) for s in input().split())))
