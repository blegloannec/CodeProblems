#!/usr/bin/env python3

import sys

M = 100

def minmaxpair(A, B):
    res = 0
    b = M
    for a in range(1,M+1):
        while A[a]>0:
            if B[b]>0:
                m = min(A[a], B[b])
                A[a] -= m
                B[b] -= m
                res = max(res, a+b)
            if B[b]==0:
                b -= 1
    return res

def main():
    N = int(sys.stdin.readline())
    A = [0]*(M+1)
    B = [0]*(M+1)
    for _ in range(N):
        a,b = map(int, sys.stdin.readline().split())
        A[a] += 1
        B[b] += 1
        res = minmaxpair(A[:], B[:])
        sys.stdout.write(f'{res}\n')

main()
