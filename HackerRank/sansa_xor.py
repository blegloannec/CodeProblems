#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        res = 0
        for i in xrange(N):
            # nb of sub-arrays A[i] appears in
            nb_sub = (i+1)*(N-i)
            if nb_sub%2==1:
                res ^= A[i]
        print res

main()
