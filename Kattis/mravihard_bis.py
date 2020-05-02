#!/usr/bin/env python3

# NB: Alternative version, using log and binary search.

from math import log, exp

def flow(u, fu):
    if K[u] is not None:
        return fu>=K[u]
    for v,x,t in T[u]:
        fv = fu+x
        if t and fv>0.:
            fv *= 2.
        if not flow(v, fv):
            return False
    return True

def main():
    global T, K
    N = int(input())
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b,x,t = map(int, input().split())
        a -= 1
        b -= 1
        T[a].append((b, log(x/100.), (t==1)))
    K = [None if k=='-1' else log(float(k)) for k in input().split()]
    l, r = 0.1, 2e9
    while r-l>1e-3:
        m = (l+r)/2.
        if flow(0, log(m)):
            r = m
        else:
            l = m
    print(l)

main()
