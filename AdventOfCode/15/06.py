#!/usr/bin/env python

import sys
import re

t = [[False for j in range(1000)] for i in range(1000)]

instr = re.compile('[a-z]+ ([a-z]*) ?([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

def turn(b,x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            t[i][j] = b

def toggle(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            t[i][j] = not t[i][j]

def cpt():
    c = 0
    for i in range(0,1000):
        for j in range(0,1000):
            if t[i][j]:
                c += 1
    return c
            
def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        s = l.strip()
        p = instr.match(s)
        if p.group(1)=='':
            toggle(int(p.group(2)),int(p.group(3)),int(p.group(4)),int(p.group(5)))
        else:
            turn((p.group(1)=='on'),int(p.group(2)),int(p.group(3)),int(p.group(4)),int(p.group(5)))
    print cpt()

main()
