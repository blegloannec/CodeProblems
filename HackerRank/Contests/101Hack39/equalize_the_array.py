#!/usr/bin/env python

import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    D = defaultdict(int)
    m = 0
    for a in A:
        D[a] += 1
        if D[a]>m:
            m = D[a]
    print n-m

main()
