#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from itertools import groupby

S = input()
T = input()
res = set()
for (a,s),(b,t) in zip(groupby(S),groupby(T)):
    assert a==b
    s = list(s)
    t = list(t)
    if len(s)!=len(t):
        assert len(t)==2*len(s)
        res.add(a)
print(''.join(res))
