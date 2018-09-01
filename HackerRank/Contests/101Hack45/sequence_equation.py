#!/usr/bin/env python

import sys

def inv(P):
    I = [0]*len(P)
    for i in xrange(len(P)):
        I[P[i]] = i
    return I

def main():
    n = int(sys.stdin.readline())
    P = map(lambda x: int(x)-1, sys.stdin.readline().split())
    I = inv(P)
    for i in xrange(n):
        print I[I[i]]+1

main()
