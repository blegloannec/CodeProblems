#!/usr/bin/env python

import sys

def main():
    gcmax = -1
    L = sys.stdin.readlines()
    i = 0
    while i<len(L):
        name = L[i][1:-1]
        s = ''
        i += 1
        while i<len(L) and L[i][0]!='>':
            s += L[i].strip()
            i += 1
        gc = 0
        for c in s:
            if c=='G' or c=='C':
                gc += 1
        gc = (100.*gc)/len(s)
        if gc>gcmax:
            namax = name
            gcmax = gc
    print namax
    print gcmax

main()
