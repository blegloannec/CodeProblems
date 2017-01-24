#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    for _ in xrange(n):
        a,b = map(int,sys.stdin.readline().split())
        A,p2,i = a,1,0
        while p2<=a:
            if b/p2>a/p2:
                A &= ~(1<<i)
            p2 <<= 1
            i += 1
        print A

main()
