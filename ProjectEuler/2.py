#!/usr/bin/env python

def problem2():
    x0 = 1
    x1 = 2
    s = 0
    while x1<=4000000:
        if x1%2==0:
            s += x1
        svg = x1
        x1 += x0
        x0 = svg
    print s

problem2()
