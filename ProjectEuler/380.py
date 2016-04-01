#!/usr/bin/env python

from decimal import *
from math import *

def problem380():
    m = 500
    n = 100
    res = Decimal(1)
    for k in range(1,n):
        for h in range(1,m):
            res *= 4*sin(h*pi/(2*m))**2+4*sin(k*pi/(2*n))**2
            print res
    print res

problem380()
