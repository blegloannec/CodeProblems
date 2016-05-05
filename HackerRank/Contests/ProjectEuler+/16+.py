#!/usr/bin/env python

import sys

def sum10(n):
    s = 0
    while n>0:
        s += n%10
        n /= 10
    return s

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print sum10(2**N)

main()
