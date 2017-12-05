#!/usr/bin/env python3

import sys

I = list(map(int,sys.stdin.readlines()))  # Input

# Part 1
P = I[:]
i = s = 0
while 0<=i<len(P):
    P[i] += 1
    i += P[i]-1
    s += 1
print(s)


# Part 2
P = I[:]
i = s = 0
while 0<=i<len(P):
    i0 = i
    i += P[i]
    P[i0] += -1 if P[i0]>=3 else 1
    s += 1
print(s)
