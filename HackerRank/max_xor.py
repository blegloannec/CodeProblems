#!/usr/bin/env python

import sys

def main():
    L = int(sys.stdin.readline())
    R = int(sys.stdin.readline())
    res = 0
    for A in xrange(L,R+1):
        for B in xrange(A,R+1):
            res = max(res,A^B)
    print res

main()
