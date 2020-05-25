#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    SB = [0]*3
    for i in range(N):
        SB[i%3] += B[i]
    C = [0]*3
    for i in range(N):
        for c in range(3):
            C[c] += A[i] * SB[(c-i+1)%3]
    print(*C)

main()
