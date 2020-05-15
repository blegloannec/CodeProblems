#!/usr/bin/env python3

import sys

In = list(map(int, sys.stdin.read().split()))

T = In[0]
i = 1
for _ in range(T):
    L = In[i]
    i += 1
    N = In[i]
    i += 1
    A = In[i:i+N]
    i += N
    tmin = max(min(a, L-a) for a in A)
    tmax = max(max(a, L-a) for a in A)
    sys.stdout.write(f'{tmin} {tmax}\n')
