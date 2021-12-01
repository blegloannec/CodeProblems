#!/usr/bin/env python3

import sys

# Part 1
def cnt_incr(A):
    return sum(1 for i in range(1, len(A)) if A[i]>A[i-1])

I = list(map(int, sys.stdin.readlines()))
print(cnt_incr(I))

# Part 2
I3 = [sum(I[i:i+3]) for i in range(len(I)-2)]
print(cnt_incr(I3))
