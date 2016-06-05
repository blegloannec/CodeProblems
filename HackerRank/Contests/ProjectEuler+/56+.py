#!/usr/bin/env python

import sys

def somme_chiffres10(n):
    s = 0
    while n>0:
        s += n%10
        n /= 10
    return s

def main():
    N = int(sys.stdin.readline())
    maxsum = 0
    for a in xrange(N):
        p = a
        for b in xrange(N):
            maxsum = max(maxsum,somme_chiffres10(p))
            p *= a
    print maxsum

main()
