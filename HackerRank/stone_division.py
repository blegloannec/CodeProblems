#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def grundy(n):
    g = 0
    G = []
    for s in S:
        if n%s==0:
            G.append(0 if s&1==0 else grundy(n//s))
        while g in G:
            g += 1
    return g

def main():
    global S
    N,M = map(int,input().split())
    S = list(map(int,input().split()))
    print('First' if grundy(N)!=0 else 'Second')

main()
