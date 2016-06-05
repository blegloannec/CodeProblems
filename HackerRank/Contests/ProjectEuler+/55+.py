#!/usr/bin/env python

import sys
from collections import *

def mirror(n):
    m = 0
    while n>0:
        m = 10*m + n%10
        n /= 10
    return m

def is_palindrome(n):
    return mirror(n)==n

def lychrel(n):
    if is_palindrome(n):
        return n
    k = 1
    while k<=60:
        n += mirror(n)
        if is_palindrome(n):
            return n
        k += 1
    return None

def main():
    N = int(sys.stdin.readline())
    maxp = 0
    maxc = 0
    D = defaultdict(int)
    for n in xrange(1,N+1):
        p = lychrel(n)
        if p!=None:
            D[p] += 1
            if D[p]>maxc:
                maxc = D[p]
                maxp = p
    print maxp,maxc

main()
