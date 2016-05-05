#!/usr/bin/env python

import sys

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def permut(N,C):
    res = []
    digits = range(N)
    for p in range(N-1,0,-1):
        f = fact(p)
        k = C/f
        res.append(digits[k])
        digits = digits[:k]+digits[k+1:]
        C -= k*f
    res.append(digits[0])
    return res

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print ''.join(map((lambda x: chr(x+ord('a'))),permut(13,N-1)))

main()
