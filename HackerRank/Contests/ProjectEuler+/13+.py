#!/usr/bin/env python

import sys

def main():
    N = int(sys.stdin.readline())
    S = 0
    for _ in xrange(N):
        X = int(sys.stdin.readline())
        S += X
    print str(S)[:10]

main()
