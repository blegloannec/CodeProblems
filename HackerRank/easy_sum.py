#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    N,m = map(int,input().split())
    q,r = divmod(N,m)
    # O(1) formula
    res = m*(m-1)//2 * q + r*(r+1)//2
    print(res)
