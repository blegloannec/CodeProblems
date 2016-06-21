#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    a0,b0 = map(int,sys.stdin.readline().split())
    h,v = True,True
    for _ in xrange(T-1):
        a,b = map(int,sys.stdin.readline().split())
        h = h and a==a0
        v = v and b==b0
    if h or v:
        print 'YES'
    else:
        print 'NO'

main()
