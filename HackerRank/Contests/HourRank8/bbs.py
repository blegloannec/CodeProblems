#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline().strip())
    res = 0
    for i in xrange(n-2):
        if s[i:i+3]==['0','1','0']:
            s[i+2] = '1'
            res += 1
    print res

main()
