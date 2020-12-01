#!/usr/bin/env python3

import sys

I = [int(L.strip()) for L in sys.stdin.readlines()]
S = set(I)

def part1():
    for x in I:
        y = 2020 - x
        if y in S:
            return x*y

print(part1())


def part2():
    for i in range(len(I)):
        for j in range(i+1, len(I)):
            z = 2020 - I[i] - I[j]
            if z in S:
                return I[i]*I[j]*z

print(part2())
