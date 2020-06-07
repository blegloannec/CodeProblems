#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Consider two distinct (not disjoint) groups A & B of size m-1.
# If both A & B cannot open a same lock l, then for any C ⊆ A ∪ B
# with |C| = m, C cannot open l. Absurd (|A ∪ B| ≥ m, such C exists)!
# Each of the binom(n, m-1) groups of size m-1 has at least one lock
# it cannot open, hence there has to be at least binom(n, m-1) locks
# for the previous situation not to occur.
# It obviously is enough as one can associate a unique excluded key to
# each group of m-1, and give this key to everyone not in the group.

from functools import lru_cache

@lru_cache(maxsize=None)
def binom(n, p):
    assert 0<=p<=n
    return 1 if p==0 else n*binom(n-1, p-1)//p

def main():
    T = int(input())
    for _ in range(T):
        n,m = map(int, input().split())
        print(binom(n, m-1))

main()
