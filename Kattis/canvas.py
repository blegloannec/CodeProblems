#!/usr/bin/env python3

# Seeing the process in reverse, it is optimal to merge the smallest
# 2 consecutive blocks.
# Because we can reorder everything the ways we want at step 1,
# it is exactly equivalent to Huffman coding.

from heapq import *
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        H = list(map(int, input().split()))
        heapify(H)
        res = 0
        while len(H)>1:
            s = heappop(H) + heappop(H)
            res += s
            heappush(H, s)
        print(res)

main()
