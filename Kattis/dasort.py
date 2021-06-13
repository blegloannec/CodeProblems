#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        K,N = map(int, input().split())
        A = []
        while len(A)<N:
            A.extend(map(int, input().split()))
        S = sorted(A, reverse=True)
        for a in A:
            if a==S[-1]:
                S.pop()
        print(K, len(S))

main()
