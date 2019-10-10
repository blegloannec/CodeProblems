#!/usr/bin/env python3

from functools import lru_cache

# from Lucas' thm, binom(n,p) is odd iff
# each bit 0 of n has a corresponding bit 0 in p

@lru_cache(maxsize=None)
def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

def full_cnt(k):
    return sum(binom(k,p) * 2**p for p in range(k+1))

def odd_binom_cnt(n):
    k = 0
    C = 1
    while n:
        if n&1:
            C += C + full_cnt(k)
        n >>= 1
        k += 1
    return C

n = int(input())
print(odd_binom_cnt(n-1))
