#!/usr/bin/env python3

memo = {}
def goro(a,b):
    if a==b:
        return 1
    if a>b:
        a,b = b,a
    if a==1:
        return b
    if (a,b) not in memo:
        res1 = min(goro(a,b1)+goro(a,b-b1) for b1 in range(1,b))
        res2 = min(goro(a1,b)+goro(a-a1,b) for a1 in range(1,a))
        memo[a,b] = min(res1,res2)
    return memo[a,b]

H,W = map(int,input().split())
print(goro(H,W))
