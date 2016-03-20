#!/usr/bin/env python

import sys
import re

instr = re.compile('([a-zA-Z]+) .+ ([0-9]+) .+ ([0-9]+) .+ ([0-9]+) .+')

T = 2503

def dist(v,t,r):
    tau = t+r
    return v*t*(T/tau)+v*min(t,T%tau)

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        s = l.strip()
        p = instr.match(s)
        print p.group(1),dist(int(p.group(2)),int(p.group(3)),int(p.group(4)))

main()
