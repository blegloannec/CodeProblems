#!/usr/bin/env python3

import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    N = int(input())
    T = sorted(map(int, input().split()))
    DP = [0]*(N+1)
    for i in range(N-1,-1,-1):
        DP[i] = DP[i+1]
        for k in (2,3,4):
            j = bisect_left(T, T[i]+k*10**5)
            DP[i] = max(DP[i], k+DP[j])
    print(DP[0])

main()
