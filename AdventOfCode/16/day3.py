#!/usr/bin/env python

import sys

# Part One
def part1():
    cpt  = 0
    for L in sys.stdin.readlines():
        a,b,c = sorted(map(int,L.split()))
        if a+b>c:
            cpt += 1
    print cpt

#part1()


# Part Two
def part2():
    cpt  = 0
    I = [map(int,L.split()) for L in sys.stdin.readlines()]
    for i in xrange(0,len(I),3):
        for j in xrange(3):
            a,b,c = sorted(I[i+k][j] for k in xrange(3))
            if a+b>c:
                cpt += 1
    print cpt

part2()
