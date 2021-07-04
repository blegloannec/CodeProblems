#!/usr/bin/env python3

import sys
input = sys.stdin.readline

N,P = map(int, input().split())
C = [int(x)-P for x in input().split()]

# max contiguous subseq
res = s = 0
for c in C:
    s = max(c, s+c)
    if s>res: res = s
print(res)
