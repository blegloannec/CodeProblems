#!/usr/bin/env python

import sys

def expmod(x,n,p):
    y = 1
    while n>0:
        if n&1==1:
            y = (x*y)%p
        x = (x*x)%p
        n >>= 1
    return y

def main():
    M = 10000000000
    N = int(sys.stdin.readline())
    s = 0
    for i in xrange(1,N+1):
        s = (s+expmod(i,i,M))%M
    print s

main()
