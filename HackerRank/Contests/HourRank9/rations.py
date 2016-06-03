#!/usr/bin/env python

import sys

def main():
    N = int(sys.stdin.readline())
    B = map(int,sys.stdin.readline().split())
    cpt = 0
    for i in xrange(N-1):
        if B[i]%2==1:
            B[i] += 1
            B[i+1] += 1
            cpt += 2
    if B[-1]%2==1:
        print 'NO'
    else:
        print cpt
        
main()
