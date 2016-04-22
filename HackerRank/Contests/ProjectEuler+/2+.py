#!/usr/bin/env python

import sys

# naive approach (recompute everything for each input) works here
# better solution (not implemented): precompute the list of
# (u_n, sum of even terms <=u_n) then dichotomic search

def problem2():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        x0 = 1
        x1 = 2
        s = 0
        while x1<=N:
            if x1%2==0:
                s += x1
            x1,x0 = x1+x0,x1
        print s

problem2()
