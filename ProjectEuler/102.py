#!/usr/bin/env python

import sys

def left_turn(a, b, c):
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]) > 0

def inside(p,a,b,c):
    return left_turn(p,a,b)==left_turn(p,b,c)==left_turn(p,c,a)

def main():
    cpt = 0
    for _ in xrange(1000):
        x0,y0,x1,y1,x2,y2 = map(int,sys.stdin.readline().split(','))
        if inside((0,0),(x0,y0),(x1,y1),(x2,y2)):
            cpt += 1
    print cpt

main()
