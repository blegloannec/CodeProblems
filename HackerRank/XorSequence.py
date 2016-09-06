#!/usr/bin/env python

import sys

def A(n):
    if n%2==0:
        return n+(n/2)%2
    return 1-(n/2)%2

def SA(n):
    return int(n%4==1) + 2*A(n/2)

def main():
    Q = int(sys.stdin.readline())
    for _ in xrange(Q):
        L,R = map(int,sys.stdin.readline().split())
        print SA(L-1)^SA(R)

main()
