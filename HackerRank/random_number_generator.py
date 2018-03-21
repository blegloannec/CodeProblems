#!/usr/bin/env python

from fractions import gcd

N = int(raw_input())
for _ in xrange(N):
    A,B,C = map(int,raw_input().split())
    m = min(max(0,C-B),A)
    M = min(A,C)
    # P = 1/A * (m + Integral((C-a)/B, a=m..M))
    q = 2*A*B
    p = 2*m*B + 2*C*(M-m)-(M*M-m*m)
    g = gcd(p,q)
    print('%d/%d' % (p/g,q/g))
