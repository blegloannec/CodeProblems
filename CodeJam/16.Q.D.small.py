#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        K,C,S = map(int,sys.stdin.readline().split())
        print 'Case #%d: %s' % (t,' '.join(map(str,range(1,K+1))))

main()
