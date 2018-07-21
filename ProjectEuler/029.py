#!/usr/bin/env python

from math import *

def problem29():
    l = []
    n = 100
    for a in range(2,n+1):
        for b in range(2,n+1):
            # h  = a**b
            # ou hashage malin :
            h = int(1000000*b*log(a))
            if h not in l:
                l.append(h)
    print len(l)

problem29()
