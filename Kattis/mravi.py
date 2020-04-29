#!/usr/bin/env python3

# NB: no need to log everything as the input Xi <= 100 & expected L <= 2e9
# As all Xi >= 1, all flows will be >=1 so that squaring is ALWAYS better.
# We assumed the root is always 0 and the edges are given in the downward
# direction (from root, towards leaves), which was not clear in the statement.

from math import sqrt

def flow(u=0):
    if K[u]>0:
        return K[u]
    fu = 0
    for v,x,t in T[u]:
        fv = flow(v)
        fu = max(fu, 100./x * (sqrt(fv) if t else fv))
    return fu

def main():
    global T, K
    N = int(input())
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b,x,t = map(int, input().split())
        a -= 1
        b -= 1
        T[a].append((b, x, (t==1)))
    K = list(map(int, input().split()))
    print(flow())

main()
