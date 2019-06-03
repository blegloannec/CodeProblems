#!/usr/bin/env python3

from functools import lru_cache

def bird(x):
    return x>>1 if x&1==0 else (3*x+1)>>1

@lru_cache(maxsize=None)
def length(x):
    return 1 if x==1 else 1+length(bird(x))

xmax = 3000
lmax = max(length(x) for x in range(2,xmax))
print(lmax)
print(*[x for x in range(2,xmax) if length(x)>=lmax-30])
