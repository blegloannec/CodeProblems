#!/usr/bin/env python

from math import *

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def problem34():
    # S(n) <= 9! log10(n)
    K = fact(9)
    s = 0
    i = 10
    while i<K*ceil(log10(i)):
        c = chiffres10(i)
        if sum(map(fact,c))==i:
            s += i
        i += 1
    print s

problem34()
