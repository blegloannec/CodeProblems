#!/usr/bin/env python

import sys

I = [map(int,L.split('-')) for L in sys.stdin.readlines()]
I.sort() # sorting intervals by start

# Part One
m = 0
for (a,b) in I:
    if a<=m<=b:
        m = b+1
    elif m<a: # no need to continue
        break
print m

# Part Two
F = [] # list of disjoint forbidden intervals 
for (a,b) in I:
    # new interval can only intersect the last of F
    # otherwise would contradict the sort
    if F and a<=F[-1][1]:
        F[-1] = (F[-1][0],max(b,F[-1][1]))
    else:
        F.append((a,b))
N = 4294967295+1
for (a,b) in F:
    N -= (b-a+1)
print N
