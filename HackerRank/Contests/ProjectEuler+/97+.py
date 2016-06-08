#!/usr/bin/env python

import sys

# NB: Actually, python pow(B,C,M) works well!
# no need for your own fast exp in python

def expo(a, b, q):
    result = 1
    while b:
        if b & 1:
            result = (result * a) % q
        a = (a * a) % q
        b >>= 1
    return result

M = 10**12

def main():
    T = int(sys.stdin.readline())
    S = 0
    for _ in xrange(T):
        A,B,C,D = map(int,sys.stdin.readline().split())
        S = (S + A*expo(B,C,M)+D) % M
    print '%012d' % S

main()
