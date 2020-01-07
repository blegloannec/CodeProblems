#!/usr/bin/env python3

# for n>0, 2^n mod 17 = 2, 4, 8, 16 ~ -1, -2, -4, -8, -16 ~ 1, 2, ...
# as we can play +/- arbitrarily, i and -i mod 17 are equivalent
# (+ on 2^1 is equivalent to - on 2^5) then exponents fall into
# only 4 categories: 1, 2, 4 & 8 mod 17.

# DP to guess the pattern
from functools import lru_cache
@lru_cache(maxsize=None)
def win(n1, n2, n4, n8, s=0, first=True):
    if n1==n2==n4==n8==0:
        return s!=0 if first else s==0
    if n1>0:
        if not win(n1-1, n2, n4, n8, (s+1)%17, not first) or \
           not win(n1-1, n2, n4, n8, (s-1)%17, not first):
            return True
    if n2>0:
        if not win(n1, n2-1, n4, n8, (s+2)%17, not first) or \
           not win(n1, n2-1, n4, n8, (s-2)%17, not first):
            return True
    if n4>0:
        if not win(n1, n2, n4-1, n8, (s+4)%17, not first) or \
           not win(n1, n2, n4-1, n8, (s-4)%17, not first):
            return True
    if n8>0:
        if not win(n1, n2, n4, n8-1, (s+8)%17, not first) or \
           not win(n1, n2, n4, n8-1, (s-8)%17, not first):
            return True
    return False

def experiment():
    N = [0]*4
    for n in range(1,50):
        N[n%4] += 1
        print(n, win(*N))

#experiment()

# We discover second wins iff n = 0 mod 8
# (btw it's not hard to prove, see editorial for instance)

import sys
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        sys.stdout.write('Second\n' if N&0b111==0 else 'First\n')

main()
