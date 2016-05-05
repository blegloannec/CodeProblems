#!/usr/bin/env python

import sys
from bisect import *

def score(name):
    s = 0
    for c in name:
        s += ord(c)-ord('A')+1
    return s

def main():
    Names = []
    N = int(sys.stdin.readline())
    for _ in xrange(N):
        Names.append(sys.stdin.readline().strip())
    Names.sort()
    Q = int(sys.stdin.readline())
    for _ in xrange(Q):
        name = sys.stdin.readline().strip()
        print (bisect_left(Names,name)+1)*score(name)

main()
