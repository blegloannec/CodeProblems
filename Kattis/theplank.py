#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def tribo(n):
    if n<2:
        return 0 if n<0 else 1
    return tribo(n-1) + tribo(n-2) + tribo(n-3)

print(tribo(int(input())))
