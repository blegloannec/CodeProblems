#!/usr/bin/env python

def problem28():
    n = 1001
    s = 1
    for n in range(3,n+1,2):
        s += n*n + n*n-(n-1) + n*n-2*(n-1) + n*n-3*(n-1)
    print s

problem28()
