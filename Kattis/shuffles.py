#!/usr/bin/env python3

# the given sequence can be decomposed into (non-consecutive)
# increasing sub-sequences of consecutive values
# initially you only have one such sub-sequence
# in 1 step, you can create 2
# in 2 steps                4
# in 3 steps                8
# ...
# Example: 21436587
# 5 sub-seq. 23, 1, 45, 67, 8  ~>  3 steps needed
# 1|23||45|67|8 -> 145|23678 -> 2143657|8 -> 21436587

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    L = map(int, input().split())
    P = [None]*N
    for i,x in enumerate(L):
        P[x-1] = i
    k = 1
    for i in range(N-1):
        if P[i+1]<P[i]:
            k += 1
    res = 0
    while 1<<res < k:
        res += 1
    print(res)

main()
