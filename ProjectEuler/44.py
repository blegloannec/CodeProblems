#!/usr/bin/env python

from math import sqrt

# p = n(3n-1)/2
# 3n^2 - n - 2p = 0
# D = 1+24p
# et n = (1+sqrt(D))/6
# mais les solutions pour n<0 ont n = (1-sqrt(D))/6
# dans ce cas (1-sqrt(D))%6 == 0
# donc (1+sqrt(D))%6 == 2 != 0

def is_penta(p):
    D = 1+24*p
    d = int(sqrt(D))
    return (d*d==D and (1+d)%6==0)

NMAX=10000
def problem44():
    for n in range(1,NMAX):
        p = n*(3*n-1)/2
        for m in range(n+1,NMAX):
            q = m*(3*m-1)/2
            if is_penta(p+q) and is_penta(q-p):
                print q-p

problem44()
