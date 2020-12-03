#!/usr/bin/env python3

import sys

I = [L.strip() for L in sys.stdin.readlines()]
H = len(I)
W = len(I[0])

def slope_cnt(r,d):
    cnt = i = j = 0
    while i<H:
        if I[i][j]=='#':
            cnt += 1
        i += d
        j = (j+r) % W
    return cnt

res = slope_cnt(3,1)
print(res)  # Part 1
for r,d in ((1,1),(5,1),(7,1),(1,2)):
    res *= slope_cnt(r,d)
print(res)  # Part 2
