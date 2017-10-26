#!/usr/bin/env python3

from collections import deque

def simu(k,A):
    M = max(A)
    v = 0
    while A[0]<M and v<k:
        if A[0]>A[1]:
            v += 1
            A.append(A[1])
            A[1] = A[0]
        else:
            v = 1
            A.append(A[0])
        A.popleft()
    return A[0]

def main():
    n,k = map(int,input().split())
    A = deque(map(int,input().split()))
    print(simu(k,A))

main()
