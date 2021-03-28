#!/usr/bin/env python3

def dot(A, B):
    res = a = b = 0
    while a<len(A):
        c = min(A[a], B[b])
        res += c*A[a+1]*B[b+1]
        A[a] -= c
        B[b] -= c
        if A[a]==0: a += 2
        if B[b]==0: b += 2
    return res

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(dot(A, B))

main()
