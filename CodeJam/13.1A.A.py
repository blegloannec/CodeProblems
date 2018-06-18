#!/usr/bin/env python

from decimal import *
getcontext().prec = 100

T = int(raw_input())
for c in xrange(1,T+1):
    r,t = map(int,raw_input().split())
    D = Decimal((2*r-1)**2 + 8*t)
    n = max(0,int((Decimal(-2*r+1)+D.sqrt())/Decimal(4)))
    print 'Case #%d: %d' % (c,n)
