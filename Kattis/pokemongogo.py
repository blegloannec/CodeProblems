#!/usr/bin/env python3

from functools import lru_cache

dist = lambda x1,y1: lambda x2,y2: abs(x1-x2) + abs(y1-y2)

@lru_cache(maxsize=None)
def held_karp(seen, curr):
    dcurr = dist(X[curr], Y[curr])
    if seen==full:
        return dcurr(0,0)
    res = float('inf')
    for i in range(N):
        if seen&B[i]==0:
            res = min(res, dcurr(X[i], Y[i]) + held_karp(seen|B[i], i))
    return res

def main():
    global N,B,X,Y,full
    N = int(input())
    X = [None]*N
    Y = [None]*N
    B = []
    NameIdx = {}
    for i in range(N):
        X[i], Y[i], name = input().split()
        X[i], Y[i] = int(X[i]), int(Y[i])
        if name not in NameIdx:
            NameIdx[name] = len(NameIdx)
        B.append(1<<NameIdx[name])
    full = (1<<len(NameIdx))-1
    res = min(dist(0,0)(X[i],Y[i]) + held_karp(B[i],i) for i in range(N))
    print(res)

main()
