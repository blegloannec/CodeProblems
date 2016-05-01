#!/usr/bin/env python

import sys
sys.setrecursionlimit(1010)

G = []

def FBT(u,p):
    n = 1
    m1,m2 = None,None
    for v in G[u]:
        if v==p:
            continue
        n0,s0 = FBT(v,u)
        n += n0
        g0 = n0-s0
        if m1==None or g0>=m1:
            m1,m2 = g0,m1
        elif m2==None or g0>=m2:
            m2 = g0
    if m2!=None:
        return (n,n-1-m1-m2)
    else:
        return (n,n-1)

def main():
    global G
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        G = [[] for _ in xrange(N)]
        for i in xrange(N-1):
            u,v = map(int,sys.stdin.readline().split())
            G[u-1].append(v-1)
            G[v-1].append(u-1)
        res = 1001
        for u in xrange(N):
            res = min(res,FBT(u,None)[1])
        print 'Case #%d: %d' % (t,res)

main()
