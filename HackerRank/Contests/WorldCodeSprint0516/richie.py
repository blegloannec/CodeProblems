#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    change = [False for _ in xrange(n)]
    op = 0
    for i in xrange(n/2):
        if s[i]!=s[n-1-i]:
            c = max(s[i],s[n-1-i])
            change[i] = True
            s[i] = c
            s[n-1-i] = c
            op += 1
    if op>k:
        print -1
    else:
        i = 0
        while op<k and i<n/2:
            if change[i] and s[i]<'9':
                op += 1
                s[i] = '9'
                s[n-1-i] = '9'
            elif k-op>=2 and s[i]<'9':
                op += 2
                s[i] = '9'
                s[n-1-i] = '9'
            i += 1
        if op<k and n%2==1:
            s[n/2] = '9'
        print ''.join(s)
main()
