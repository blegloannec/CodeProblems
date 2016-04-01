#!/usr/bin/env python

from math import *

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def problem30():
    # S(n) <= 9^5 log10(n)
    K = 9**5
    s = 0
    i = 2
    while i<K*ceil(log10(i)):
        c = chiffres10(i)
        if sum(map((lambda x: x**5),c))==i:
            s += i
        i += 1
    print s

problem30()
