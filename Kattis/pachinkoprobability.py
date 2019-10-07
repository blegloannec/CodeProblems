#!/usr/bin/env python3

import sys
sys.setrecursionlimit(5000)
from functools import lru_cache

@lru_cache(maxsize=None)
def paths(u):
    return sum(paths(v) for v in Pred[u]) if Pred[u] else 1

def main():
    global Pred
    N = int(input())
    M = int(input())
    Pred = [[] for _ in range(N)]
    Succ = [0]*N
    for _ in range(M):
        u,v = map(int,input().split())
        Pred[v].append(u)
        Succ[u] += 1
    K = int(input())
    Outs = [int(input()) for _ in range(K)]
    print('winning paths', sum(paths(o) for o in Outs))
    print('total paths', sum(paths(u) for u in range(N) if Succ[u]==0))

main()
