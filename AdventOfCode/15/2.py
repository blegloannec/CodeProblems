#!/usr/bin/env python

import sys

def cpt((l,w,h)):
    x,y,z = l*w,w*h,h*l
    return (2*x+2*y+2*z+min([x,y,z]),l*w*h+min([2*l+2*w,2*l+2*h,2*w+2*h]))

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    res,res2 = 0,0
    for l in cases:
        a,b = cpt(tuple(map(int,l.strip().split('x'))))
        res += a
        res2 += b
    print res,res2

main()
