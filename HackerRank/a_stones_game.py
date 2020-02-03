#!/usr/bin/env python3

import sys

# DP to guess the Grundy function
from functools import lru_cache
@lru_cache(maxsize=None)
def grundy(n):
    if n==0:
        return 0
    S = [grundy(m) for m in range(n//2+1)]
    g = 0
    while g in S:
        g += 1
    return g

# we discover that grundy(n) == n.bit_length()

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        L = N.bit_length()
        G = 1  # for the single 1
        # all values from 2 to L-1 appear an even number of times
        if N&1==0:  # value L if appears an odd nb of times (i.e. N even)
            G ^= L
        # we want G = 0, so A -> B with grundy(A)^grundy(B) = G and 2B <= A
        D = 1
        if G!=1:
            GA = 1<<(G.bit_length()-1)
            A = 1<<(GA-1)
            GB = G^GA
            B = min((1<<GB)-1, A>>1) if GB else 0
            D = A-B
        sys.stdout.write('%d\n' % D)

main()
