#!/usr/bin/env python3

from math import sqrt

# dp(P,i) = largest value <= P reachable using intervals I[0],...,I[i]
# (analog to knapsack)
memo = {}
def dp(P,i):
    if i<0:
        return 0
    if (P,i) in memo:
        return memo[P,i]
    res = dp(P,i-1)
    l,r = I[i]
    if res<P and l<=P:
        res = max(res, min(P, r+dp(P-l,i-1)))
    memo[P,i] = res
    return res

def main():
    global I
    T = int(input())
    for t in range(1,T+1):
        N,P = map(int,input().split())
        R = [tuple(map(int,input().split())) for _ in range(N)]
        P0 = sum(2*(h+w) for (w,h) in R)
        I = [(2*min(w,h),2*sqrt(w*w+h*h)) for (w,h) in R]
        memo.clear()
        res = P0 + dp(P-P0,N-1)
        print('Case #%d: %f' % (t,res))

main()
