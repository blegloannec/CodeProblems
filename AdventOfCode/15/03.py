#!/usr/bin/env python

import sys

def cpt(data):
    px,py = 0,0
    pos = set([(px,py)])
    for d in data:
        if d=='<':
            px -= 1
        elif d=='>':
            px += 1
        elif d=='v':
            py -= 1
        elif d=='^':
            py += 1
        pos.add((px,py))
    return len(pos)

def cpt_bis(data):
    px,py = [0,0],[0,0]
    pos = set([(0,0)])
    for di in range(len(data)):
        d = data[di]
        if d=='<':
            px[di%2] -= 1
        elif d=='>':
            px[di%2] += 1
        elif d=='v':
            py[di%2] -= 1
        elif d=='^':
            py[di%2] += 1
        pos.add((px[di%2],py[di%2]))
    return len(pos)

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        data = l.strip()
        print cpt(data),cpt_bis(data)

main()
