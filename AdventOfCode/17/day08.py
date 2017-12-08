#!/usr/bin/env python3

import sys
from collections import defaultdict

def parse_instr(I):
    I = I.split(' if ')
    return tuple(I[0].split()+I[1].split())

P = list(map(parse_instr,sys.stdin.readlines()))

R = defaultdict(int)

def val(x):
    return R[x] if 'a'<=x[0]<='z' else int(x)

def test(I):
    a,b = val(I[3]),val(I[5])
    if I[4]=='==':
        return a==b
    elif I[4]=='!=':
        return a!=b
    elif I[4]=='<':
        return a<b
    elif I[4]=='>':
        return a>b
    elif I[4]=='<=':
        return a<=b
    elif I[4]=='>=':
        return a>=b

def simu(P):
    h = 0
    for I in P:
        if test(I):
            r,v = I[0],val(I[2])
            R[r] += (v if I[1]=='inc' else -v)
            h = max(h,R[r])
    return h

h = simu(P)
print(max(R[r] for r in R))  # Part 1
print(h)                     # Part 2
