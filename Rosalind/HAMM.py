#!/usr/bin/env python3

def hamming(A,B):
    assert(len(A)==len(B))
    return sum(int(A[i]!=B[i]) for i in range(len(A)))

A = input()
B = input()
print(hamming(A,B))
