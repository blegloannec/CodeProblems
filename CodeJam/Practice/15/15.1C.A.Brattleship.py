#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        R,C,W = map(int,sys.stdin.readline().split())
        print 'Case #%d: %d' % (t,R*(C/W)+W-int(C%W==0))

main()
