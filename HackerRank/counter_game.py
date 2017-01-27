#!/usr/bin/env python

import sys

# the solution is directly given by the number of 1s +
# the number of trailing 0s in the binary writing of N

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        trail0,nb1 = 0,0
        while N:
            if N&1:
                nb1 += 1
            elif nb1==0:
                trail0 += 1
            N >>= 1
        print 'Richard' if (nb1+trail0)%2 else 'Louise'

main()
