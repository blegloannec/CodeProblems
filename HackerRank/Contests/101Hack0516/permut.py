#!/usr/bin/env python

import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    P = map((lambda x: int(x)-1),sys.stdin.readline().split())
    # P is given in such a way that it already is the "inverse"
    # of the permutation in the problem statement
    m -= 1
    m0 = m
    while m0>=0 and m-m0<n:
        m = m0 + P[m-m0]
        m0 -= 1
    print m+1

main()
