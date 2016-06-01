#!/usr/bin/env python

import sys

def main():
    N = int(sys.stdin.readline())
    S = map(int,sys.stdin.readline().split())
    X = reduce((lambda x,y: x^y), S)
    if X==0:
        print 0
        return
    leftmost1 = 1<<31
    while X&leftmost1==0:
        leftmost1 >>= 1
    cpt = 0
    for s in S:
        if s&leftmost1!=0:
            cpt += 1
    print cpt

main()
