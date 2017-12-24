#!/usr/bin/env python3

import sys
from collections import defaultdict

# Input
P = [tuple(map(int,L.split('/'))) for L in sys.stdin.readlines()]
S = [sum(p) for p in P]
D = defaultdict(list)
for i in range(len(P)):
    D[P[i][0]].append(i)
    D[P[i][1]].append(i)


# Part 1
memo = {}
def dp(p=0,used=0):
    if (p,used) in memo:
        return memo[p,used]
    res = 0
    for u in D[p]:
        if not used&(1<<u):
            res = max(res,S[u]+dp(S[u]-p,used|(1<<u)))
    memo[p,used] = res
    return res

print(dp())


# Part 2
memo2 = {}
def dp2(p=0,used=0):
    if (p,used) in memo2:
        return memo2[p,used]
    res = (0,0)
    for u in D[p]:
        if not used&(1<<u):
            l,s = dp2(S[u]-p,used|(1<<u))
            res = max(res,(l+1,S[u]+s))
    memo2[p,used] = res
    return res

print(dp2()[1])
