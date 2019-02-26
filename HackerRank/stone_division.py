#!/usr/bin/env python3

import sys
sys.setrecursionlimit(5000)

memo = {}
def dp(n):
    if n not in memo:
        res = 0
        for s in S:
            if s>=n:   break
            if n%s==0: res = max(res, 1+(n//s)*dp(s))
        memo[n] = res
    return memo[n]

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        N,M = map(int,input().split())
        S = sorted(map(int,input().split()))
        print(dp(N))
        memo.clear()
