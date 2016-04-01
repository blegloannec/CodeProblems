#!/usr/bin/env python

from decimal import *
from math import *

# Kirchhoff's matrix tree theorem for grid graphs
# https://oeis.org/A116469
# T(m,n) = Prod(Prod( 4*sin(h*Pi/(2*m))^2+4*sin(k*Pi/(2*n))^2, h=1..m-1), k=1..n-1))))

def problem380():
    m = 500
    n = 100
    res = Decimal(1)
    for k in range(1,n):
        for h in range(1,m):
            res *= Decimal(4*sin(h*pi/(2*m))**2+4*sin(k*pi/(2*n))**2)
    print res

problem380()

# 6.320236506980189432845944257E+25093
# Solution: 6.3202e25093
