#!/usr/bin/env python3

# NB: Given input numbers happen to be actually so small that this can
#     reasonably be interpreted as a binary addition. E.g. in Ruby:
# n = gets.to_i
# puts gets.split.map{|x| 1<<x.to_i}.sum.to_s(2).count('1')

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
