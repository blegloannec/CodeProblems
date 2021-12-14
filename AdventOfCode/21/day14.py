#!/usr/bin/env python3

import sys
from collections import Counter


# Parse input
start = sys.stdin.readline().strip()
assert sys.stdin.readline().strip()==''
Rules = dict(L.strip().split(' -> ') for L in sys.stdin.readlines())


# Compute result from counters of pairs
def result(Pairs):
    # pairs counters -> element counters
    Cnt = Counter()
    for p,cnt in Pairs.items():
        Cnt[p[0]] += cnt
        Cnt[p[1]] += cnt
    # every element belongs to 2 pairs, hence is counted twice,
    # except for both ends, so we add one occurrence of each
    Cnt[start[0]]  += 1
    Cnt[start[-1]] += 1
    return max(Cnt.values())//2 - min(Cnt.values())//2


# Iterate keeping count of pairs
Pairs = Counter(start[i:i+2] for i in range(len(start)-1))
for t in range(1, 41):
    Pnew = Counter()
    for p,cnt in Pairs.items():
        r = Rules.get(p, None)
        if r is not None:
            Pnew[p[0]+r] += cnt
            Pnew[r+p[1]] += cnt
        else:
            Pnew[p] += cnt
    Pairs = Pnew
    if t==10:
        print(result(Pairs))  # Part 1
print(result(Pairs))          # Part 2
