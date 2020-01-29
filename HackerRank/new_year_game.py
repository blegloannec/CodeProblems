#!/usr/bin/env python3

# DP to guess the pattern
from functools import lru_cache
@lru_cache(maxsize=None)
def win(n0, n1, n2, s=0, first=True):
    if n1==n2==0:
        return not first if s==0 else first
    if n0>0 and not win(n0-1, n1, n2, s, not first):
        return True
    if n1>0 and not win(n0, n1-1, n2, (s+1 if first else s-1)%3, not first):
        return True
    if n2>0 and not win(n0, n1, n2-1, (s+2 if first else s-2)%3, not first):
        return True
    return False

# we discover that the result is determined by the parity of n1 and n2
# (btw, it's not very hard to prove once you figured it out, the winning
#  strategies are mostly about canceling the other player move)
def pattern(n0,n1,n2):
    return not n2%2==n1%2==0

import random
random.seed()
def experiment():
    for n in range(100):
        N = [random.randint(1,60) for _ in range(3)]
        assert win(*N)==pattern(*N)

#experiment()


import sys
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int,sys.stdin.readline().split()))
        R = [0]*3
        for a in A:
            R[a%3] += 1
        sys.stdout.write('Balsa\n' if not R[1]&1==R[2]&1==0 else 'Koca\n')

main()
