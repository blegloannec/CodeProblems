#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())-1
p = 3
while t>=p:
    t -= p
    p *= 2
print p-t
