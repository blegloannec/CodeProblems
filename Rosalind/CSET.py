#!/usr/bin/env python3

import sys

Chars = [L.strip() for L in sys.stdin.readlines()]
n = len(Chars[0])
Sall = frozenset(range(n))
C = []
Cc = []
for i in range(len(Chars)):
    s = frozenset(x for x in range(n) if Chars[i][x]=='1')
    C.append(s)
    Cc.append(Sall-s)

Conflicts = set(range(n))
for i in range(len(Chars)):
    for j in range(i+1,len(Chars)):
        if C[i]&C[j] and C[i]&Cc[j] and Cc[i]&C[j] and Cc[i]&Cc[j]:
            Conflicts &= {i,j}
assert(Conflicts)
k = Conflicts.pop()
for i in range(len(Chars)):
    if i!=k:
        print(Chars[i])
