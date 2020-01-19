#!/usr/bin/env python

import sys
import re

instr = re.compile('([a-z]+): ([0-9]+)[,\n]')

data = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def match_dict(d):
    for p in d:
        if d[p]!=data[p]:
            return False
    return True

def match_dict2(d):
    for p in d:
        if p in ['cats','trees']:
            if d[p]<=data[p]:
                return False
        elif p in ['pomeranians','goldfish']:
            if d[p]>=data[p]:
                return False
        elif d[p]!=data[p]:
            return False
    return True

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    A = []
    for l in cases:
        a = {}
        props = instr.findall(l)
        for p in props:
            a[p[0]] = int(p[1])
        A.append(a)
    for i in range(len(A)):
        if match_dict(A[i]):
            print 1,i+1
        if match_dict2(A[i]):
            print 2,i+1

main()
