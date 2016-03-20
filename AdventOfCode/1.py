#!/usr/bin/env python

import sys

def cpt(data):
    pos = 0
    res = 0
    for i in range(len(data)):
        res += 1 if data[i]=='(' else -1
        if pos==0 and res<0:
            pos = i+1
    return (res,pos)

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        print cpt(l.strip())

main()
