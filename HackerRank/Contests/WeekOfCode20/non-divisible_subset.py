#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    R = [0 for _ in xrange(k)]
    for a in A:
        R[a%k] += 1
    s = 0
    m = k/2+1 if k%2==1 else k/2
    for i in xrange(1,m):
        s += max(R[i],R[k-i])
    if R[0]>=1:
        s += 1
    if k%2==0 and R[k/2]>=1:
        s += 1
    print s

main()
