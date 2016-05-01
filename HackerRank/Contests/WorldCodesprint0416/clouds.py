#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    C = map(int,sys.stdin.readline().split())
    i = 0
    j = 0
    while i<n-1:
        if i<n-2 and C[i+2]==0:
            i += 2
        else:
            i += 1
        j += 1
    print j

main()
