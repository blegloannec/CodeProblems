#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    Suff = A[:]
    for i in range(N-2, -1, -1):
        Suff[i] += Suff[i+1]
    res = S2 = 0
    for i in range(N-1):
        S2 += A[i]*A[i]
        res = max(res, S2*Suff[i+1])
    print(res)

main()
