#!/usr/bin/env python3

from collections import Counter

_,d = map(int,input().split())
A = list(map(int,input().split()))
C = Counter(a//d for a in A)
print(sum(c*(c-1)//2 for c in C.values()))
