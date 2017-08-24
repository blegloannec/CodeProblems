#!/usr/bin/env python3

from collections import *

S1 = Counter(map(float,input().split()))
S2 = Counter(map(float,input().split()))
D = defaultdict(int)
m = None
for x in S1:
    for y in S2:
        d = round(x-y,5)
        D[d] += S1[x]*S2[y]
        if m==None or D[d]>D[m]:
            m = d
print(D[m])
print(m)
