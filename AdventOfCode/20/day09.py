#!/usr/bin/env python3

import sys

I = [int(L.strip()) for L in sys.stdin.readlines()]
N = len(I)


# Part 1
for i in range(25, N):
    valid = False
    for j in range(i-25, i):
        for k in range(j+1, i):
            if I[i] == I[j]+I[k]:
                valid = True
    if not valid:
        part1 = I[i]
        break
print(part1)


# Part 2
for i in range(N):
    s = I[i]
    for j in range(i+1, N):
        s += I[j]
        if s == part1:
            print(min(I[i:j+1]) + max(I[i:j+1]))
