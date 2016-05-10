#!/usr/bin/env python

import sys

D = {'A':0, 'C':0, 'G':0, 'T':0}

def main():
    s = sys.stdin.readline().strip()
    for c in s:
        D[c] += 1
    print D['A'],D['C'],D['G'],D['T']

main()
