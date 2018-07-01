#!/usr/bin/env python

# runs in <30s with pypy

from collections import defaultdict
from fractions import Fraction

def randgen(N):
    s = 290797
    T = []
    for _ in xrange(2*N):
        s = (s*s)%50515093
        T.append((s%2000)-1000)
    return T

def S(N):
    D = defaultdict(set)
    T = randgen(N)
    for i in xrange(N):
        xi,yi = T[2*i],T[2*i+1]
        for j in xrange(i):
            xj,yj = T[2*j],T[2*j+1]
            if xi!=xj:
                a = Fraction(yj-yi,xj-xi)  # slope
                # y = a(x-xi) + yi
                b = yi-a*xi                # y(0)
            else:
                a = float('inf')
                b = xi
            D[a].add(b)
    M = sum(len(D[a]) for a in D)
    res = 0
    for a in D:
        res += len(D[a])*(M-len(D[a]))
    return res

print S(2500)
