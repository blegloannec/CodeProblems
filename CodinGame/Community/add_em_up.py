#!/usr/bin/env python3

from heapq import *

N = int(input())
H = list(map(int,input().split()))
heapify(H)
C = 0
while len(H)>1:
    x = heappop(H)+heappop(H)
    C += x
    heappush(H,x)
print(C)
