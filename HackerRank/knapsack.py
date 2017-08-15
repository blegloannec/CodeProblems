#!/usr/bin/env python3

import sys
sys.setrecursionlimit(3000)

memo = {}
def dp(i,k):
    if i<0:
        return 0
    if (i,k) in memo:
        return memo[i,k]
    res = dp(i-1,k)
    if A[i]<=k:
        res = max(res,A[i]+dp(i,k-A[i]))
    memo[i,k] = res
    return res

def main():
    global A
    T = int(input())
    for _ in range(T):
        n,k = map(int,input().split())
        A = list(map(int,input().split()))
        print(dp(n-1,k))
        memo.clear()

main()
