#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Euler%27s_criterion

N = int(input())
for _ in range(N):
    a,p = map(int,input().split())
    a %= p
    sol = p==2 or a==0 or pow(a,p>>1,p)==1
    print('yes' if sol else 'no')
