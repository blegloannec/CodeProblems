#!/usr/bin/env python

import sys

def abundants(NMAX):
    S = [1 for i in xrange(NMAX)]
    A = []
    for i in xrange(2,NMAX):
        if S[i]>i:
            A.append(i)
        for j in xrange(2*i,NMAX,i):
            S[j] += i
    return A

def main():
    NMAX = 28123
    A = abundants(NMAX)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        if n>28123:
            print 'YES'
            continue
        yes = False
        for a in A:
            if a>n/2:
                break
            if n-a in A:
                yes = True
                break
        print 'YES' if yes else 'NO'

main()
