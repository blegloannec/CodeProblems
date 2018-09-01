#!/usr/bin/env python

import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    posA = 0
    inv = False
    for _ in xrange(m):
        t,k = map(int,sys.stdin.readline().split())
        if t==1:
            posA = (posA+k)%n
        else:
            posA = (k-posA)%n
            inv = not inv
    if not inv:
        print 1,(n-posA)%n
    else:
        print 2,posA

main()
