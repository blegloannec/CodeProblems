#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Lucas%27s_theorem

T = int(input())
for _ in range(T):
    N,P = map(int,input().split())
    n = N
    non0 = 1
    while n:
        n,d = divmod(n,P)
        non0 *= d+1
    print(N+1 - non0)
