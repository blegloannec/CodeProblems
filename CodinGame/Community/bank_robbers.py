#!/usr/bin/env python3

from heapq import *

def duration(C,N):
    return 10**N * 5**(C-N)

def schedule(R,V,CN):
    Current = [0]*R
    v = 0
    while Current:
        t = heappop(Current)
        if v<V:
            heappush(Current, t+duration(*CN[v]))
            v += 1
    return t

def main():
    R = int(input())
    V = int(input())
    CN = [tuple(map(int,input().split())) for _ in range(V)]
    print(schedule(R,V,CN))

main()
