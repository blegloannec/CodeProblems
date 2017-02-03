#!/usr/bin/env python3

from heapq import *

N = int(input())
H = list(map(int,input().split()))
heapify(H)

res = 0
while H:
    i = heappop(H)
    if H and H[0]==i:
        heappop(H)
        heappush(H,i+1)
    else:
        res += 1
print(res)
