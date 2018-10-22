#!/usr/bin/env python3

def possible(A):
    F = [i for i in range(1,len(A)) if A[i-1]>A[i]]
    if len(F)!=1:
        return len(F)==0
    f = F[0]
    return min(A[:f])>=max(A[f:])

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print('YES' if possible(A) else 'NO')

main()
