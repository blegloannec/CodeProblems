#!/usr/bin/env python

import sys

def main():
    global N,H,memo
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        H = sorted(map(int,sys.stdin.readline().split()))
        for i in xrange(N-2,-1,-1):
            H[i] += H[i+1]
        m = 0
        for i in xrange(N):
            m = max(m,(1+i)*H[i])
        print m
        
main()
