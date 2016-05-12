#!/usr/bin/python

import sys
from math import log

def main():
    N = int(sys.stdin.readline())
    v = []
    for _ in xrange(N):
        B,E = map(int,sys.stdin.readline().split())
        V.append((E*log(B),B,E))
    K = int(sys.stdin.readline())
    V.sort()
    print V[K-1][1],V[K-1][2]

main()
