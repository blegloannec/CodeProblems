#!/usr/bin/env python

from fractions import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

def problem5():
    l = 2
    for i in range(3,21):
        l = lcm(l,i)
    print l

problem5()
