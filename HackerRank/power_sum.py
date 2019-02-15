#!/usr/bin/env python3

memo = {}
def dp(x,i):
    if i<0:
        return int(x==0)
    if (x,i) not in memo:
        memo[x,i] = dp(x,i-1) + (dp(x-P[i],i-1) if P[i]<=x else 0)
    return memo[x,i]

if __name__=='__main__':
    X = int(input())
    N = int(input())
    P = []
    p = 1
    while p**N<=X:
        P.append(p**N)
        p += 1
    print(dp(X,len(P)-1))
