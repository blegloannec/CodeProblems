#!/usr/bin/env python

import sys

def digits(b,n):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def pal(l):
    s = len(l)
    for i in xrange(s/2):
        if l[i]!=l[s-1-i]:
            return False
    return True

def main():
    N,K = map(int,sys.stdin.readline().split())
    res = 0
    for n in xrange(N):
        if pal(digits(10,n)) and pal(digits(K,n)):
            res += n
    print res

main()
