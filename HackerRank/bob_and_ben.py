#!/usr/bin/env python3

# Typically a tree of size n>0 can either be transformed into:
#  - a tree of size n-1 by removing a leaf;
#  - a tree of size 0 (i.e. deleted) if there is an internal node (i.e. n>2).
# Hence, the Grundy function of a tree of size n is:
#  n = 0 -> 0
#      1 -> 1
#      2 -> 0 (as both vertices are leaves, no internal node)
#      3 -> 1 = mex(G(0),G(2))
#      4 -> 2 = mex(G(0),G(3))
#      5 -> 1 = mex(G(0),G(4))
# even n -> 2
#  odd n -> 1

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        G = 0
        for _ in range(N):
            M,_ = map(int,sys.stdin.readline().split())
            if M!=2:
                G ^= 2 - (M&1)
        sys.stdout.write('BEN\n' if G==0 else 'BOB\n')

main()
