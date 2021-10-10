#!/usr/bin/env python3

# NB: is it also https://oeis.org/A062200

from functools import lru_cache

MOD = 10**9+7

@lru_cache(maxsize=None)
def cnt_a(n):
    if n==0: return 0
    if n==1: return 1
    return (cnt_b(n-1) + cnt_a(n-2)) % MOD

def cnt_b(n):
    if n==0: return 1
    if n==1: return 0
    return cnt(n-2)

@lru_cache(maxsize=None)
def cnt(n):
    return (cnt_a(n) + cnt_b(n)) % MOD

print(cnt(int(input())))
