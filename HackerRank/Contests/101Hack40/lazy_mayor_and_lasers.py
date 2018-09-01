#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    H = map(int,sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    X = map(int,sys.stdin.readline().split())
    X.sort()
    x0 = 0
    for p in X:
        x = p-1
        h = 1
        while x>x0:
            H[x-1] = min(H[x-1],h)
            x -= 1
            h += 1
        x0 = p-1
    print sum(H)

main()
