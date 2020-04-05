#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for t in range(1,T+1):
    N,M = map(int,sys.stdin.readline().split())
    exists = set()
    cpt = 0
    for i in xrange(N):
        exists.add(sys.stdin.readline().strip())
    for i in xrange(M):
        path = sys.stdin.readline().strip().split('/')
        p = ''
        for j in xrange(1,len(path)):
            p += '/'+path[j]
            if not (p in exists):
                exists.add(p)
                cpt += 1
    print 'Case #%d: %d' % (t,cpt)
