#!/usr/bin/env python

import sys

def digit(n):
    d = 1
    p = 1
    while n>=9*d*p:
        n -= 9*d*p
        d += 1
        p *= 10
    k = p+n/d
    D = []
    while k>0:
        D.append(k%10)
        k /= 10
    return D[-1-(n%d)]

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        I = map(int,sys.stdin.readline().split())
        res = 1
        for i in I:
            res *= digit(i-1)
        print res

main()
