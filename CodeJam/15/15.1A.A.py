#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        M = map(int,sys.stdin.readline().split())
        rate = 0
        nb1 = 0
        for i in xrange(1,len(M)):
            if M[i]<M[i-1]:
                nb1 += M[i-1]-M[i]
                rate = max(rate,M[i-1]-M[i])
        nb2 = 0
        for i in xrange(len(M)-1):
            nb2 += min(rate,M[i])
        print 'Case #%d: %d %d' % (t,nb1,nb2)

main()
