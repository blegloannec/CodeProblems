#!/usr/bin/env python3

from collections import defaultdict

S = input()
D = defaultdict(float)
i = d = 0
while i<len(S):
    if S[i]=='-':
        d -= 1
        i += 2
    else:
        d += 1
        D[S[i]] += 1/d
        i += 1
print(max(D.keys(), key=(lambda a: D[a])))
