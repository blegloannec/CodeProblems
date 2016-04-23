#!/usr/bin/env python

import sys

def problem11():
    n = 20
    M = []
    for i in xrange(n):
        M.append(map(int,sys.stdin.readline().split()))
    pmax = 0
    for i in xrange(n):
        for j in xrange(n):
            if i<n-3:
                p = M[i][j]*M[i+1][j]*M[i+2][j]*M[i+3][j]
                pmax = max(p,pmax)
            if j<n-3:
                p = M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]
                pmax = max(p,pmax)
            if i<n-3 and j<n-3:
                p = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
                pmax = max(p,pmax)
                p = M[i+3][j]*M[i+2][j+1]*M[i+1][j+2]*M[i][j+3]
                pmax = max(p,pmax)
    print pmax

problem11()
