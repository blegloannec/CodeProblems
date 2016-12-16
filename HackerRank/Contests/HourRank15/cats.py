#!/usr/bin/env python

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        x,y,z = map(int,sys.stdin.readline().split())
        d1,d2 = abs(z-x),abs(z-y)
        if d1<d2:
            print 'Cat A'
        elif d1>d2:
            print 'Cat B'
        else:
            print 'Mouse C'

main()
