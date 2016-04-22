#!/usr/bin/env python

import sys

def sum_digits(n):
    s = 0
    while n>0:
        s += n%10
        n /= 10
    return s

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def problem20():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N = int(sys.stdin.readline())
        print sum_digits(fact(N))

problem20()
