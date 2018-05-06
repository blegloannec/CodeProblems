#!/usr/bin/env python3

import sys

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = [True]*N
        C = [0]*N
        for _ in range(N):
            L = list(map(int,input().split()))
            D = L[0]
            if D<0:
                return
            ID = L[1:]
            for i in ID:
                C[i] += 1
            p = min((i for i in ID if A[i]), key=(lambda i: C[i]), default=-1)
            if p>=0:
                A[p] = False
            print(p)
            sys.stdin.flush()

main()
