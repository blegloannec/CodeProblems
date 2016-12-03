#!/usr/bin/env python

import sys

def cpt(s):
    i = 0
    c = 0
    c2 = 0
    while i<len(s):
        if s[i]=='\\' and i<len(s)-1:
            if s[i+1] in ['\\','"']:
                i += 2
                c2 += 4
            elif s[i+1]=='x':
                i += 4
                c2 += 5
            else:
                print "ERROR"
                i += 1
                c2 += 2
        else:
            i += 1
            c2 += 1
        c += 1
    return c,c2

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    r = 0
    r2 = 0
    for l in cases:
        s = l.strip()
        c = cpt(s[1:-1])
        r += len(s)-c[0]
        r2 += c[1]+6-len(s)
    print r,r2

main()
