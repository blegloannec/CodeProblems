#!/usr/bin/env python3

# NB: In this harder version, precision becomes a problem
#     and squaring is only interesting if the flow is > 1.

from decimal import Decimal

def flow(u=0):
    if K[u] is not None:
        return K[u]
    fu = Decimal(0)
    for v,x,t in T[u]:
        fv = flow(v)
        if t and fv>1.:
            fv = fv.sqrt()
        fu = max(fu, fv*x)
    return fu

def main():
    global T, K
    N = int(input())
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b,x,t = map(int, input().split())
        a -= 1
        b -= 1
        T[a].append((b, Decimal(100)/Decimal(x), (t==1)))
    K = [None if k=='-1' else Decimal(k) for k in input().split()]
    print(flow())

main()
