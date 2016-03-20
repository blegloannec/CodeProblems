#!/usr/bin/env python

import sys
import re

instr = re.compile('([a-zA-Z]+) .+ ([0-9]+) .+ ([0-9]+) .+ ([0-9]+) .+')

def dist(T,(v,t,r)):
    tau = t+r
    return v*t*(T/tau)+v*min(t,T%tau)

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    R = {}
    for l in cases:
        s = l.strip()
        p = instr.match(s)
        R[p.group(1)] = (int(p.group(2)),int(p.group(3)),int(p.group(4)))
    S = {}
    for r in R:
        S[r] = 0
    for t in range(1,2504):
        dmax = 0
        best = []
        for r in R:
            d = dist(t,R[r])
            if d==dmax:
                best.append(r)
            elif d>dmax:
                best = [r]
                dmax = d
        for r in best:
            S[r] += 1
    print S

main()
