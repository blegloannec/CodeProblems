#!/usr/bin/env python3

import sys
from math import sqrt, acos, pi

for L in sys.stdin.readlines():
    r,x,y = map(float, L.split())
    d = sqrt(x*x+y*y)
    if d>r:
        sys.stdout.write('miss\n')
    else:
        e = sqrt(r*r-d*d)
        a = acos(d/r)
        A = a*r*r - d*e
        B = pi*r*r - A
        if A<B:
            A,B = B,A
        sys.stdout.write(f'{A} {B}\n')
