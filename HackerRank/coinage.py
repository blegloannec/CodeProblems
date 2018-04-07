#!/usr/bin/env python3

# Lots of acceptable computation splitting tradeoffs here
# We use a loop for A in O(N) per testcase
#      + a DP for B,C,D in O(N^3/100) ~ 10^7 globally

memo = {}
def dp(N,B,C,D):
    B,C,D = min(B,N//2),min(C,N//5),min(D,N//10)
    if N==0:
        return 1
    if (N,B,C,D) in memo:
        return memo[N,B,C,D]
    res = 0
    if D:
        res = dp(N-10,B,C,D-1) + dp(N,B,C,0)
    elif C:
        res = dp(N-5,B,C-1,0) + dp(N,B,0,0)
    elif B:
        res = dp(N-2,B-1,0,0)
    memo[N,B,C,D] = res
    return res

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A,B,C,D = map(int,input().split())
        res = 0
        for a in range(min(N,A)+1):
            res += dp(N-a,B,C,D)
        print(res)

main()
