#!/usr/bin/env python3

# https://fr.wikipedia.org/wiki/M%C3%B6lkky

from functools import lru_cache

@lru_cache(maxsize=None)
def dp(n, r=4):
    if n==50: return 1
    if r==0:  return 0
    return dp(n+1,r-1) + 2*sum(dp(m,r-1) for m in range(n+2,min(n+12,50)+1))

n = int(input())
print(dp(n))
