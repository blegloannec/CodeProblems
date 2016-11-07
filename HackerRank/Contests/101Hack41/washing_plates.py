#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    V = []
    res = 0
    for _ in xrange(n):
        p,d = map(int,sys.stdin.readline().split())
        res -= d
        V.append(p+d)
    V.sort(reverse=True)
    print max(0,res+sum(V[:min(k,n)]))

main()
