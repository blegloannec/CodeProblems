#!/usr/bin/env python

import sys
from math import *

def S(n):
    s = 0
    while n>0:
        s += F[n%10]
        n /= 10
    return s

def fact(n):
    return 1 if n<2 else n*fact(n-1)

F = [fact(i) for i in xrange(10)]

def main():
    N = int(sys.stdin.readline())
    s = 0
    for i in xrange(10,N):
        if S(i)%i==0:
            s += i
    print s

main()
