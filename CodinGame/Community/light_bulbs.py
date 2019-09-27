#!/usr/bin/env python3

# solves inputs of size ~10^4 in < 0.1s

import sys
sys.setrecursionlimit(30000)  # for very large input sizes
from functools import lru_cache

@lru_cache(maxsize=None)
def switch(S,T,N):
    if N==0:     return 0
    if S&1==T&1: return switch(S>>1, T>>1, N-1)
    return switch(S>>1, 1, N-1) + 1 + switch(1, T>>1, N-1)

S = input()
T = input()
N = len(S)
print(switch(int(S[::-1],2), int(T[::-1],2), N))
