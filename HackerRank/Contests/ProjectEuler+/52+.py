#!/usr/bin/env python

import sys
from math import log10

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def test(n,k):
    if int(log10(n))!=int(log10(k*n)):
        return False
    D = sorted(digits(n))
    for i in xrange(2,k+1):
        if sorted(digits(i*n))!=D:
            return False
    return True
    
def main():
    N,K = map(int,sys.stdin.readline().split())
    for n in xrange(1,N+1):
        if test(n,K):
            print ' '.join([str(k*n) for k in xrange(1,K+1)])

main()
