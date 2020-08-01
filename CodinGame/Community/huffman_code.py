#!/usr/bin/env python3

# NB: actually the same as CG/add_em_up

from heapq import *

N = int(input())
F = list(map(int, input().split()))
if N==1:
    res = F[0]
else:
    res = 0
    heapify(F)
    while len(F)>1:
        f = heappop(F) + heappop(F)
        res += f
        heappush(F, f)
print(res)
