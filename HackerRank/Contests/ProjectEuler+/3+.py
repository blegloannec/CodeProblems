#!/usr/bin/env python

import sys
from math import *

def maxdecomp(n):
    m = n
    p = 1
    if m%2==0:
        p = 2
        m /= 2
        while m%2==0:
            m /= 2
    i = 3
    s = int(sqrt(n))+1
    while m>1 and i<s:
        if m%i==0:
            p = i
            m /= i
            while m%i==0:
                m /= i
        i += 2
    return max(p,m)

def problem3():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        print maxdecomp(n)

problem3()
