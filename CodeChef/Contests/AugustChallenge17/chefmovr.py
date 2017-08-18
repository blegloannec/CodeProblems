#!/usr/bin/env python3

def mover(D,A):
    v = None
    res = 0
    for i in range(D):
        B = A[i::D]
        n = len(B)
        m = sum(B)
        if m%n!=0:
            return -1
        m //= n
        if v==None:
            v = m
        elif v!=m:
            return -1
        for j in range(n-1):
            d = m-B[j]
            B[j] += d  # useless
            B[j+1] -= d
            res += abs(d)
    return res

def main():
    T = int(input())
    for _ in range(T):
        N,D = map(int,input().split())
        A = list(map(int,input().split()))
        print(mover(D,A))

main()
