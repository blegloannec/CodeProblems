#!/usr/bin/env python

import sys
from bisect import *

def miroir(n):
    m = 0
    while n!=0:
        m = 10*m + n%10
        n /= 10
    return m

def palindrome(n):
    return miroir(n)==n

def palindromes():
    P = set()
    for i in xrange(100,1000):
        for j in xrange(i,1000):
            p = i*j
            if palindrome(p):
                P.add(p)
    return sorted(list(P))

def main():
    P = palindromes()
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        print P[bisect_left(P,N)-1]

main()
