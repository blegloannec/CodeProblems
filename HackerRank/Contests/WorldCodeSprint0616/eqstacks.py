#!/usr/bin/env python

import sys

def main():
    n1,n2,n3 = int(sys.stdin.readline())
    H1 = [0]+map(int,sys.stdin.readline().split())[::-1]
    H2 = [0]+map(int,sys.stdin.readline().split())[::-1]
    H3 = [0]+map(int,sys.stdin.readline().split())[::-1]
    for i in xrange(1,n1+1):
        H1[i] += H1[i-1]
    for i in xrange(1,n2+1):
        H2[i] += H2[i-1]
    for i in xrange(1,n3+1):
        H3[i] += H3[i-1]
    while not (H1[-1]==H2[-1]==H3[-1]):
        m = max(H1[-1],H2[-1],H3[-1])
        if H1[-1]==m:
            H1.pop()
        if H2[-1]==m:
            H2.pop()
        if H3[-1]==m:
            H3.pop()
    print H1[-1]

main()
