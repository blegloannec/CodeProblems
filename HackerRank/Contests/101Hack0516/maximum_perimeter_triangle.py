#!/usr/bin/env python

import sys

def main():
    pmax = 0
    n = int(sys.stdin.readline())
    L = sorted(map(int, sys.stdin.readline().split()))
    for c in xrange(n-1,-1,-1):
        for b in xrange(c-1,-1,-1):
            for a in xrange(b-1,-1,-1):
                if L[a]+L[b]>L[c]:
                    p = L[a]+L[b]+L[c]
                    if p>pmax:
                        pmax = p
                        amax,bmax,cmax = a,b,c
    if pmax==0:
        print -1
    else:
        print L[amax],L[bmax],L[cmax]

main()
