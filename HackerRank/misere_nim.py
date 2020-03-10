#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        S = map(int,sys.stdin.readline().split())
        if max(S)==1:
            if len(S)%2==0:
                print 'First'
            else:
                print 'Second'
        else:
            if reduce((lambda x,y: x^y), S)==0:
                print 'Second'
            else:
                print 'First'

main()
