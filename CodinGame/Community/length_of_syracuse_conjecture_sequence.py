#!/usr/bin/env python3

from functools import lru_cache

def syracuse(u):
    return u>>1 if u&1==0 else 3*u+1

@lru_cache(maxsize=None)
def preperiod(u):
    return 1 if u==1 else preperiod(syracuse(u))+1

if __name__=='__main__':
    N = int(input())
    for _ in range(N):
        A,B = map(int,input().split())
        u = max(range(A,B+1), key=preperiod)
        print(u, preperiod(u))
