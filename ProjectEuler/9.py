#!/usr/bin/env python

from math import sqrt

def problem9():
    for a in range(1,1000):
        for b in range(1,a+1):
            c = sqrt(a*a+b*b)
            if int(c)==c and a+b+c==1000:
                c = int(c)
                print a, b, c, a*b*c

problem9()
