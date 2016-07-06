#!/usr/bin/env python

import sys

def main():
    x1,v1,x2,v2 = map(int,sys.stdin.readline().split())
    if x1==x2:
        print 'YES'
    elif v1==v2:
        print 'NO'
    elif (x1-x2)*(v2-v1)>=0 and (x1-x2)%(v2-v1)==0:
        print 'YES'
    else:
        print 'NO'

main()
