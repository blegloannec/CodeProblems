#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def count(k,t):
    assert k <= t <= 6*k
    if k==0:
        return 1
    res = 0
    for d in range(1,7):
        if k-1 <= t-d <= 6*(k-1):
            res += count(k-1,t-d)
    return res

def best_pick(K, Target, Dice):
    diff = Target - sum(Dice)
    if diff==0:
        return 0
    Sums = [set() for _ in range(K+1)]
    Sums[0].add(0)
    for k in range(1,K+1):
        for l in range(k,0,-1):
            for s in Sums[l-1]:
                Sums[l].add(s+Dice[k-1])
    pmax = 0.
    for k in range(1,K+1):
        for s in Sums[k]:
            dt = diff + s
            if k <= dt <= 6*k:
                p = count(k,dt) / 6**k
                if p > pmax:
                    pmax, kmax = p, k
    return kmax

def main():
    K,T = map(int,input().split())
    D = list(map(int,input().split()))
    print(best_pick(K,T,D))

main()
