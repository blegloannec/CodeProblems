#!/usr/bin/env python3

import sys

ord0 = ord('0')

I = [L.strip() for L in sys.stdin.readlines()]
BS = len(I[0])


# Part 1
def part1():
    gamma = epsilon = 0
    for b in range(BS):
        cnt = [0,0]
        for L in I:
            cnt[ord(L[b])-ord0] += 1
        assert cnt[0]!=cnt[1]
        if cnt[0]<cnt[1]:
            gamma |= 1<<(BS-1-b)
        else:
            epsilon |= 1<<(BS-1-b)
    return gamma*epsilon

print(part1())


# Part 2
def elim(most=True):
    bmost = 0 if most else 1
    R = I.copy()
    b = 0
    while len(R)>1:
        sub = [[],[]]
        for L in R:
            sub[ord(L[b])-ord0].append(L)
        keep = bmost ^ (len(sub[0])<=len(sub[1]))
        R = sub[keep]
        b += 1
    return int(R[0],2)

def part2():
    oxygen = elim()
    co2 = elim(False)
    return oxygen*co2

print(part2())
