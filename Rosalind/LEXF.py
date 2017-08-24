#!/usr/bin/env python3

from itertools import combinations_with_replacement

def next_permutation(T):
    pivot = len(T)-2
    while pivot>=0 and T[pivot]>=T[pivot+1]:
        pivot -= 1
    if pivot<0:
        return False
    swap = len(T)-1
    while T[swap]<=T[pivot]:
        swap -= 1
    T[swap],T[pivot] = T[pivot],T[swap]
    i = pivot+1
    j = len(T)-1
    while i<j:
        T[i],T[j] = T[j],T[i]
        i += 1
        j -= 1
    return True

A = input().split()
n = int(input())
L = []
for P in combinations_with_replacement(A,n):
    Q = list(P)
    L.append(''.join(Q))
    while next_permutation(Q):
        L.append(''.join(Q))
L.sort()
for P in L:
    print(P)
