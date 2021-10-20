#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def min_swaps(P):
    res = 0
    Seen = [False]*len(P)
    for i in range(len(P)):
        if not Seen[i]:
            # straightening up a cycle of the permutation
            # costs its size - 1
            Seen[i] = True
            j = P[i]
            while j!=i:
                Seen[j] = True
                j = P[j]
                res += 1
    return res

def main():
    N = int(input())
    P = [int(i)-1 for i in input().split()]
    print(min_swaps(P))

main()
