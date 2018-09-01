#!/usr/bin/env python

import sys

def main():
    N = int(sys.stdin.readline())
    M = []
    G = []
    for i in xrange(3):
        M.append(int(sys.stdin.readline()))
        G.append([set() for _ in xrange(N)])
        for _ in xrange(M[i]):
            u,v = map(int, sys.stdin.readline().split())
            u,v = u-1,v-1
            G[i][u].add(v)
            G[i][v].add(u)
    cpt = 0
    for a in xrange(N):
        for b in G[0][a]:
            for c in G[1][b]:
                if a in G[2][c]:
                    #print a,b,c
                    cpt += 1
    print cpt

main()
