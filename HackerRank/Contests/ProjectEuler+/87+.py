#!/usr/bin/env python

import sys
from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def main():
    P = eratosthene(100000)
    M = 10000001
    S = [0 for _ in xrange(M)]
    for a in P:
        A = a*a
        if A>=M:
            break
        for b in P:
            B = b*b*b
            if A+B>=M:
                break
            for c in P:
                X = A+B+c*c*c*c
                if X<M:
                    S[X] = 1
                else:
                    break
    for i in xrange(1,M):
        S[i] += S[i-1]
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        print S[int(sys.stdin.readline())]

main()
