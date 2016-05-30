#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    c = 0
    for i in xrange(n):
        for j in xrange(i+1,n):
            if (A[i]+A[j])%k==0:
                c += 1
    print c

main()
