#!/usr/bin/env python

def problem15():
    n = 20+1
    M = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        for j in range(1,n):
            M[i][j] = M[i-1][j]+M[i][j-1]
    print M[n-1][n-1]

problem15()
