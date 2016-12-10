#!/usr/bin/env python

import sys
from math import sqrt

# algo en O(n*m*r) ~ 10^8
# surprisingly too slow for python 2 (and not due to sqrt)
# but way under limit (<1s on every testcase) with pypy

def main():
    n,m,r = map(int,sys.stdin.readline().split())
    W = []
    for _ in xrange(n):
        W.append(map(int,sys.stdin.readline().split()))
    # propagation des sommes
    for i in xrange(n):
        for j in xrange(1,m):
            W[i][j] += W[i][j-1]
    X = 0
    for i in xrange(n):
        for j in xrange(m):
            S = 0
            # on somme les lignes du cercle de centre (i,j)
            # grace au precalcul, on a la somme sur chaque ligne en O(1)
            for x in xrange(r+1):
                y = int(sqrt(r*r-x*x))
                if i+x<n:
                    S += W[i+x][min(j+y,m-1)] - (0 if j-y-1<0 else W[i+x][j-y-1])
                if x>0 and i-x>=0:
                    S += W[i-x][min(j+y,m-1)] - (0 if j-y-1<0 else W[i-x][j-y-1])
            X ^= S
    print X

main()
