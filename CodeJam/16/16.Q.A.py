#!/usr/bin/env python

import sys

def loop(n):
    k = 0
    s = set()
    while len(s)<10:
        k += 1
        m = k*n
        while m>0:
            s.add(m%10)
            m /= 10
    return k*n

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        a = int(sys.stdin.readline())
        if a==0:
            print 'Case #%d: INSOMNIA' % t
        else:
            print 'Case #%d: %d' % (t,loop(a))

main()
