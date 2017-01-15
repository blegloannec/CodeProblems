#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
C = map(int,sys.stdin.readline().split())
if n==1:
    print 2*C[0],1
else:
    m = min(C)
    if C.count(m)>1:
        print m,n
    else:
        print min(2*m,min(c for c in C if c>m)),1
