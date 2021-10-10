#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = A.copy()
    M = int(input())
    for _ in range(M):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        S[u] += A[v]
        S[v] += A[u]
    print(min(range(N), key=(lambda u: (S[u],u)))+1)

main()
