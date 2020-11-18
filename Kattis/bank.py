#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from heapq import *

def main():
    N,T = map(int, input().split())
    Client = [[] for _ in range(T)]
    for _ in range(N):
        c,t = map(int, input().split())
        Client[t].append(c)
    Avail = []
    res = 0
    for t in range(T-1, -1, -1):
        for c in Client[t]:
            heappush(Avail, -c)
        if Avail:
            res += -heappop(Avail)
    print(res)

main()
