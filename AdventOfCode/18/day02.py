#!/usr/bin/env python3

import sys
from collections import Counter

I = [L.strip() for L in sys.stdin.readlines()]

# Part 1
CL = [Counter(y for _,y in Counter(L).items()) for L in I]  # counters^2
c2 = sum(int(2 in C) for C in CL)
c3 = sum(int(3 in C) for C in CL)
print(c2*c3)

# Part 2
for i in range(len(I)):
    for j in range(i+1,len(I)):
        X = ''.join(a for a,b in zip(I[i],I[j]) if a==b)
        if len(X)==len(I[i])-1:
            print(X)
