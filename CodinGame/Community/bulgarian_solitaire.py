#!/usr/bin/env python3

# interesting game from Martin Gardner
# https://en.wikipedia.org/wiki/Bulgarian_solitaire

N = int(input())
C = tuple(int(x) for x in input().split() if x!='0')
t = 0
Time = {}
while C not in Time:
    Time[C] = t
    C = tuple(sorted([c-1 for c in C if c>1]+[len(C)]))
    t += 1
print(t-Time[C])
