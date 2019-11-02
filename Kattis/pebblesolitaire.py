#!/usr/bin/env python3

from functools import lru_cache

S = 12

@lru_cache(maxsize=None)
def final(C):
    res = sum((C>>i)&1 for i in range(S))
    for b in range(S-2):
        c = (C>>b) & 0b111
        if c==0b011 or c==0b110:
            res = min(res, final(C^(0b111<<b)))
    return res

def main():
    N = int(input())
    for _ in range(N):
        C0 = int(input().replace('-','0').replace('o','1'),2)
        print(final(C0))

main()
