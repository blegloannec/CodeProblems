#!/usr/bin/env python3

import sys

I = []
for L in sys.stdin.readlines():
    c,x = L.split()
    I.append((c, int(x)))

def part1(I):
    horiz = depth = 0
    for c,x in I:
        if c=='forward':
            horiz += x
        elif c=='down':
            depth += x
        else:
            assert c=='up'
            depth -= x
            assert depth>=0
    return horiz*depth

print(part1(I))

def part2(I):
    horiz = depth = aim = 0
    for c,x in I:
        if c=='down':
            aim += x
        elif c=='up':
            aim -= x
        else:
            horiz += x
            depth += aim*x
            assert depth>=0
    return horiz*depth

print(part2(I))
