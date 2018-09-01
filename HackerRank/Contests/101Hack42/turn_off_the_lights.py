#!/usr/bin/env python

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    C = map(int,sys.stdin.readline().split())
    cmin = float('inf')
    for i0 in xrange(k+1):
        # on demarre par 0<=i0<=k, qui couvre les lampes 0 a i0+k
        # puis on choisit les lampes i0+l*(2*k+1)
        r = (n-(i0+k+1))%(2*k+1) # nb de lampes du dernier segment
        if r==0 or r>k:
            cmin = min(cmin,sum(C[i] for i in xrange(i0,n,2*k+1)))
    print cmin

main()
