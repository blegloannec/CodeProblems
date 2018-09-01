#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    M,M2,m,m2 = -1,-1,float('inf'),float('inf')
    for a in A:
        if a>M:
            M,M2 = a,M
        elif a>M2:
            M2 = a
        if a<m:
            m,m2 = a,m
        elif a<m2:
            m2 = a
    print min(M2-m,M-m2)

main()
