#!/usr/bin/env python3

import sys
from collections import Counter

I = [0] + sorted(int(L.strip()) for L in sys.stdin.readlines())
I.append(I[-1]+3)
N = len(I)


# Part 1
Cnt = Counter(I[i]-I[i-1] for i in range(1, N))
print(Cnt[1]*Cnt[3])


# Part 2
DP = [0]*N
DP[-1] = 1
for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if I[j]-I[i] <= 3:
            DP[i] += DP[j]
        else:
            break
print(DP[0])
