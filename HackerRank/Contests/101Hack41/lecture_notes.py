#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    S = sys.stdin.readline()
    F = map(int,sys.stdin.readline().split())
    for f in F:
        if S[f-1]=='0':
            print 'YES'
            return
    print 'NO'

main()
