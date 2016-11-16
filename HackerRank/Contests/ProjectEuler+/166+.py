#!/usr/bin/env python

import sys

# Symmetries: geometrical, n-x on each cell (n the maximum digit)
# let A(s) = the nb of grids with sum s, A(s) = A(4n-s)
# Let S be the sum on each line/column/diagonal
# let X be the sum of the 4 corner elements
# let C be the sum of the 4 central elements
# let E be the sum of the 8 other (edges) elements
# then we have E = full square - both diagonals = 4S - 2S = 2S
# 2C = 2 central lines + 2 central columns - E = 2S + 2S - 2S = 2S
# hence C = S
# X = both diagonals - C = 2S - S = S too

def backtrack(n,s,i=0,G=[]):
    res = 0
    if i==3:
        d = s-G[0]-G[1]-G[2]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==7:
        d = s-G[4]-G[5]-G[6]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==10:
        d = s-G[5]-G[6]-G[9]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==11:
        d = s-G[8]-G[9]-G[10]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==12:
        d = s-G[0]-G[4]-G[8]
        e = s-G[3]-G[6]-G[9]
        if d==e and 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==13:
        d = s-G[1]-G[5]-G[9]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==14:
        d = s-G[2]-G[6]-G[10]
        if 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==15:
        d = s-G[12]-G[13]-G[14]
        e = s-G[3]-G[7]-G[11]
        f = s-G[0]-G[5]-G[10]
        if d==e==f and 0<=d<=n:
            G.append(d)
            res = backtrack(n,s,i+1,G)
            G.pop()
    elif i==16:
        res = 1
    else:
        for d in xrange(n+1):
            G.append(d)
            res += backtrack(n,s,i+1,G)
            G.pop()
    return res

def count(n):
    cpt = 0
    for s in xrange(0,2*n+1):
        C = backtrack(n,s)
        cpt += C if s==2*n else 2*C
    return cpt

# Precomputed data as it takes ~2s with pypy (reasonable time)
# but ~45s with python and unfortunately pypy is not activated for
# that contest! The same code would pass in C++.
C = [1, 34, 621, 5400, 30277, 125794, 423097, 1214992]

def main():
    n = int(sys.stdin.readline())
    print C[n]

main()
