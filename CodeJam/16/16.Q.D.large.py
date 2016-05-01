#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for t in range(1,T+1):
    K,C,S = map(int,sys.stdin.readline().split())
    if C*S<K:
        print 'Case #%d: IMPOSSIBLE' % t
    else:
        P = [sum([min(i+j,K-1)*(K**j) for j in range(C)])+1 for i in range(0,K,C)]
        print 'Case #%d: %s' % (t,' '.join(map(str,P)))
