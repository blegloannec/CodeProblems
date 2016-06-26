#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    d = float('inf')
    for i in xrange(n):
        for j in xrange(i+1,n):
            if A[i]==A[j]:
                d = min(d,j-i)
    print (-1 if d==float('inf') else d)

main()
