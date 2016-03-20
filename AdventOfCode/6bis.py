#!/usr/bin/env python

import sys
import re

t = [[0 for j in range(1000)] for i in range(1000)]

instr = re.compile('[a-z]+ ([a-z]*) ?([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

def turn(b,x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            t[i][j] = max(0,t[i][j]+b)

def cpt():
    return sum(map(sum,t))
            
def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        s = l.strip()
        p = instr.match(s)
        b = 2 if (p.group(1)=='') else 1 if (p.group(1)=='on') else -1
        turn(b,int(p.group(2)),int(p.group(3)),int(p.group(4)),int(p.group(5)))
    print cpt()

main()
