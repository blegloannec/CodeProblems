#!/usr/bin/env python3

from collections import deque

Cnt = deque([0]*9)
for a in map(int, input().split(',')):
    Cnt[a] += 1

for d in range(1, 257):
    Cnt[7] += Cnt[0]
    Cnt.rotate(-1)
    if d==80:
        print(sum(Cnt))  # Part 1
print(sum(Cnt))          # Part 2
