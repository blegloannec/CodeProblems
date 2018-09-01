#!/usr/bin/env python

import sys

def main():
    A = map(int,sys.stdin.readline().split())
    B = map(int,sys.stdin.readline().split())
    sa,sb = 0,0
    for i in xrange(3):
        if A[i]>B[i]:
            sa += 1
        elif B[i]>A[i]:
            sb += 1
    print sa,sb
            
main()
