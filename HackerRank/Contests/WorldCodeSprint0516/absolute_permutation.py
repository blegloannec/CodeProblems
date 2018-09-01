#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N,K = map(int,sys.stdin.readline().split())
        P = range(N)
        if K==0:
            print ' '.join(map((lambda x: str(x+1)), P))
            continue
        if N%(2*K)!=0:
            print -1
            continue
        for j in xrange(N/(2*K)):
            for i in xrange(2*K*j,2*K*j+K):
                P[i],P[i+K] = P[i+K],P[i]
        print ' '.join(map((lambda x: str(x+1)), P))

main()
