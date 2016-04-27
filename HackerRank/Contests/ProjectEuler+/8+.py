#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N,K = map(int,sys.stdin.readline().split())
        L = map(int,list(sys.stdin.readline().strip()))
        m = 0
        for i in range(N-K+1)
            p = reduce((lambda x,y: x*y), L[i:i+K])
            m = max(m,p)
        print m

main()
