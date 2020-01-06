#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def dp(l,r):
    if l>=r:
        return 0
    K = M[l][0] * M[r][1]
    return min(dp(l,m) + dp(m+1,r) + K*M[m][1] for m in range(l,r))

def main():
    global M
    N = int(input())
    M = [tuple(map(int,input().split())) for _ in range(N)]
    print(dp(0,N-1))

main()
