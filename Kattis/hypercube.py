#!/usr/bin/env python3

def gray_idx(g):
    n = len(g)
    idx = inv = 0
    for i,c in enumerate(g):
        c = int(c)
        if c!=inv:
            idx |= 1<<(n-1-i)
        inv ^= c
    return idx

_, a, b = input().split()
print(gray_idx(b)-gray_idx(a)-1)
